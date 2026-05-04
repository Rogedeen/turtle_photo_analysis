import os
from dataclasses import dataclass
from dotenv import load_dotenv

# .env dosyalarını hiyerarşik olarak yükle (.env veya key.env)
load_dotenv(".env")
load_dotenv("key.env")

@dataclass
class GeminiConfig:
    # Her zaman en güncel ortam değişkeninden oku
    @property
    def api_key(self) -> str:
        return os.getenv("GEMINI_API_KEY", "mock_key")
        
    @property
    def model_name(self) -> str:
        # Kota dostu olması için varsayılanı 1.5-flash yapalım
        return os.getenv("MODEL_NAME", "gemini-1.5-flash")
        
    max_output_tokens: int = 2000
    temperature: float = 0.1
