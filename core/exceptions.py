"""
core.exceptions
---------------

This module defines custom exceptions used across the JARVIS architecture.
"""

class JarvisException(Exception):
    """Base exception for all JARVIS errors."""
    pass

class ServiceNotFound(JarvisException):
    """Raised when a requested service is not found in the registry."""
    pass

class InvalidState(JarvisException):
    """Raised when the system is in an invalid state for the requested operation."""
    pass

class ModuleInitializationError(JarvisException):
    """Raised when a module or service fails to initialize properly."""
    pass
