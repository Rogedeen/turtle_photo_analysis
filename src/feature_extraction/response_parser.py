import json
from datetime import datetime
from src.feature_extraction.models import TurtleFeatures
from src.feature_extraction.exceptions import ParserError

class ResponseParser:
    def parse(self, raw_json: str, model_name: str) -> TurtleFeatures:
        try:
            # Markdown code block temizleme
            clean_json = raw_json.strip()
            if clean_json.startswith("```json"):
                clean_json = clean_json[7:]
            if clean_json.endswith("```"):
                clean_json = clean_json[:-3]
            clean_json = clean_json.strip()

            data = json.loads(clean_json)
            
            return TurtleFeatures(
                yanak_seridi=data.get("yanak_seridi", "belirsiz"),
                gaga_yapisi=data.get("gaga_yapisi", "belirsiz"),
                kabuk_rengi=data.get("kabuk_rengi", "belirsiz"),
                kabuk_sari_benek=data.get("kabuk_sari_benek", "belirsiz"),
                boyun_deseni=data.get("boyun_deseni", "belirsiz"),
                ayak_yapisi=data.get("ayak_yapisi", "belirsiz"),
                kabuk_kenari=data.get("kabuk_kenari", "belirsiz"),
                kafa_pul_sayisi=data.get("kafa_pul_sayisi", "belirsiz"),
                api_model=model_name,
                raw_response=raw_json,
                extraction_timestamp=datetime.now().isoformat()
            )
        except Exception as e:
            raise ParserError(f"Failed to parse API response: {str(e)}")
