import base64
from datetime import datetime
from src.models import PreparedImage
from src.feature_extraction.interfaces import IFeatureExtractor
from src.feature_extraction.models import TurtleFeatures
from src.feature_extraction.config import GeminiConfig
from src.feature_extraction.prompt_builder import PromptBuilder
from src.feature_extraction.response_parser import ResponseParser
from src.feature_extraction.exceptions import APIError

class GeminiFeatureExtractor(IFeatureExtractor):
    def __init__(self, config: GeminiConfig = None):
        self.config = config or GeminiConfig()
        self.prompt_builder = PromptBuilder()
        self.parser = ResponseParser()

    async def extract_features(self, image: PreparedImage) -> TurtleFeatures:
        prompt = self.prompt_builder.build_prompt()
        
        # Gerçek implementation'da burada google-generativeai kütüphanesi kullanılır.
        # Bu görev kapsamında API çağrısı simüle edilmektedir.
        try:
            # Simüle edilmiş API yanıtı
            simulated_response = """
            {
              "yanak_seridi": "evet",
              "gaga_yapisi": "düz",
              "kabuk_rengi": "yeşil",
              "kabuk_sari_benek": "hayır",
              "boyun_deseni": "evet",
              "ayak_yapisi": "perde",
              "kabuk_kenari": "düz",
              "kafa_pul_sayisi": "2"
            }
            """
            return self.parser.parse(simulated_response, self.config.model_name)
        except Exception as e:
            raise APIError(f"API call failed: {str(e)}")
