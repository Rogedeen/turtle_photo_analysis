import pytest
import io
import base64
from PIL import Image
from src.image_prep.preparer import ImagePreparer
from src.image_prep.exceptions import InvalidImageError, CompressionError
from src.config import IMAGE_PREP_CONFIG

def create_test_image(size=(2000, 2000), mode='RGB', fmt='JPEG'):
    img = Image.new(mode, size, color='red')
    buf = io.BytesIO()
    img.save(buf, format=fmt)
    return buf.getvalue()

def test_prepare_image_resizes_correctly():
    preparer = ImagePreparer()
    # 2000x2000 should be resized to 1024x1024 (default config)
    img_bytes = create_test_image(size=(2000, 2000))
    
    result = preparer.prepare_image(img_bytes, "test.jpg")
    
    assert result.processed_size[0] <= IMAGE_PREP_CONFIG.MAX_WIDTH
    assert result.processed_size[1] <= IMAGE_PREP_CONFIG.MAX_HEIGHT
    assert result.original_size == (2000, 2000)

def test_prepare_image_returns_base64():
    preparer = ImagePreparer()
    img_bytes = create_test_image(size=(100, 100))
    
    result = preparer.prepare_image(img_bytes, "small.jpg")
    
    # Should be valid base64
    base64.b64decode(result.base64_data)
    assert len(result.base64_data) > 0

def test_invalid_image_raises_error():
    preparer = ImagePreparer()
    with pytest.raises(InvalidImageError):
        preparer.prepare_image(b"not an image", "fraud.txt")

def test_file_size_limit_respected():
    preparer = ImagePreparer()
    # Create a very large image that needs heavy compression
    # (Though thumbnailing to 1024x1024 usually fits 1MB easily)
    img_bytes = create_test_image(size=(3000, 3000))
    
    result = preparer.prepare_image(img_bytes, "large.jpg")
    
    max_allowed = IMAGE_PREP_CONFIG.MAX_FILE_SIZE_MB * 1024 * 1024
    assert result.file_size_bytes <= max_allowed

def test_alpha_channel_handling():
    preparer = ImagePreparer()
    # JPEG doesn't support RGBA, should be converted
    img_bytes = create_test_image(size=(100, 100), mode='RGBA', fmt='PNG')
    
    result = preparer.prepare_image(img_bytes, "alpha.png")
    
    assert result.format == IMAGE_PREP_CONFIG.IMAGE_FORMAT.lower()
