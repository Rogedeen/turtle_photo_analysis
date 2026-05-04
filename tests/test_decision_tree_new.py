import unittest
from src.decision_tree import TurtleDecisionTree
from src.interfaces import DecisionResult

class TestDecisionTree(unittest.TestCase):
    def setUp(self):
        self.rulebook_path = "reports/morphological-rulebook.md"
        self.tree = TurtleDecisionTree(self.rulebook_path)

    def test_gemini_guaranteed_candidate(self):
        features = {
            "olasi_turler": [
                {"tur": "Trachemys scripta elegans", "confidence": 0.98},
                {"tur": "Chelonia mydas", "confidence": 0.02}
            ],
            "ayak_yapisi": "perde",
            "yanak_seridi": "hayır"
        }
        result = self.tree.decide(features)
        self.assertEqual(result.predicted_species, "Trachemys scripta elegans")
        self.assertLess(result.confidence, 0.98)
        self.assertGreater(result.confidence, 0.0)

    def test_ideal_features_return(self):
        features = {
            "olasi_turler": [{"tur": "Chelonia mydas", "confidence": 0.90}]
        }
        result = self.tree.decide(features)
        self.assertEqual(result.predicted_species, "Chelonia mydas")
        self.assertIn("predicted_features", result.features_used)
        self.assertEqual(result.features_used["predicted_features"]["kafa_pul_sayisi"], "2")

if __name__ == "__main__":
    unittest.main()
