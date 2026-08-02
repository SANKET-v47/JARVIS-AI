"""
models.providers.dummy_provider
-------------------------------

A dummy implementation of BaseProvider used for testing and
architecture validation before connecting real AI APIs.
"""

from typing import Generator
from utils.logger import get_logger
from models.providers.base_provider import BaseProvider

logger = get_logger(__name__)

class DummyProvider(BaseProvider):
    """A placeholder provider that returns fixed responses."""
    
    def __init__(self):
        self._fixed_response = "I'm the Dummy Provider. Real AI will be connected later."
        logger.info("DummyProvider initialized.")

    def generate(self, prompt: str) -> str:
        """
        Returns a fixed text response.
        """
        logger.debug(f"DummyProvider generating response for prompt: {prompt}")
        return self._fixed_response

    def stream(self, prompt: str) -> Generator[str, None, None]:
        """
        Streams the fixed text response word by word.
        """
        logger.debug(f"DummyProvider streaming response for prompt: {prompt}")
        words = self._fixed_response.split(" ")
        for i, word in enumerate(words):
            # yield with space if it's not the last word
            yield word + (" " if i < len(words) - 1 else "")

    def health_check(self) -> bool:
        """
        The DummyProvider is always healthy.
        """
        return True
