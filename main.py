import base64
import os
from datetime import datetime
from typing import Dict, Any, List

from src.models import PreparedImage
from src.interfaces import IDecisionEngine, DecisionResult, EliminationStep
from src.feature_extraction.interfaces import IFeatureExtractor
from src.image_prep.interfaces import IImagePreparer

# --- Mock Implementations ---

class MockImagePreparer(IImagePreparer):
    def prepare(self, image_path: str) -> PreparedImage:
        print(f"DEBUG: [MockImagePreparer] Processing {image_path}...")
        return PreparedImage(
            base64_data="dummy_base64",
            original_filename=os.path.basename(image_path),
            original_size=(2000, 2000),
            processed_size=(1024, 1024),
            format="jpeg",
            file_size_bytes=102400,
            prep_timestamp=datetime.now().isoformat()
        )

class MockFeatureExtractor(IFeatureExtractor):
    def extract_features(self, image: PreparedImage) -> Dict[str, Any]:
        print(f"DEBUG: [MockFeatureExtractor] Extracting features from {image.original_filename}...")
        # Simulating finding a Green Sea Turtle
        return {
            "ayak_yapisi": "perde",
            "prefrontal_pul_sayisi": "1",
            "lateral_skut_sayisi": "4",
            "kiremit_dizilimi": "hayır",
            "yanak_seridi": "hayır"
        }

class MockDecisionEngine(IDecisionEngine):
    def decide(self, features: Dict[str, Any]) -> DecisionResult:
        print(f"DEBUG: [MockDecisionEngine] Making decision based on: {features}")
        
        steps = [
            EliminationStep(
                feature_checked="ayak_yapisi",
                feature_value="perde",
                eliminated_species=["Trachemys scripta elegans", "Testudo graeca", "Testudo hermanni", "Mauremys rivulata"],
                reason="Perde ayak yapısı sadece deniz kaplumbağalarında bulunur."
            ),
            EliminationStep(
                feature_checked="lateral_skut_sayisi",
                feature_value="4",
                eliminated_species=["Caretta caretta"],
                reason="Caretta caretta'da lateral sküt sayısı 5 veya daha fazladır."
            )
        ]
        
        return DecisionResult(
            predicted_species="Chelonia mydas",
            common_name_tr="Yeşil Deniz Kaplumbağası",
            confidence=0.85,
            confidence_level="Orta",
            elimination_steps=steps,
            remaining_candidates=["Chelonia mydas", "Eretmochelys imbricata"],
            features_used=features
        )

# --- Orchestrator Logic ---

class TurtleVisionOrchestrator:
    def __init__(
        self, 
        preparer: IImagePreparer, 
        extractor: IFeatureExtractor, 
        engine: IDecisionEngine
    ):
        self.preparer = preparer
        self.extractor = extractor
        self.engine = engine

    def run_pipeline(self, image_path: str):
        print("=== TurtleVision Pipeline Started ===")
        
        # 1. Image Prep
        prepared = self.preparer.prepare(image_path)
        print(f"✓ Image prepared: {prepared.processed_size} ({prepared.file_size_bytes // 1024} KB)")
        
        # 2. Feature Extraction
        features = self.extractor.extract_features(prepared)
        print(f"✓ Features extracted: {list(features.keys())}")
        
        # 3. Decision Tree
        result = self.engine.decide(features)
        
        print("\n=== FINAL RESULT ===")
        print(f"Species: {result.predicted_species} ({result.common_name_tr})")
        print(f"Confidence: {result.confidence_level} ({result.confidence*100}%)")
        print("\nElimination Logic:")
        for step in result.elimination_steps:
            print(f"- Checked {step.feature_checked} ({step.feature_value}): Elimated {len(step.eliminated_species)} species. Reason: {step.reason}")
        
        print("\n=== Pipeline Completed Successfully ===")

if __name__ == "__main__":
    # In a real app, these would be the actual Gemini/OpenCV implementations
    orchestrator = TurtleVisionOrchestrator(
        preparer=MockImagePreparer(),
        extractor=MockFeatureExtractor(),
        engine=MockDecisionEngine()
    )
    
    # Mocking a test run
    orchestrator.run_pipeline("test_turtle.jpg")
