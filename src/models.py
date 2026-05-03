from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class PreparedImage:
    """
    Prepared image data in Base64 format with metadata.
    """
    base64_data: str
    original_filename: str
    original_size: tuple[int, int]
    processed_size: tuple[int, int]
    format: str  # "jpeg" | "png"
    file_size_bytes: int
    prep_timestamp: str
