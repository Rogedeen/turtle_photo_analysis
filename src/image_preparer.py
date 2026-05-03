import base64
import io
import os
from PIL import Image
from src.config import IMAGE_PREP_CONFIG
from src.models import PreparedImage

class ImagePreparer:
    """
    Handles image resizing, compression, and conversion to Base64.
    """

    def prepare_image(self, image_bytes: bytes, filename: str = "image.jpg") -> PreparedImage:
        """
        Main method to process image bytes into PreparedImage dataclass.
        """
        image = Image.open(io.BytesIO(image_bytes))
        
        # 1. Resize if necessary
        image = self._resize_image(image)
        
        # 2. Compress and convert to Base64
        processed_bytes = self._compress_image(image)
        base64_str = base64.b64encode(processed_bytes).decode('utf-8')
        
        return PreparedImage(
            base64_data=base64_str,
            format=IMAGE_PREP_CONFIG.IMAGE_FORMAT,
            width=image.width,
            height=image.height,
            file_size_bytes=len(processed_bytes),
            original_filename=filename
        )

    def _resize_image(self, image: Image.Image) -> Image.Image:
        """
        Resizes image to stay within MAX_WIDTH and MAX_HEIGHT while maintaining aspect ratio.
        """
        max_size = (IMAGE_PREP_CONFIG.MAX_WIDTH, IMAGE_PREP_CONFIG.MAX_HEIGHT)
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
        return image

    def _compress_image(self, image: Image.Image) -> bytes:
        """
        Compresses image into JPEG format until it's under MAX_FILE_SIZE_MB.
        """
        quality = IMAGE_PREP_CONFIG.QUALITY
        max_size_bytes = IMAGE_PREP_CONFIG.MAX_FILE_SIZE_MB * 1024 * 1024
        
        output = io.BytesIO()
        image = image.convert("RGB") # Ensure RGB for JPEG
        image.save(output, format=IMAGE_PREP_CONFIG.IMAGE_FORMAT, quality=quality)
        
        # Iterative compression if still too large
        while output.tell() > max_size_bytes and quality > 10:
            quality -= 10
            output = io.BytesIO()
            image.save(output, format=IMAGE_PREP_CONFIG.IMAGE_FORMAT, quality=quality)
            
        return output.getvalue()
