"""
core.service_registry
---------------------

This module provides a centralized dependency injection container 
to register and retrieve services globally.
"""

from typing import Dict, Any
from utils.logger import get_logger
from core.exceptions import ServiceNotFound

logger = get_logger(__name__)

class ServiceRegistry:
    """Central registry for application services."""

    def __init__(self):
        self._services: Dict[str, Any] = {}

    def register(self, name: str, service: Any) -> None:
        """
        Registers a service.
        
        Args:
            name (str): The unique name of the service.
            service (Any): The service instance.
        """
        self._services[name] = service
        logger.info(f"Registered service: {name}")

    def get(self, name: str) -> Any:
        """
        Retrieves a registered service.
        
        Args:
            name (str): The name of the service.
            
        Returns:
            Any: The service instance.
            
        Raises:
            ServiceNotFound: If the service has not been registered.
        """
        if name not in self._services:
            raise ServiceNotFound(f"Service '{name}' not found in registry.")
        return self._services[name]

    def exists(self, name: str) -> bool:
        """Checks if a service is registered."""
        return name in self._services

    def remove(self, name: str) -> None:
        """Removes a service from the registry."""
        if name in self._services:
            del self._services[name]
            logger.info(f"Removed service: {name}")
