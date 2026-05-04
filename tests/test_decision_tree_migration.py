import unittest
from src.decision_tree import TurtleDecisionTree
from src.interfaces import DecisionResult

class TestDecisionTreeMigration(unittest.TestCase):
    def setUp(self):
        self.rulebook_path = "reports/morphological-rulebook.md"
        self.tree = TurtleDecisionTree(self.rulebook_path)

    def test_gemini_dominance(self):
        """Gemini adayının elenmediğini ve yüksek ağırlığa sahip olduğunu kontrol et."""
        features = {
            "olasi_turler": [
                {"tur": "Trachemys scripta elegans", "confidence": 0.90},
                {"tur": "Chelonia mydas", "confidence": 0.10}
            ],
            "ayak_yapisi": "perde", # Trachemys normalde pençedir
        }
        result = self.tree.decide(features)
        
        # Eleme yasak, Trachemys seçilmeli
        self.assertEqual(result.predicted_species, "Trachemys scripta elegans")
        # Güven %90'a çok yakın olmalı (Çünkü %95 Gemini ağırlığı var)
        self.assertGreater(result.confidence, 0.85)

    def test_top_3_comparison_structure(self):
        """top_3_comparison yapısının doğru döndüğünü kontrol et."""
        features = {
            "olasi_turler": [
                {"tur": "Chelonia mydas", "confidence": 0.90},
                {"tur": "Caretta caretta", "confidence": 0.05},
                {"tur": "Dermochelys coriacea", "confidence": 0.03}
            ]
        }
        result = self.tree.decide(features)
        
        self.assertIsNotNone(result.top_3_comparison)
        self.assertEqual(len(result.top_3_comparison), 3)
        self.assertEqual(result.top_3_comparison[0]["species_key"], "Chelonia mydas")
        # DB'den gelen gerçek özelliklerin varlığını kontrol et
        self.assertIn("ayak_yapisi", result.top_3_comparison[0])
        self.assertEqual(result.top_3_comparison[0]["ayak_yapisi"], "perde")

    def test_no_elimination_all_remain(self):
        """Herhangi bir türün elenmediğini kontrol et."""
        features = {
            "olasi_turler": [
                {"tur": "Chelonia mydas", "confidence": 0.70},
                {"tur": "Testudo graeca", "confidence": 0.30}
            ],
            "ayak_yapisi": "pençe" # Chelonia için çelişki
        }
        result = self.tree.decide(features)
        # Tüm adaylar listede kalmalı
        self.assertIn("Chelonia mydas", result.remaining_candidates)
        self.assertIn("Testudo graeca", result.remaining_candidates)

if __name__ == "__main__":
    unittest.main()
