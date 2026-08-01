"""
core.version
------------

This module manages the application's versioning. It exists to centralize 
version information, ensuring that version strings are consistent for logging, 
API responses, and user interfaces.
"""

__version__ = "0.1.0"

def get_version() -> str:
    """Returns the current application version."""
    return __version__
