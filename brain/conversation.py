"""
brain.conversation
------------------

This module provides the ConversationManager, responsible for 
generating conversational responses without using external AI APIs.
"""

from typing import Dict, Optional
import re
from models.llm_interface import LLMInterface
from memory.session_memory import SessionMemory
from memory.long_term_memory import LongTermMemory

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
        self.long_term_memory = LongTermMemory()
        
    def generate_response(self, text: str) -> str:
        """
        Generates a response for the given input text.
        
        Args:
            text (str): The raw text input from the user.
            
        Returns:
            str: The generated response, or a fallback message if unknown.
        """
        self.memory.add_user_message(text)
        
        self._detect_and_save_facts(text)
        
        normalized_text = text.lower().strip()
        
        import string
        normalized_text_no_punct = normalized_text.rstrip(string.punctuation)
        response_text = self._handle_fact_retrieval(normalized_text_no_punct)
        
        # Check if the exact normalized phrase is in our map
        if response_text is None and normalized_text in self.response_map:
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

    def _detect_and_save_facts(self, text: str) -> None:
        """Detects simple user facts using pattern matching and saves them."""
        patterns = [
            (r"(?i)my name is\s+(.+)", "name"),
            (r"(?i)i am learning\s+(.+)", "learning"),
            (r"(?i)my favorite color is\s+(.+)", "favorite_color")
        ]
        
        import string
        for pattern, key in patterns:
            match = re.search(pattern, text)
            if match:
                value = match.group(1).strip()
                value = value.rstrip(string.punctuation)
                if value:
                    self.long_term_memory.save_fact(key, value)

    def _handle_fact_retrieval(self, normalized_text: str) -> Optional[str]:
        """Checks if the user is asking for a fact and returns the appropriate response."""
        questions = {
            "what is my name": ("name", "Your name is {value}."),
            "what am i learning": ("learning", "You are learning {value}."),
            "what is my favorite color": ("favorite_color", "Your favorite color is {value}.")
        }
        
        if normalized_text in questions:
            key, template = questions[normalized_text]
            fact_value = self.long_term_memory.get_fact(key)
            if fact_value:
                return template.format(value=fact_value)
            else:
                return "I don't know that yet."
                
        return None

