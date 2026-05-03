class FeatureExtractionError(Exception):
    """Base exception for feature extraction errors."""
    pass

class APIError(FeatureExtractionError):
    """Raised when the Vision AI API returns an error or fails to respond."""
    pass

class ParserError(FeatureExtractionError):
    """Raised when the API response cannot be parsed into the expected format."""
    pass
