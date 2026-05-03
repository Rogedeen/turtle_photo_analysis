import unittest
from src.decision_tree import TurtleDecisionTree
from src.interfaces import DecisionResult

class TestDecisionTree(unittest.TestCase):
    def setUp(self):
        self.rulebook_path = "reports/morphological-rulebook.md"
        self.tree = TurtleDecisionTree(self.rulebook_path)

    def test_initialization(self):
        """Rulebook'un doğru yüklendiğini kontrol et."""
        self.assertGreater(len(self.tree.species_rules), 0)
        self.assertIn("Chelonia mydas", self.tree.species_rules)

    def test_habitat_filter_marine(self):
        """Deniz kaplumbağası filtresini kontrol et."""
        features = {"ayak_yapisi": "perde"}
        result = self.tree.decide(features)
        
        # Sadece deniz kaplumbağaları kalmalı
        deniz_turleri = ["Chelonia mydas", "Caretta caretta", "Eretmochelys imbricata", "Dermochelys coriacea"]
        for candidate in result.remaining_candidates:
            self.assertIn(candidate, deniz_turleri)

    def test_habitat_filter_land(self):
        """Kara kaplumbağası filtresini kontrol et."""
        features = {"ayak_yapisi": "pençe"}
        result = self.tree.decide(features)
        
        # Deniz kaplumbağaları elenmeli
        deniz_turleri = ["Chelonia mydas", "Caretta caretta", "Eretmochelys imbricata", "Dermochelys coriacea"]
        for candidate in result.remaining_candidates:
            self.assertNotIn(candidate, deniz_turleri)

    def test_elimination_by_feature(self):
        """Özellik bazlı elemeyi kontrol et (Trachemys)."""
        # Yanak şeridi yoksa Trachemys elenmeli
        features = {"yanak_seridi": "hayır"}
        result = self.tree.decide(features)
        self.assertNotIn("Trachemys scripta elegans", result.remaining_candidates)

    def test_full_elimination_to_single_species(self):
        """Tek bir türe kadar eleme sürecini test et."""
        features = {
            "ayak_yapisi": "perde",
            "prefrontal_pul_sayisi": "1",
            "lateral_skut_sayisi": "4",
            "kiremit_dizilimi": "hayır"
        }
        result = self.tree.decide(features)
        self.assertEqual(result.predicted_species, "Chelonia mydas")
        self.assertEqual(result.confidence_level, "Orta") # 4/8 özellik

    def test_different_species_eliminations(self):
        """Farklı türlerin eleme kurallarını test et."""
        # Caretta caretta eleme: lateral_skut_sayisi == 4
        res = self.tree.decide({"lateral_skut_sayisi": "4", "ayak_yapisi": "perde"})
        self.assertNotIn("Caretta caretta", res.remaining_candidates)
        
        # Eretmochelys eleme: kiremit_dizilimi == hayır
        res = self.tree.decide({"kiremit_dizilimi": "hayır", "ayak_yapisi": "perde"})
        self.assertNotIn("Eretmochelys imbricata", res.remaining_candidates)
        
        # Testudo graeca eleme: uyluk_mahmuzu == hayır
        res = self.tree.decide({"uyluk_mahmuzu": "hayır", "ayak_yapisi": "pençe"})
        self.assertNotIn("Testudo graeca", res.remaining_candidates)

        # Testudo hermanni eleme: kuyruk_mahmuzu == hayır
        res = self.tree.decide({"kuyruk_mahmuzu": "hayır", "ayak_yapisi": "pençe"})
        self.assertNotIn("Testudo hermanni", res.remaining_candidates)

        # Dermochelys eleme: sert_plaka_var_mi == evet
        res = self.tree.decide({"sert_plaka_var_mi": "evet", "ayak_yapisi": "perde"})
        self.assertNotIn("Dermochelys coriacea", res.remaining_candidates)

    def test_all_eliminated(self):
        """Tüm türlerin elendiği durumu test et."""
        features = {
            "ayak_yapisi": "perde",
            "sert_plaka_var_mi": "evet", # Dermochelys elendi
            "yanak_seridi": "hayır", # Trachemys (zaten elenmişti ama kural çalışsın)
            "lateral_skut_sayisi": "4", # Caretta elendi
            "kiremit_dizilimi": "hayır", # Eretmochelys elendi
            "prefrontal_pul_sayisi": "2" # Chelonia elendi (Gerçekte 3-4 tür kaldıysa da pul sayısı önemli)
        }
        result = self.tree.decide(features)
        self.assertEqual(len(result.remaining_candidates), 0)
        self.assertIsNone(result.predicted_species)
        """Log dosyasının oluşturulduğunu ve yazıldığını kontrol et."""
        import os
        log_path = "reports/test-decision-log.md"
        if os.path.exists(log_path):
            os.remove(log_path)
            
        tree = TurtleDecisionTree(self.rulebook_path, log_path=log_path)
        tree.decide({"ayak_yapisi": "pençe"})
        
        self.assertTrue(os.path.exists(log_path))
        with open(log_path, "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("Karar Süreci Başladı", content)
            self.assertIn("ayak_yapisi tespit edildi", content)

    def test_habitat_filter_marine(self):
        """Güven seviyelerinin doğru atandığını kontrol et."""
        res_high = self.tree._build_result("Test", 0.8, [], [], {})
        self.assertEqual(res_high.confidence_level, "Yüksek")
        
        res_mid = self.tree._build_result("Test", 0.5, [], [], {})
        self.assertEqual(res_mid.confidence_level, "Orta")
        
        res_low = self.tree._build_result("Test", 0.2, [], [], {})
        self.assertEqual(res_low.confidence_level, "Düşük")

if __name__ == "__main__":
    unittest.main()
