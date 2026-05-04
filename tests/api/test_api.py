import pytest
import io
from fastapi.testclient import TestClient
from unittest.mock import Mock, AsyncMock, patch

from src.api.main import app
from src.api.dependencies import get_image_preparer, get_feature_extractor, get_decision_tree
from src.models import PreparedImage
from src.feature_extraction.models import TurtleFeatures
from src.interfaces import DecisionResult, EliminationStep

# Setup mocked results
mock_prepared_image = PreparedImage(
    base64_data="dummy_b64",
    original_filename="test.jpg",
    original_size=(800, 600),
    processed_size=(400, 300),
    format="jpeg",
    file_size_bytes=1024,
    prep_timestamp="2026-05-03T12:00:00"
)

mock_features = TurtleFeatures(
    olasi_turler=[],
    api_model="gemini-mock",
    raw_response="{}",
    extraction_timestamp="2026-05-03T12:00:00"
)

mock_decision_result = DecisionResult(
    predicted_species="Trachemys scripta elegans",
    common_name_tr="Kırmızı Yanaklı Su Kaplumbağası",
    confidence=0.9,
    confidence_level="Yüksek",
    elimination_steps=[
        EliminationStep(feature_checked="yanak_seridi", feature_value="evet", eliminated_species=["Emys orbicularis"], reason="Yanak şeridi var")
    ],
    remaining_candidates=[],
    features_used={"yanak_seridi": "evet"}
)

@pytest.fixture
def override_dependencies():
    # Mock ImagePreparer
    mock_preparer = Mock()
    mock_preparer.prepare_image.return_value = mock_prepared_image
    
    # Mock FeatureExtractor
    mock_extractor = AsyncMock()
    mock_extractor.extract_features.return_value = mock_features
    
    # Mock DecisionTree
    mock_tree = Mock()
    mock_tree.decide.return_value = mock_decision_result
    
    app.dependency_overrides[get_image_preparer] = lambda: mock_preparer
    app.dependency_overrides[get_feature_extractor] = lambda: mock_extractor
    app.dependency_overrides[get_decision_tree] = lambda: mock_tree
    
    yield mock_preparer, mock_extractor, mock_tree
    
    app.dependency_overrides.clear()

@pytest.fixture
def client():
    return TestClient(app)

def test_analyze_endpoint_success(client, override_dependencies):
    mock_preparer, mock_extractor, mock_tree = override_dependencies
    
    # Create a dummy image file
    file_content = b"dummy file content"
    files = {"file": ("test.jpg", io.BytesIO(file_content), "image/jpeg")}
    
    response = client.post("/api/v1/analyze", files=files)
    
    assert response.status_code == 200
    data = response.json()
    assert data["predicted_species"] == "Trachemys scripta elegans"
    assert data["confidence"] == 0.9
    assert len(data["elimination_steps"]) == 1
    
    # Verify mocked methods were called
    mock_preparer.prepare_image.assert_called_once()
    mock_extractor.extract_features.assert_called_once()
    mock_tree.decide.assert_called_once()

def test_analyze_endpoint_image_prep_error(client, override_dependencies):
    mock_preparer, mock_extractor, mock_tree = override_dependencies
    
    mock_preparer.prepare_image.side_effect = Exception("Compression failed")
    
    file_content = b"dummy"
    files = {"file": ("test.jpg", io.BytesIO(file_content), "image/jpeg")}
    response = client.post("/api/v1/analyze", files=files)
    
    assert response.status_code == 422
    assert "Image preparation failed" in response.json()["detail"]

def test_analyze_endpoint_feature_extraction_error(client, override_dependencies):
    mock_preparer, mock_extractor, mock_tree = override_dependencies
    
    mock_extractor.extract_features.side_effect = Exception("API timeout")
    
    file_content = b"dummy"
    files = {"file": ("test.jpg", io.BytesIO(file_content), "image/jpeg")}
    response = client.post("/api/v1/analyze", files=files)
    
    assert response.status_code == 502
    assert "Feature extraction failed" in response.json()["detail"]

def test_analyze_endpoint_decision_tree_error(client, override_dependencies):
    mock_preparer, mock_extractor, mock_tree = override_dependencies
    
    mock_tree.decide.side_effect = Exception("Rule parsing failed")
    
    file_content = b"dummy"
    files = {"file": ("test.jpg", io.BytesIO(file_content), "image/jpeg")}
    response = client.post("/api/v1/analyze", files=files)
    
    assert response.status_code == 500
    assert "Decision engine failure" in response.json()["detail"]

def test_cors_headers(client):
    # Test CORS headers for preflight request
    headers = {
        "Origin": "http://localhost:5173",
        "Access-Control-Request-Method": "POST",
        "Access-Control-Request-Headers": "X-Requested-With",
    }
    response = client.options("/api/v1/analyze", headers=headers)
    assert response.status_code == 200
    assert response.headers.get("access-control-allow-origin") == "http://localhost:5173"
