import json
import re
from datetime import datetime
from src.feature_extraction.models import TurtleFeatures, SpeciesDetail, TheoreticalFeature
from src.feature_extraction.exceptions import ParserError

class ResponseParser:
    def _sanitize_json(self, text: str) -> str:
        """JSON içindeki geçersiz kontrol karakterlerini temizler."""
        # \x00-\x1F ve \x7F kontrol karakterlerini kaldırır (ancak \n, \r, \t gibi yaygın olanları koruyabiliriz 
        # veya json.loads'un strict=False parametresini kullanabiliriz)
        # En güvenli yol kontrol karakterlerini temizlemektir.
        return re.sub(r'[\x00-\x1F\x7F]', '', text)

    def parse(self, raw_response: str, model_name: str) -> TurtleFeatures:
        try:
            # ... existing cleaning logic (extracted from above for brevity in this tool call)
            json_match = re.search(r'```json\s*(.*?)\s*```', raw_response, re.DOTALL)
            if json_match:
                clean_json = json_match.group(1)
            else:
                clean_json = raw_response.strip()
                if clean_json.startswith("```"):
                    clean_json = re.sub(r'^```(?:json)?', '', clean_json)
                if clean_json.endswith("```"):
                    clean_json = re.sub(r'```$', '', clean_json)
            
            clean_json = clean_json.strip()
            clean_json = self._sanitize_json(clean_json)

            data = json.loads(clean_json, strict=False)
            
            olasi_turler_data = data.get("olasi_turler", [])
            olasi_turler = []
            
            for tur_data in olasi_turler_data:
                teorik_ozellikler = [
                    TheoreticalFeature(
                        ozellik_adi=feat.get("ozellik_adi", "Bilinmiyor"),
                        teorik_deger=feat.get("teorik_deger", "Bilinmiyor"),
                        gozlemle_uyumlu=feat.get("gozlemle_uyumlu", False)
                    )
                    for feat in tur_data.get("teorik_ozellikler", [])
                ]
                
                olasi_turler.append(SpeciesDetail(
                    tur_adi=tur_data.get("tur_adi", "Bilinmeyen Tür"),
                    confidence=float(tur_data.get("confidence", 0.0)),
                    teorik_ozellikler=teorik_ozellikler
                ))

            return TurtleFeatures(
                olasi_turler=olasi_turler,
                api_model=model_name,
                raw_response=raw_response,
                extraction_timestamp=datetime.now().isoformat()
            )
        except Exception as e:
            raise ParserError(f"JSON parsing or mapping failed: {str(e)}")
