from abc import ABC, abstractmethod
from src.models import PreparedImage

class IImagePreparer(ABC):
    """
    Interface for image preparation services.
    Adheres to SOLID Principles: Interface Segregation & Dependency Inversion.
    """
    
    @abstractmethod
    def prepare_image(self, image_bytes: bytes, filename: str) -> PreparedImage:
        """
        Process raw image bytes and return a standardized PreparedImage object.
        
        Args:
            image_bytes: Raw binary data of the image.
            filename: Original name of the file for tracking.
            
        Returns:
            PreparedImage: Processed image metadata and base64 string.
            
        Raises:
            InvalidImageError: If source data is not a recognizable image.
            CompressionError: If size constraints cannot be met.
        """
        pass
