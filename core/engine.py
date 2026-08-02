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
from core.command_parser import CommandParser
from core.intent import IntentDetector
from core.router import ActionRouter
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
        self.parser = CommandParser()
        self.intent_detector = IntentDetector()
        self.router = ActionRouter()
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
            
            # 2. Parse and normalize
            tokens = self.parser.parse(raw_input)
            if not tokens:
                continue
                
            # 3. Detect intent
            intent = self.intent_detector.detect(tokens)
            
            # Exit loop gracefully if intent is exit
            if intent == "exit":
                logger.info("JARVIS: Shutting down...")
                farewell = self.conversation_manager.generate_response(raw_input)
                if farewell == "I'm still learning. I don't know how to respond to that yet.":
                    farewell = "Goodbye! Shutting down."
                print(f"JARVIS: {farewell}")
                self.state.set("system_status", "offline")
                break
                
            # Publish event for intent detection
            self.event_bus.publish("intent:detected", {"intent": intent})
            
            # 4. Route to an action and execute
            if intent in ["greeting", "unknown"]:
                result = self.conversation_manager.generate_response(raw_input)
            else:
                result = self.router.route(intent, tokens)
            
            # Publish event for execution result
            self.event_bus.publish("action:executed", {"result": result})
            
            # Print the result back to the user
            print(f"JARVIS: {result}")
