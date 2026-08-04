import json
import logging
from pathlib import Path
from typing import Union

logger = logging.getLogger(__name__)

class LongTermMemory:
    """
    Handles long-term persistence of memory in a JSON file.
    """
    
    def __init__(self, file_path: Union[str, Path] = None):
        """
        Initialize LongTermMemory.
        
        Args:
            file_path: The path to the memory JSON file. 
                       Defaults to memory.json in the same directory as this file.
        """
        if file_path is None:
            # Default to memory/memory.json
            self.file_path = Path(__file__).parent / "memory.json"
        else:
            self.file_path = Path(file_path)
            
        self._initialize_file()

    def _initialize_file(self) -> None:
        """
        Check whether the memory file exists, and create it with an empty 
        JSON array if it doesn't.
        """
        if not self.file_path.exists():
            try:
                self.file_path.parent.mkdir(parents=True, exist_ok=True)
                with open(self.file_path, "w", encoding="utf-8") as f:
                    json.dump([], f)
                logger.info(f"Initialized new long-term memory file at {self.file_path}")
            except Exception as e:
                logger.error(f"Error initializing long-term memory file: {e}")
                raise

    def save_fact(self, key: str, value: str) -> None:
        """
        Saves or updates a user fact in long-term memory.
        
        Args:
            key (str): The fact key (e.g., 'name', 'learning').
            value (str): The fact value.
        """
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                memory_data = json.load(f)
                
            updated = False
            for item in memory_data:
                if item.get("type") == "fact" and item.get("key") == key:
                    item["value"] = value
                    updated = True
                    break
                    
            if updated:
                logger.info(f"Updated fact:\n{key} = {value}")
            else:
                memory_data.append({"type": "fact", "key": key, "value": value})
                logger.info(f"Saved fact:\n{key} = {value}")
                
            with open(self.file_path, "w", encoding="utf-8") as f:
                json.dump(memory_data, f, indent=4)
                
        except Exception as e:
            logger.error(f"Error saving fact to long-term memory: {e}")
