"""
utils.logger
------------

This module provides a centralized logging configuration. It exists to ensure 
consistent, structured logging across all modules in the JARVIS architecture, 
making debugging and monitoring easier.
"""

import logging
from core.constants import DEFAULT_LOG_LEVEL

def get_logger(name: str) -> logging.Logger:
    """
    Creates and returns a configured logger instance for the given module name.
    
    Args:
        name (str): The name of the module requesting the logger.
        
    Returns:
        logging.Logger: A configured logger object.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        logger.setLevel(DEFAULT_LOG_LEVEL)
        
        # Console handler
        ch = logging.StreamHandler()
        ch.setLevel(DEFAULT_LOG_LEVEL)
        
        # Formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        
        logger.addHandler(ch)
        
    return logger
