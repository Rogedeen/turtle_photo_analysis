from dataclasses import dataclass

@dataclass(frozen=True)
class ImageConfig:
    MAX_WIDTH: int = 1024
    MAX_HEIGHT: int = 1024
    MAX_FILE_SIZE_MB: float = 1.0
    QUALITY: int = 85
    IMAGE_FORMAT: str = "JPEG"

IMAGE_PREP_CONFIG = ImageConfig()
