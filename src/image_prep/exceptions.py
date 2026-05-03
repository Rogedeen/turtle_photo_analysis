class ImagePrepError(Exception):
    """Base class for image preparation errors."""
    pass

class InvalidImageError(ImagePrepError):
    """Raised when the input file is not a valid image or cannot be opened."""
    pass

class ImageTooSmallError(ImagePrepError):
    """Raised when the image dimensions are below a minimum threshold."""
    pass

class CompressionError(ImagePrepError):
    """Raised when the image cannot be compressed below the target size."""
    pass
