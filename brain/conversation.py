"""
brain.conversation
------------------

This module provides the ConversationManager, responsible for 
generating conversational responses without using external AI APIs.
"""

from typing import Dict
from models.llm_interface import LLMInterface
from memory.session_memory import SessionMemory

class ConversationManager:
    """Handles basic conversational inputs and generates appropriate responses."""
    
    def __init__(self):
        """Initializes the conversation manager and its response map."""
        # Centralized map for easy extension
        self.response_map: Dict[str, str] = {
            "hello": "Hello! How can I assist you today?",
            "hi": "Hi there! What can I do for you?",
            "good morning": "Good morning! I hope you're having a great day.",
            "who are you": "I am JARVIS, your local AI assistant.",
            "how are you": "I'm functioning perfectly, thank you for asking!",
            "thank you": "You're very welcome!",
            "bye": "Goodbye! Have a great day."
        }
        self.llm = LLMInterface()
        self.memory = SessionMemory()
        
    def generate_response(self, text: str) -> str:
        """
        Generates a response for the given input text.
        
        Args:
            text (str): The raw text input from the user.
            
        Returns:
            str: The generated response, or a fallback message if unknown.
        """
        self.memory.add_user_message(text)
        
        normalized_text = text.lower().strip()
        response_text = None
        
        # Check if the exact normalized phrase is in our map
        if normalized_text in self.response_map:
            response_text = self.response_map[normalized_text]
            
        # Optional: check if the text contains any of the mapped phrases
        # This handles cases like "hi jarvis" or "who are you?"
        if response_text is None:
            for phrase, response in self.response_map.items():
                if phrase in normalized_text:
                    response_text = response
                    break
                    
        # Default fallback for unknown inputs, routes to LLM interface
        if response_text is None:
            history = self.memory.get_history()
            prompt_lines = []
            for msg in history:
                role = "JARVIS" if msg["role"] == "assistant" else "User"
                prompt_lines.append(f"{role}: {msg['content']}")
            prompt_lines.append("JARVIS:")
            prompt = "\n".join(prompt_lines)
            
            response_text = self.llm.ask(prompt)
            
        self.memory.add_assistant_message(response_text)
        return response_text
