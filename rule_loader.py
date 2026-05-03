import re
from dataclasses import dataclass
from typing import List, Dict, Optional
from pathlib import Path

@dataclass
class MorphologicalRule:
    """Represents a single morphological rule for a turtle species."""
    characteristic: str
    vision_ai_question: str

@dataclass
class SpeciesRules:
    """Represents all rules associated with a specific turtle species."""
    scientific_name: str
    common_name: str
    distinguishing_features: List[MorphologicalRule]
    elimination_features: List[str]

class RuleLoader:
    """
    Loads morphological rules from a markdown file into a dictionary.
    Follows SOLID principles and Clean Code rules.
    """

    def __init__(self, rulebook_path: str):
        self.rulebook_path = Path(rulebook_path)
        self.elimination_rules: Dict[str, SpeciesRules] = {}

    def load_rules(self) -> Dict[str, SpeciesRules]:
        """
        Reads the markdown file and parses the rules for each species.
        """
        if not self.rulebook_path.exists():
            raise FileNotFoundError(f"Rulebook not found at {self.rulebook_path}")

        content = self.rulebook_path.read_text(encoding="utf-8")
        self.elimination_rules = self._parse_markdown(content)
        return self.elimination_rules

    def _parse_markdown(self, content: str) -> Dict[str, SpeciesRules]:
        """
        Parses the markdown content using regex to extract species and their rules.
        """
        rules_dict = {}
        
        # Split by species sections (header with "Tür:")
        # Looking for sections starting with **n. Tür:**
        sections = re.split(r'\n(?=\*\*\d+\.\s*Tür:)', content)
        
        for section in sections:
            if "Tür:" in section:
                species_data = self._parse_species_section(section)
                if species_data:
                    rules_dict[species_data.scientific_name] = species_data
                    
        return rules_dict

    def _parse_species_section(self, section: str) -> Optional[SpeciesRules]:
        """
        Parses a single species section to extract its details.
        """
        # Extract scientific and common name
        # Format: **1. Tür:** *Scientific Name* / Common Name
        name_pattern = r'\*\*\d+\.\s*Tür:\*\*\s*\*([^*]+)\*\s*/\s*([^\n\r]+)'
        name_match = re.search(name_pattern, section)
        
        if not name_match:
            # Try a slightly looser pattern
            name_pattern = r'Tür:\*\*?\s*\*([^*]+)\*\s*/\s*([^\n\r]+)'
            name_match = re.search(name_pattern, section)
            
        if not name_match:
            return None
        
        sci_name = name_match.group(1).strip()
        common_name = name_match.group(2).strip()

        # Extract Distinguishing Features
        dist_features = []
        # Support both -> and → characters
        feature_pattern = r'-\s*\*\*([^*]+)\*\*:(.*?)[\-\→]\s*Vision AI sorusu:\s*"([^"]+)"'
        items = re.findall(feature_pattern, section, re.DOTALL)
        
        for item in items:
            char_name, description, question = item
            dist_features.append(MorphologicalRule(
                characteristic=f"{char_name.strip()}: {description.strip()}",
                vision_ai_question=question.strip()
            ))

        # Extract Elimination Features
        elim_features = []
        elim_section_pattern = r'\*\*Bu türü kesin eleyecek özellikler:\*\*(.*?)(?=\n\n|\Z)'
        elim_section_match = re.search(elim_section_pattern, section, re.DOTALL)
        
        if elim_section_match:
            elim_text = elim_section_match.group(1).strip()
            # Find bulleted lines
            elim_items = re.findall(r'-\s*(.*)', elim_text)
            elim_features = [item.strip() for item in elim_items if item.strip()]

        return SpeciesRules(
            scientific_name=sci_name,
            common_name=common_name,
            distinguishing_features=dist_features,
            elimination_features=elim_features
        )

if __name__ == "__main__":
    # Example usage
    loader = RuleLoader("reports/morphological-rulebook.md")
    rules = loader.load_rules()
    for species, data in rules.items():
        print(f"Loaded: {species} ({data.common_name})")
        print(f"  Features: {len(data.distinguishing_features)}")
        print(f"  Elimination Rules: {len(data.elimination_features)}")
