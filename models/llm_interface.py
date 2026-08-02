"""
models.llm_interface
--------------------

Primary public interface for JARVIS to interact with the active AI model.
"""

from typing import Generator
from utils.logger import get_logger
from models.providers.provider_registry import ProviderRegistry

logger = get_logger(__name__)

class LLMInterface:
    """Facade for the language model system."""
    
    def __init__(self):
        """Initializes the LLM interface and loads the registry."""
        self.registry = ProviderRegistry()

    def ask(self, prompt: str) -> str:
        """
        Sends a prompt to the active provider and returns the full response.
        
        Args:
            prompt (str): The input text prompt.
            
        Returns:
            str: The fully generated response from the active provider.
        """
        provider = self.registry.get_active_provider()
        return provider.generate(prompt)

    def stream(self, prompt: str) -> Generator[str, None, None]:
        """
        Sends a prompt to the active provider and streams the response back.
        
        Args:
            prompt (str): The input text prompt.
            
        Yields:
            str: Chunks of the generated response.
        """
        provider = self.registry.get_active_provider()
        yield from provider.stream(prompt)
