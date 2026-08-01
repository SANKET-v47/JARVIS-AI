"""
core.intent
-----------

This module detects the user's intent based on parsed tokens. 
Currently uses basic string/rule matching as a foundation before 
introducing AI models.
"""

from typing import List

class IntentDetector:
    """Classifies user intent from a list of tokens."""
    
    def detect(self, tokens: List[str]) -> str:
        """
        Determines the intent from tokens.
        
        Args:
            tokens (List[str]): The normalized input tokens.
            
        Returns:
            str: The detected intent.
        """
        if not tokens:
            return "unknown"
            
        first_token = tokens[0]
        full_command = " ".join(tokens)
        
        # Exit intent
        if first_token in ["exit", "quit", "stop", "bye"]:
            return "exit"
            
        # Greeting intent
        if first_token in ["hello", "hi", "hey", "greetings"]:
            return "greeting"
            
        # System intents
        if first_token == "time":
            return "get_time"
        if first_token == "date":
            return "get_date"
        if "username" in full_command:
            return "get_username"
        if "computer name" in full_command:
            return "get_computer_name"
        if "cwd" in full_command or "current working directory" in full_command:
            return "get_cwd"
        if "python version" in full_command:
            return "get_python_version"
            
        # File intents
        if full_command.startswith("create folder") and len(tokens) > 2:
            return "create_folder"
        if full_command.startswith("create file") and len(tokens) > 2:
            return "create_file"
        if full_command.startswith("list files"):
            return "list_files"
            
        # App / Website intents
        if first_token == "open" and len(tokens) > 1:
            target = " ".join(tokens[1:])
            # Decide if website or app
            if target in ["google", "youtube", "github", "chatgpt"]:
                return "open_website"
            return "open_app"
            
        if first_token == "close" and len(tokens) > 1:
            return "close_app"
            
        return "unknown"
