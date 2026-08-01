"""
config.py
---------

This module acts as a top-level facade for the configuration system. 
It exists to provide a convenient import path (e.g., `import config`) 
for scripts or external tools that need quick access to the ConfigManager.
"""

from config.manager import ConfigManager

# Provide a global instance for simple access if needed
# Typically, dependency injection is preferred in a clean architecture,
# but this facade can be useful for scripts.
global_config = ConfigManager()
