import os
from src.image_prep.preparer import ImagePreparer
from src.feature_extraction.gemini_extractor import GeminiFeatureExtractor
from src.decision_tree import TurtleDecisionTree

def get_image_preparer() -> ImagePreparer:
    """Provides an instance of ImagePreparer"""
    return ImagePreparer()

def get_feature_extractor() -> GeminiFeatureExtractor:
    """Provides an instance of GeminiFeatureExtractor"""
    return GeminiFeatureExtractor()

def get_decision_tree() -> TurtleDecisionTree:
    """Provides an instance of TurtleDecisionTree"""
    # Look for the rulebook. In our setup, it's in reports/morphological-rulebook.md
    # We should ensure the path is absolute or relatively correct.
    rulebook_path = os.path.join(os.getcwd(), "reports", "morphological-rulebook.md")
    if not os.path.exists(rulebook_path):
        # Fallback to rules directory if needed, but per workspace info it's in reports/morphological-rulebook.md
        rulebook_path = os.path.join(os.getcwd(), "rules", "morphological-rulebook.md")
        
    return TurtleDecisionTree(rulebook_path=rulebook_path)
