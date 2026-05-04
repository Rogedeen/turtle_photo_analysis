import base64
import os
import json
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

from src.models import PreparedImage
from src.feature_extraction.interfaces import IFeatureExtractor
from src.feature_extraction.models import TurtleFeatures
from src.feature_extraction.config import GeminiConfig
from src.feature_extraction.prompt_builder import PromptBuilder
from src.feature_extraction.response_parser import ResponseParser
from src.feature_extraction.exceptions import APIError

# Çevre değişkenlerini yükle (.env veya key.env fark etmez)
load_dotenv("key.env")
load_dotenv(".env")

class GeminiFeatureExtractor(IFeatureExtractor):
    def __init__(self, config: GeminiConfig = None):
        self.config = config or GeminiConfig()
        self.prompt_builder = PromptBuilder()
        self.parser = ResponseParser()
        
    def _configure_api(self):
        """API'yi her taze girişte yapılandırır."""
        api_key = self.config.api_key
        if not api_key or api_key == "mock_key":
             raise APIError("Geçerli bir GEMINI_API_KEY bulunamadı. Lütfen key.env veya .env dosyanızı kontrol edin.")
        genai.configure(api_key=api_key)

    async def extract_features(self, image: PreparedImage) -> TurtleFeatures:
        # Her istekte API anahtarını tazeleyici yapılandırma (Key değişimi için)
        self._configure_api()
        
        prompt_text = self.prompt_builder.build_prompt()
        
        try:
            # Model çağrısı (Kullanıcı girdisine göre flash model kontrolü vb. de yapılabilir)
            model = genai.GenerativeModel(self.config.model_name)
            
            # Gerçek çağrı (Image b64 encoding kullanılarak)
            response = await model.generate_content_async([
                prompt_text,
                {"mime_type": "image/jpeg", "data": image.base64_data}
            ])
            
            # Gelen yanıtı al (Markdown json tag'leri gelmişse temizle)
            response_text = response.text.replace("```json", "").replace("```", "").strip()
            
            return self.parser.parse(response_text, self.config.model_name)
        except Exception as e:
            raise APIError(f"API call failed: {str(e)}")
