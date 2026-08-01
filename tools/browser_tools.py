"""
tools.browser_tools
-------------------

This module handles opening specific websites using the default system browser.
"""

import webbrowser
from utils.logger import get_logger

logger = get_logger(__name__)

class BrowserTools:
    """Opens websites in the system's default browser."""
    
    SITE_MAP = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://www.github.com",
        "chatgpt": "https://chatgpt.com"
    }

    def open_website(self, target: str) -> str:
        """
        Opens a known website in the browser.
        
        Args:
            target (str): The name of the website.
            
        Returns:
            str: A message indicating success or failure.
        """
        url = self.SITE_MAP.get(target.lower())
        
        if not url:
            return f"Error: Website '{target}' is not in my bookmarks."
            
        try:
            webbrowser.open(url)
            logger.info(f"Opened website: {url}")
            return f"Opened {target} in your browser."
        except Exception as e:
            logger.error(f"Failed to open {target}: {e}")
            return f"Error opening {target}: {str(e)}"
