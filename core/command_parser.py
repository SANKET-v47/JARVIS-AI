"""
core.command_parser
-------------------

This module normalizes user input by removing extra whitespace, 
converting to lowercase, and tokenizing the string into discrete words.
"""

from typing import List

class CommandParser:
    """Parses and normalizes raw user input."""
    
    def parse(self, raw_input: str) -> List[str]:
        """
        Normalizes and tokenizes the input string.
        
        Args:
            raw_input (str): The raw string from the user.
            
        Returns:
            List[str]: A list of normalized tokens.
        """
        if not raw_input:
            return []
            
        # Strip leading/trailing spaces and convert to lower case
        normalized = raw_input.strip().lower()
        
        # Tokenize by splitting on spaces (removes multiple spaces automatically)
        tokens = normalized.split()
        return tokens
