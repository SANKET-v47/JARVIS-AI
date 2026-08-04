from abc import ABC, abstractmethod
from typing import Any

class BaseTool(ABC):
    """
    Abstract base class for all tools in JARVIS.
    All tools should inherit from this class and implement the required methods.
    """
    
    @property
    @abstractmethod
    def name(self) -> str:
        """The name of the tool."""
        pass
        
    @property
    @abstractmethod
    def description(self) -> str:
        """A brief description of what the tool does."""
        pass

    @abstractmethod
    def execute(self, *args, **kwargs) -> Any:
        """
        Executes the tool's core functionality.
        """
        pass
