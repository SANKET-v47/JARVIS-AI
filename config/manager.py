"""
config.manager
--------------

This module implements the ConfigManager. It exists to centralize the loading 
and validation of environment variables and configuration settings, ensuring 
that other modules interact with a safe, typed configuration object.
"""

import os
from typing import Optional
from utils.logger import get_logger

logger = get_logger(__name__)

class ConfigManager:
    """
    Manages application configuration, reading from environment variables
    or default values.
    """
    
    def __init__(self):
        """Initialize the ConfigManager and load settings."""
        logger.info("Initializing ConfigManager...")
        self.debug_mode = os.getenv("DEBUG_MODE", "false").lower() == "true"
        self.api_key = os.getenv("API_KEY", None)

    def get_api_key(self) -> Optional[str]:
        """
        Retrieves the configured API key.
        
        Returns:
            Optional[str]: The API key or None if not set.
        """
        return self.api_key
        
    def is_debug(self) -> bool:
        """
        Checks if the application is in debug mode.
        
        Returns:
            bool: True if debug mode is active.
        """
        return self.debug_mode
