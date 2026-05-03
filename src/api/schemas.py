from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class EliminationStepSchema(BaseModel):
    feature_checked: str
    feature_value: str
    eliminated_species: List[str]
    reason: str

class DecisionResultSchema(BaseModel):
    predicted_species: Optional[str]
    common_name_tr: Optional[str]
    confidence: float
    confidence_level: str
    elimination_steps: List[EliminationStepSchema]
    remaining_candidates: List[str]
    features_used: Dict[str, Any]
