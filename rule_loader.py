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
        
        # Normalize line endings
        content = content.replace('\r\n', '\n')
        
        # Split by the species marker specifically
        # Pattern: **n. Tür:** 
        sections = re.split(r'\n(?=\*\*\d+\.\s*T[uü]r:)', content)
        
        for section in sections:
            if "Tür:" in section or "Tur:" in section:
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
        name_pattern = r'\*\*\d+\.\s*T[uü]r:\*\*\s*\*([^*]+)\*\s*/\s*([^\n\r]+)'
        name_match = re.search(name_pattern, section)
        
        if not name_match:
            return None
        
        sci_name = name_match.group(1).strip()
        common_name = name_match.group(2).strip()

        # Extract Distinguishing Features
        dist_features = []
        # Pattern to match bullets and questions
        # Matches: - **Feature**: Desc -> Vision AI Question: "Text"
        # Using a very permissive regex for characters between feature and arrow
        feature_pattern = r'-\s*\*\*([^*]+)\*\*:(.*?)(?:-|\u2192|->)\s*Vision\s+AI\s+sorusu:\s*"([^"]+)"'
        
        # New approach: split by lines and parse each line
        for line in section.split('\n'):
            line = line.strip()
            if line.startswith('-') and 'Vision AI sorusu:' in line:
                # Use a more flexible regex that doesn't rely on strict colon positioning after **
                m = re.search(r'-\s*\*\*([^*]+)\*\*.*?(?:-|\u2192|->)\s*Vision\s+AI\s+sorusu:\s*"([^"]+)"', line, re.IGNORECASE)
                if m:
                    char_name, question = m.groups()
                    # Description is everything between the feature name and the arrow
                    # We re-extract it for cleaner logic
                    desc_match = re.search(rf'\*\*{re.escape(char_name)}\*\*:(.*?)(?:-|\u2192|->)', line)
                    description = desc_match.group(1).strip() if desc_match else ""
                    
                    dist_features.append(MorphologicalRule(
                        characteristic=f"{char_name.strip()}: {description}",
                        vision_ai_question=question.strip()
                    ))

        # Extract Elimination Features
        elim_features = []
        # Looking for the elimination section and getting all bullted items after it
        elim_section_start = "Bu türü kesin eleyecek özellikler:**"
        if elim_section_start in section:
            parts = section.split(elim_section_start)
            if len(parts) > 1:
                elim_text = parts[1].strip()
                # Split by lines and take lines starting with -
                for line in elim_text.split('\n'):
                    line = line.strip()
                    if line.startswith('-'):
                        elim_features.append(line[1:].strip())
                    elif line and not line.startswith('*') and not line.startswith('-'): # Stop if next section starts
                        break

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
