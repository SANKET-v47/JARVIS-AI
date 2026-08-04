"""
core.engine
-----------

This module acts as the core runtime engine for the JARVIS application.
It initializes services, binds the event bus, and controls the main execution loop.
"""

from core.event_bus import EventBus
from core.state import GlobalState
from core.service_registry import ServiceRegistry
from utils.logger import get_logger

# Existing subsystems to orchestrate
from core.input_handler import InputHandler
from brain.conversation import ConversationManager

logger = get_logger(__name__)

class JarvisEngine:
    """The central runtime engine of JARVIS."""

    def __init__(self):
        """Initializes the engine and its core components."""
        self.registry = ServiceRegistry()
        self.event_bus = EventBus()
        self.state = GlobalState()
        
        # Initialize subsystem pipeline
        self.input_handler = InputHandler()
        self.conversation_manager = ConversationManager()

    def start(self):
        """Starts the application and registers services."""
        logger.info("Initializing JARVIS Core Engine...")
        
        # Register core services for dependency injection
        self.registry.register("event_bus", self.event_bus)
        self.registry.register("state", self.state)
        
        # Update state
        self.state.set("system_status", "ready")
        
        # Publish startup event
        self.event_bus.publish("system:ready")
        
        logger.info("Engine successfully started.")

    def run(self):
        """Exposes the main run loop."""
        self.start()
        
        logger.info("=" * 40)
        logger.info("🤖 JARVIS CORE ENGINE ONLINE")
        logger.info("Type 'exit' to shut down.")
        logger.info("=" * 40)

        while self.state.get("system_status") == "ready":
            # 1. Get input
            raw_input = self.input_handler.get_input()
            if not raw_input or not raw_input.strip():
                continue
            
            normalized_input = raw_input.strip().lower()
            
            # Exit loop gracefully
            if normalized_input == "exit":
                logger.info("JARVIS: Shutting down...")
                print("JARVIS: Goodbye! Shutting down.")
                self.state.set("system_status", "offline")
                break
                
            # 2. Process via ConversationManager
            result = self.conversation_manager.generate_response(raw_input)
            
            # Publish event for execution result
            self.event_bus.publish("action:executed", {"result": result})
            
            # Print the result back to the user
            print(f"JARVIS: {result}")
