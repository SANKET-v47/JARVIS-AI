"""
memory.session_memory
---------------------

This module provides the SessionMemory class, which stores the conversational
history between the user and the assistant.
"""

from typing import List, Dict

class SessionMemory:
    """Stores and manages the conversational history for a session."""

    def __init__(self):
        """Initializes an empty session memory."""
        self._history: List[Dict[str, str]] = []

    def add_user_message(self, message: str) -> None:
        """
        Adds a user message to the session history.

        Args:
            message (str): The message from the user.
        """
        self._history.append({"role": "user", "content": message})

    def add_assistant_message(self, message: str) -> None:
        """
        Adds an assistant message to the session history.

        Args:
            message (str): The message from the assistant.
        """
        self._history.append({"role": "assistant", "content": message})

    def get_history(self) -> List[Dict[str, str]]:
        """
        Retrieves the complete session history.

        Returns:
            List[Dict[str, str]]: The list of conversation turns.
        """
        return self._history.copy()

    def clear(self) -> None:
        """Clears the session history."""
        self._history.clear()
