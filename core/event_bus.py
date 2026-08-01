"""
core.event_bus
--------------

This module implements a Publish/Subscribe pattern, allowing disparate 
components of the system to communicate without tight coupling.
"""

from typing import Callable, Dict, List, Any
from utils.logger import get_logger

logger = get_logger(__name__)

class EventBus:
    """Manages event subscriptions and publishing."""

    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_name: str, callback: Callable) -> None:
        """
        Subscribes a callback to an event.
        
        Args:
            event_name (str): The name of the event to listen for.
            callback (Callable): The function to call when the event occurs.
        """
        if event_name not in self._subscribers:
            self._subscribers[event_name] = []
        self._subscribers[event_name].append(callback)
        logger.debug(f"Subscribed to event: {event_name}")

    def unsubscribe(self, event_name: str, callback: Callable) -> None:
        """
        Unsubscribes a callback from an event.
        
        Args:
            event_name (str): The name of the event.
            callback (Callable): The function to remove.
        """
        if event_name in self._subscribers:
            try:
                self._subscribers[event_name].remove(callback)
                logger.debug(f"Unsubscribed from event: {event_name}")
            except ValueError:
                pass

    def publish(self, event_name: str, data: Any = None) -> None:
        """
        Publishes an event to all subscribed callbacks.
        
        Args:
            event_name (str): The name of the event.
            data (Any): The payload to send to subscribers.
        """
        if event_name in self._subscribers:
            logger.debug(f"Publishing event: {event_name}")
            for callback in self._subscribers[event_name]:
                try:
                    callback(data)
                except Exception as e:
                    logger.error(f"Error in event callback for '{event_name}': {e}")
