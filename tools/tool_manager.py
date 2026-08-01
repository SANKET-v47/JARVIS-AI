"""
tools.tool_manager
------------------

This module is the central orchestrator for execution. It takes an action 
payload, routes it to the appropriate specific tool, and returns the result.
"""

from typing import Dict, Any
from utils.logger import get_logger

# Import specific tools
from tools.app_launcher import AppLauncher
from tools.browser_tools import BrowserTools
from tools.system_tools import SystemTools
from tools.file_tools import FileTools

logger = get_logger(__name__)

class ToolManager:
    """Routes and executes intents using the correct tool subsystem."""
    
    def __init__(self):
        """Initialize all tool subsystems."""
        self.app_launcher = AppLauncher()
        self.browser_tools = BrowserTools()
        self.system_tools = SystemTools()
        self.file_tools = FileTools()

    def execute(self, action: Dict[str, Any]) -> str:
        """
        Executes the action described by the action payload.
        
        Args:
            action (Dict[str, Any]): The action payload containing 'intent' and optional 'target'.
            
        Returns:
            str: The text output or result of the execution to display to the user.
        """
        intent = action.get("intent")
        target = action.get("target", "")
        
        if not intent:
            return "Error: No intent provided to ToolManager."
            
        logger.info(f"Executing intent: {intent} with target: {target}")
        
        try:
            # Browser and App Launcher
            if intent == "open_app":
                return self.app_launcher.launch(target)
            elif intent == "open_website":
                return self.browser_tools.open_website(target)
                
            # System Tools
            elif intent == "get_time":
                return self.system_tools.get_time()
            elif intent == "get_date":
                return self.system_tools.get_date()
            elif intent == "get_computer_name":
                return self.system_tools.get_computer_name()
            elif intent == "get_username":
                return self.system_tools.get_username()
            elif intent == "get_cwd":
                return self.system_tools.get_cwd()
            elif intent == "get_python_version":
                return self.system_tools.get_python_version()
                
            # File Tools
            elif intent == "create_folder":
                return self.file_tools.create_folder(target)
            elif intent == "create_file":
                return self.file_tools.create_file(target)
            elif intent == "list_files":
                # If no target specified, use current dir
                target_dir = target if target else "."
                return self.file_tools.list_files(target_dir)
                
            # Standard intents not executed by tools
            elif intent in ["exit", "greeting", "unknown"]:
                # The router or main loop usually handles these, but if they get here:
                if intent == "greeting":
                    return "Hello! I am JARVIS. How can I help you today?"
                elif intent == "unknown":
                    return "I'm sorry, I didn't understand that command."
                
            return f"Intent '{intent}' is not supported by the ToolManager yet."
            
        except Exception as e:
            logger.error(f"Execution error for intent {intent}: {e}")
            return f"An unexpected error occurred during execution: {str(e)}"
