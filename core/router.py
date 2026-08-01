"""
core.router
-----------

This module translates intent and tokens into an actionable payload
and calls the ToolManager to execute it.
"""

from typing import List, Dict, Any
from tools.tool_manager import ToolManager

class ActionRouter:
    """Routes an intent and tokens to the ToolManager."""
    
    def __init__(self):
        self.tool_manager = ToolManager()
    
    def route(self, intent: str, tokens: List[str]) -> str:
        """
        Generates an action object based on the intent and executes it.
        
        Args:
            intent (str): The detected intent.
            tokens (List[str]): The parsed tokens.
            
        Returns:
            str: The result of the execution.
        """
        action = {"intent": intent}
        
        if intent in ["open_app", "open_website", "close_app"]:
            target = " ".join(tokens[1:])
            action["target"] = target
            
        elif intent in ["create_folder", "create_file"]:
            target = " ".join(tokens[2:])
            action["target"] = target
            
        elif intent == "list_files":
            target = " ".join(tokens[2:]) if len(tokens) > 2 else ""
            action["target"] = target
            
        # Call the ToolManager to execute
        return self.tool_manager.execute(action)
