import os
from dataclasses import dataclass

@dataclass
class GeminiConfig:
    api_key: str = os.getenv("GEMINI_API_KEY", "mock_key")
    model_name: str = "gemini-1.5-flash"
    max_output_tokens: int = 1000
    temperature: float = 0.0
