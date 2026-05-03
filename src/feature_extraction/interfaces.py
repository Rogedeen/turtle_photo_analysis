from abc import ABC, abstractmethod
from src.models import PreparedImage
from src.feature_extraction.models import TurtleFeatures

class IFeatureExtractor(ABC):
    @abstractmethod
    async def extract_features(self, image: PreparedImage) -> TurtleFeatures:
        """
        Extract physical features of a turtle from a prepared image.
        """
        pass
