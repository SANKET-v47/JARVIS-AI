"""
models.providers.provider_registry
----------------------------------

Manages the registration and selection of LLM providers.
"""

from typing import Dict, Optional
from utils.logger import get_logger
from models.providers.base_provider import BaseProvider
from models.providers.dummy_provider import DummyProvider

logger = get_logger(__name__)

class ProviderRegistry:
    """Registry pattern to manage different AI providers."""
    
    def __init__(self):
        self._providers: Dict[str, BaseProvider] = {}
        self._active_provider_name: Optional[str] = None
        
        # Register and set default provider on initialization
        self.register_provider("dummy", DummyProvider())
        self.set_active_provider("dummy")

    def register_provider(self, name: str, provider: BaseProvider) -> None:
        """
        Registers a new provider under the given name.
        
        Args:
            name (str): Unique name for the provider (e.g., 'openai').
            provider (BaseProvider): The provider instance to register.
        """
        self._providers[name] = provider
        logger.info(f"Registered LLM provider: '{name}'")

    def get_provider(self, name: str) -> Optional[BaseProvider]:
        """
        Retrieves a provider by name.
        
        Args:
            name (str): The name of the registered provider.
            
        Returns:
            Optional[BaseProvider]: The provider instance or None if not found.
        """
        return self._providers.get(name)

    def set_active_provider(self, name: str) -> None:
        """
        Sets the active provider for the system to use.
        
        Args:
            name (str): The name of the registered provider to activate.
            
        Raises:
            ValueError: If the provider name is not registered.
        """
        if name not in self._providers:
            raise ValueError(f"Provider '{name}' is not registered.")
            
        self._active_provider_name = name
        logger.info(f"Active LLM provider set to: '{name}'")

    def get_active_provider(self) -> BaseProvider:
        """
        Returns the currently active provider instance.
        
        Returns:
            BaseProvider: The active provider instance.
            
        Raises:
            RuntimeError: If no active provider is set.
        """
        if not self._active_provider_name:
            raise RuntimeError("No active provider is set.")
            
        return self._providers[self._active_provider_name]
