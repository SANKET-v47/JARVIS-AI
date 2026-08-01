"""
core.state
----------

This module provides a centralized, thread-safe global state manager 
for tracking the application's runtime status.
"""

import threading
from typing import Dict, List, Any
from utils.logger import get_logger

logger = get_logger(__name__)

class GlobalState:
    """Thread-safe global state manager."""

    def __init__(self):
        self._lock = threading.RLock()
        self._state: Dict[str, Any] = {
            "system_status": "offline",
            "current_user": None,
            "active_tasks": [],
            "loaded_modules": [],
            "conversation_id": None
        }

    def get(self, key: str) -> Any:
        """Retrieves a value from the state."""
        with self._lock:
            return self._state.get(key)

    def set(self, key: str, value: Any) -> None:
        """Updates a value in the state."""
        with self._lock:
            self._state[key] = value
            logger.debug(f"State updated: {key} = {value}")

    def append_task(self, task: str) -> None:
        """Appends a task to the active tasks list."""
        with self._lock:
            if "active_tasks" not in self._state:
                self._state["active_tasks"] = []
            self._state["active_tasks"].append(task)

    def remove_task(self, task: str) -> None:
        """Removes a task from the active tasks list."""
        with self._lock:
            try:
                self._state["active_tasks"].remove(task)
            except ValueError:
                pass
