import unittest
from pathlib import Path
from rule_loader import RuleLoader, SpeciesRules

class TestRuleLoader(unittest.TestCase):
    """
    Unit tests for RuleLoader class.
    """

    def setUp(self):
        self.rulebook_path = "reports/morphological-rulebook.md"
        self.loader = RuleLoader(self.rulebook_path)

    def test_load_rules_not_empty(self):
        """Test if rules are loaded and not empty."""
        rules = self.loader.load_rules()
        self.assertIsInstance(rules, dict)
        self.assertGreater(len(rules), 0)

    def test_species_data_integrity(self):
        """Test if a specific species has correct data structure."""
        rules = self.loader.load_rules()
        species_name = "Trachemys scripta elegans"
        
        self.assertIn(species_name, rules)
        data = rules[species_name]
        
        self.assertEqual(data.scientific_name, species_name)
        self.assertEqual(data.common_name, "Kızıl Yanaklı Su Kaplumbağası")
        self.assertGreater(len(data.distinguishing_features), 0)
        self.assertGreater(len(data.elimination_features), 0)

    def test_vision_ai_question_parsing(self):
        """Test if Vision AI questions are correctly extracted."""
        rules = self.loader.load_rules()
        species_name = "Chelonia mydas"
        data = rules[species_name]
        
        # Check if first feature has a question
        first_feature = data.distinguishing_features[0]
        self.assertTrue(len(first_feature.vision_ai_question) > 0)
        self.assertIn("Gözlerin arasındaki alanda kaç çift büyük pul", first_feature.vision_ai_question)

    def test_file_not_found(self):
        """Test if loader handles missing file correctly."""
        with self.assertRaises(FileNotFoundError):
            bad_loader = RuleLoader("non_existent_file.md")
            bad_loader.load_rules()

if __name__ == "__main__":
    unittest.main()
