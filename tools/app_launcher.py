"""
tools.app_launcher
------------------

This module handles launching basic system applications securely 
using the subprocess module.
"""

import subprocess
from utils.logger import get_logger

logger = get_logger(__name__)

class AppLauncher:
    """Launches local system applications."""
    
    # Mapping of common names to Windows executables
    APP_MAP = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
        "command prompt": "cmd.exe",
        "cmd": "cmd.exe",
        "file explorer": "explorer.exe",
        "explorer": "explorer.exe"
    }

    def launch(self, target: str) -> str:
        """
        Launches the target application.
        
        Args:
            target (str): The name of the application to launch.
            
        Returns:
            str: A message indicating success or failure.
        """
        app_exe = self.APP_MAP.get(target.lower())
        
        if not app_exe:
            return f"Error: App '{target}' is not supported."
            
        try:
            # We use subprocess.Popen to avoid blocking the main thread
            subprocess.Popen([app_exe])
            logger.info(f"Launched application: {app_exe}")
            return f"Successfully opened {target}."
        except Exception as e:
            logger.error(f"Failed to launch {target}: {e}")
            return f"Error opening {target}: {str(e)}"
