from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class TurtleFeatures:
    yanak_seridi: str        # "evet" | "hayır" | "belirsiz"
    gaga_yapisi: str         # "düz" | "hafif_kıvrık" | "kanca" | "belirsiz"
    kabuk_rengi: str
    kabuk_sari_benek: str
    boyun_deseni: str
    ayak_yapisi: str         # "perde" | "pençe" | "belirsiz"
    kabuk_kenari: str        # "düz" | "girintili" | "belirsiz"
    kafa_pul_sayisi: str     # "2" | "4" | "belirsiz"
    api_model: str           # hangi model kullanıldı
    raw_response: str        # hata ayıklama için ham yanıt
    extraction_timestamp: str
