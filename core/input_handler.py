"""
core.input_handler
------------------

This module handles receiving input from the user. It isolates the 
I/O boundary for input, allowing it to be easily swapped out for 
audio input or an API endpoint in the future.
"""

class InputHandler:
    """Handles retrieval of user input."""
    
    def get_input(self, prompt: str = "You: ") -> str:
        """
        Retrieves input from the user.
        
        Args:
            prompt (str): The prompt to display to the user.
            
        Returns:
            str: The raw input string provided by the user.
        """
        try:
            return input(prompt)
        except (KeyboardInterrupt, EOFError):
            return "exit"
