"""
tools.file_tools
----------------

This module allows JARVIS to safely create files and folders, 
as well as list directory contents. It strictly prohibits file deletion.
"""

import os
from pathlib import Path
from utils.logger import get_logger

logger = get_logger(__name__)

class FileTools:
    """Safely manages files and directories."""

    def create_folder(self, folder_name: str) -> str:
        """Creates a new directory if it doesn't exist."""
        try:
            path = Path(folder_name)
            if path.exists():
                return f"Folder '{folder_name}' already exists."
            
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Created folder: {path.absolute()}")
            return f"Folder '{folder_name}' created successfully."
        except Exception as e:
            logger.error(f"Failed to create folder {folder_name}: {e}")
            return f"Error creating folder: {str(e)}"

    def create_file(self, file_name: str) -> str:
        """Creates an empty file if it doesn't exist."""
        try:
            path = Path(file_name)
            if path.exists():
                return f"File '{file_name}' already exists."
                
            path.touch()
            logger.info(f"Created file: {path.absolute()}")
            return f"File '{file_name}' created successfully."
        except Exception as e:
            logger.error(f"Failed to create file {file_name}: {e}")
            return f"Error creating file: {str(e)}"

    def list_files(self, target_dir: str = ".") -> str:
        """Lists contents of the specified directory."""
        try:
            path = Path(target_dir)
            if not path.exists() or not path.is_dir():
                return f"'{target_dir}' is not a valid directory."
                
            contents = os.listdir(path)
            if not contents:
                return f"The directory '{target_dir}' is empty."
                
            return "Contents:\n- " + "\n- ".join(contents)
        except Exception as e:
            logger.error(f"Failed to list files in {target_dir}: {e}")
            return f"Error listing files: {str(e)}"
