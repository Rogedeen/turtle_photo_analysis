from dataclasses import dataclass, field
from typing import Optional, List, Dict

@dataclass(frozen=True)
class TheoreticalFeature:
    ozellik_adi: str
    teorik_deger: str
    gozlemle_uyumlu: bool

@dataclass(frozen=True)
class SpeciesDetail:
    tur_adi: str
    confidence: float
    teorik_ozellikler: List[TheoreticalFeature]

@dataclass(frozen=True)
class TurtleFeatures:
    olasi_turler: List[SpeciesDetail]
    api_model: str           # hangi model kullanıldı
    raw_response: str        # hata ayıklama için ham yanıt
    extraction_timestamp: str
