import pytest
from unittest.mock import MagicMock, patch
from src.feature_extraction.gemini_extractor import GeminiFeatureExtractor
from src.models import PreparedImage
from src.feature_extraction.models import TurtleFeatures

@pytest.fixture
def mock_prepared_image():
    return PreparedImage(
        base64_data="iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mP8/5+hHgAHggJ/PchI7wAAAABJRU5ErkJggg==",
        original_filename="test_turtle.jpg",
        original_size=(1024, 768),
        processed_size=(512, 512),
        format="jpeg",
        file_size_bytes=1024,
        prep_timestamp="2026-05-03T12:00:00"
    )

@pytest.mark.asyncio
async def test_gemini_extraction_success(mock_prepared_image):
    extractor = GeminiFeatureExtractor()
    
    # Gerçek API çağrısını mocklayabiliriz ancak mevcut implementasyon simüle ediyor.
    features = await extractor.extract_features(mock_prepared_image)
    
    assert isinstance(features, TurtleFeatures)
    assert features.yanak_seridi in ["evet", "hayır", "belirsiz"]
    assert features.api_model == "gemini-1.5-flash"

def test_prompt_builder():
    from src.feature_extraction.prompt_builder import PromptBuilder
    builder = PromptBuilder()
    prompt = builder.build_prompt()
    
    assert "kaplumbağa biyologu" in prompt
    assert "JSON" in prompt
    assert "yanak_seridi" in prompt
