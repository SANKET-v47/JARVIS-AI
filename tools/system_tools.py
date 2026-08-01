"""
tools.system_tools
------------------

This module provides access to basic system information like 
time, date, username, and system properties.
"""

import os
import sys
import getpass
import platform
from datetime import datetime

class SystemTools:
    """Provides system information."""

    def get_time(self) -> str:
        """Returns the current local time."""
        now = datetime.now()
        return f"The current time is {now.strftime('%I:%M %p')}"

    def get_date(self) -> str:
        """Returns the current local date."""
        now = datetime.now()
        return f"Today's date is {now.strftime('%B %d, %Y')}"

    def get_computer_name(self) -> str:
        """Returns the network name of the computer."""
        return f"Your computer name is {platform.node()}"

    def get_username(self) -> str:
        """Returns the current logged-in username."""
        return f"You are logged in as {getpass.getuser()}"

    def get_cwd(self) -> str:
        """Returns the current working directory."""
        return f"The current working directory is {os.getcwd()}"

    def get_python_version(self) -> str:
        """Returns the Python version running JARVIS."""
        return f"JARVIS is running on Python {sys.version.split(' ')[0]}"
