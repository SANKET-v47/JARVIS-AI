"""
models.providers.base_provider
------------------------------

Defines the abstract base class for all LLM providers.
"""

from abc import ABC, abstractmethod
from typing import Generator

class BaseProvider(ABC):
    """
    Abstract Base Class for LLM Providers.
    All future providers (e.g., OpenAI, Gemini) must implement these methods.
    """

    @abstractmethod
    def generate(self, prompt: str) -> str:
        """
        Generates a full text response for a given prompt.
        
        Args:
            prompt (str): The input text to send to the LLM.
            
        Returns:
            str: The fully generated response.
        """
        pass

    @abstractmethod
    def stream(self, prompt: str) -> Generator[str, None, None]:
        """
        Streams a text response piece by piece.
        
        Args:
            prompt (str): The input text to send to the LLM.
            
        Yields:
            str: Incremental chunks of the generated response.
        """
        pass

    @abstractmethod
    def health_check(self) -> bool:
        """
        Checks if the provider is currently available and correctly configured.
        
        Returns:
            bool: True if healthy, False otherwise.
        """
        pass
