"""
core.startup
------------

This module provides the StartupManager. It exists to orchestrate the boot 
sequence of JARVIS, ensuring that the configuration, logger, and other 
foundational subsystems are initialized in the correct order before the main 
logic begins.
"""

from config.manager import ConfigManager
from utils.logger import get_logger
from core.version import get_version

logger = get_logger(__name__)

class StartupManager:
    """
    Handles the initialization and boot sequence for the JARVIS application.
    """
    
    def __init__(self):
        """Initializes the StartupManager."""
        self.config = None

    def boot(self) -> ConfigManager:
        """
        Executes the startup sequence.
        
        Returns:
            ConfigManager: The initialized configuration manager.
        """
        logger.info(f"Starting JARVIS v{get_version()} boot sequence...")
        
        # Load configuration
        self.config = ConfigManager()
        
        # Validate critical dependencies or environment here
        if not self.config.get_api_key():
            logger.warning("API_KEY is not set in the environment. Some features may be unavailable.")
            
        logger.info("Boot sequence completed successfully.")
        return self.config
