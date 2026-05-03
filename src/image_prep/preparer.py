import base64
import io
from datetime import datetime
from PIL import Image, UnidentifiedImageError
from src.config import IMAGE_PREP_CONFIG
from src.models import PreparedImage
from src.image_prep.interfaces import IImagePreparer
from src.image_prep.exceptions import InvalidImageError, CompressionError
from src.image_prep.logger import log_image_prep

class ImagePreparer(IImagePreparer):
    """
    Concrete implementation of image preparation service.
    Follows SOLID Principle: Single Responsibility (only prepares images).
    """

    def prepare_image(self, image_bytes: bytes, filename: str) -> PreparedImage:
        """
        Executes the image preparation pipeline.
        """
        try:
            original_file_size = len(image_bytes)
            image = Image.open(io.BytesIO(image_bytes))
            original_size = image.size
            
            # 1. Resize while maintaining aspect ratio
            processed_image = self._resize_to_limits(image)
            
            # 2. Compress to target file size
            compressed_data = self._compress_to_limit(processed_image)
            
            # 3. Create result package
            result = PreparedImage(
                base64_data=base64.b64encode(compressed_data).decode('utf-8'),
                original_filename=filename,
                original_size=original_size,
                processed_size=processed_image.size,
                format=IMAGE_PREP_CONFIG.IMAGE_FORMAT.lower(),
                file_size_bytes=len(compressed_data),
                prep_timestamp=datetime.now().isoformat()
            )
            
            # 4. Log the success
            log_image_prep(
                filename=filename,
                original_size=original_size,
                processed_size=processed_image.size,
                original_file_size=original_file_size,
                processed_file_size=len(compressed_data)
            )
            
            return result

        except UnidentifiedImageError as e:
            log_image_prep(filename, (0,0), (0,0), 0, 0, str(e))
            raise InvalidImageError(f"File {filename} is not a valid image.") from e
        except Exception as e:
            log_image_prep(filename, (0,0), (0,0), 0, 0, str(e))
            raise

    def _resize_to_limits(self, image: Image.Image) -> Image.Image:
        """
        Resizes the image to remain within configured dimensions.
        Clean Code: Small, focused function.
        """
        max_dims = (IMAGE_PREP_CONFIG.MAX_WIDTH, IMAGE_PREP_CONFIG.MAX_HEIGHT)
        # thumbnail() preserves aspect ratio
        image_copy = image.copy()
        image_copy.thumbnail(max_dims, Image.Resampling.LANCZOS)
        return image_copy

    def _compress_to_limit(self, image: Image.Image) -> bytes:
        """
        Iteratively compresses the image until it falls under the size limit.
        Clean Code: Clear logic, uses config values.
        """
        max_bytes = IMAGE_PREP_CONFIG.MAX_FILE_SIZE_MB * 1024 * 1024
        quality = IMAGE_PREP_CONFIG.QUALITY
        img_format = IMAGE_PREP_CONFIG.IMAGE_FORMAT
        
        # Ensure RGB for JPEG conversion
        if image.mode in ("RGBA", "P") and img_format.upper() == "JPEG":
            image = image.convert("RGB")

        while quality >= 10:
            buffer = io.BytesIO()
            image.save(buffer, format=img_format, quality=quality)
            if buffer.tell() <= max_bytes:
                return buffer.getvalue()
            quality -= 5 # More granular reduction
            
        raise CompressionError("Could not compress image below target size even at minimum quality.")
