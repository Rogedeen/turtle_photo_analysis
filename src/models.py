from dataclasses import dataclass
from typing import Optional

@dataclass(frozen=True)
class PreparedImage:
    """
    Prepared image data in Base64 format with metadata.
    """
    base64_data: str
    format: str
    width: int
    height: int
    file_size_bytes: int
    original_filename: Optional[str] = None
