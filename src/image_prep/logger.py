from datetime import datetime
from src.models import PreparedImage

# This file fulfills the reporting requirements from Image.agent.md

def log_image_prep(
    filename: str, 
    original_size: tuple[int, int], 
    processed_size: tuple[int, int], 
    original_file_size: int,
    processed_file_size: int,
    error: str = None
) -> None:
    """
    Logs the image preparation process into reports/image-prep-log.md.
    """
    log_path = "reports/image-prep-log.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    compression_ratio = (1 - (processed_file_size / original_file_size)) * 100 if original_file_size > 0 else 0
    
    log_entry = f"""
## [{timestamp}] Execution Log
**File:** {filename}
**Original Dimensions:** {original_size[0]}x{original_size[1]} ({original_file_size / 1024:.2f} KB)
**Processed Dimensions:** {processed_size[0]}x{processed_size[1]} ({processed_file_size / 1024:.2f} KB)
**Compression Ratio:** %{compression_ratio:.2f}
**Status:** {"SUCCESS" if not error else "FAILED"}
**Error (if any):** {error if error else "None"}
**Clean Code Rules Applied:**
- SOLID: Single Responsibility (Logging isolated)
- Clean Code: Meaningful names, type hints, docstrings
---
"""
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_entry)

import os
