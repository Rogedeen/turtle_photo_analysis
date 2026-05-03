import unittest
import io
import base64
from PIL import Image
from src.image_preparer import ImagePreparer
from src.config import IMAGE_PREP_CONFIG

class TestImagePreparer(unittest.TestCase):
    def setUp(self):
        self.preparer = ImagePreparer()

    def _create_test_image_bytes(self, width: int, height: int) -> bytes:
        img = Image.new('RGB', (width, height), color='red')
        buf = io.BytesIO()
        img.save(buf, format='JPEG')
        return buf.getvalue()

    def test_resize_large_image(self):
        large_width, large_height = 2000, 1500
        image_bytes = self._create_test_image_bytes(large_width, large_height)
        
        prepared = self.preparer.prepare_image(image_bytes)
        
        self.assertLessEqual(prepared.width, IMAGE_PREP_CONFIG.MAX_WIDTH)
        self.assertLessEqual(prepared.height, IMAGE_PREP_CONFIG.MAX_HEIGHT)
        # Aspect ratio check (approximate due to rounding)
        original_ratio = large_width / large_height
        prepared_ratio = prepared.width / prepared.height
        self.assertAlmostEqual(original_ratio, prepared_ratio, places=1)

    def test_file_size_constraint(self):
        # Create a very large uncompressed-like image by filling with noise
        import numpy as np
        noise = np.random.randint(0, 255, (2000, 2000, 3), dtype=np.uint8)
        img = Image.fromarray(noise)
        buf = io.BytesIO()
        img.save(buf, format='JPEG', quality=100)
        image_bytes = buf.getvalue()

        prepared = self.preparer.prepare_image(image_bytes)
        
        max_bytes = IMAGE_PREP_CONFIG.MAX_FILE_SIZE_MB * 1024 * 1024
        self.assertLessEqual(prepared.file_size_bytes, max_bytes)

    def test_base64_encoding_valid(self):
        image_bytes = self._create_test_image_bytes(100, 100)
        prepared = self.preparer.prepare_image(image_bytes)
        
        # Try to decode back
        decoded_bytes = base64.b64decode(prepared.base64_data)
        self.assertTrue(len(decoded_bytes) > 0)
        
        # Verify it's a valid image
        img = Image.open(io.BytesIO(decoded_bytes))
        self.assertEqual(img.width, prepared.width)

    def test_small_image_stays_small(self):
        small_width, small_height = 100, 100
        image_bytes = self._create_test_image_bytes(small_width, small_height)
        
        prepared = self.preparer.prepare_image(image_bytes)
        
        self.assertEqual(prepared.width, small_width)
        self.assertEqual(prepared.height, small_height)

if __name__ == '__main__':
    unittest.main()
