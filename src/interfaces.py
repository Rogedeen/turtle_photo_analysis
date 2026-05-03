from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict, Optional, Any

@dataclass
class EliminationStep:
    feature_checked: str
    feature_value: str
    eliminated_species: List[str]
    reason: str

@dataclass
class DecisionResult:
    predicted_species: Optional[str]
    common_name_tr: Optional[str]
    confidence: float
    confidence_level: str        # "Yüksek" | "Orta" | "Düşük"
    elimination_steps: List[EliminationStep]
    remaining_candidates: List[str]
    features_used: Dict[str, Any]

class IDecisionEngine(ABC):
    @abstractmethod
    def decide(self, features: Dict[str, Any]) -> DecisionResult:
        pass
