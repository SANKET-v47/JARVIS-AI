"""
main.py
-------

This is the main entry point for the JARVIS application. It exists to 
bootstrap the core systems using the StartupManager and keep the main 
application loop running.
"""

import sys
from core.startup import StartupManager
from utils.logger import get_logger
from core.input_handler import InputHandler
from core.command_parser import CommandParser
from core.intent import IntentDetector
from core.router import ActionRouter

def main():
    """Main execution loop for JARVIS."""
    # Initialize the startup sequence
    startup_manager = StartupManager()
    config = startup_manager.boot()
    
    logger = get_logger(__name__)
    
    # Initialize Command Interpreter Pipeline
    input_handler = InputHandler()
    parser = CommandParser()
    intent_detector = IntentDetector()
    router = ActionRouter()
    
    logger.info("=" * 40)
    logger.info("🤖 JARVIS ONLINE")
    logger.info("Type 'exit' to shut down.")
    logger.info("=" * 40)
    
    try:
        while True:
            # 1. Get input
            raw_input = input_handler.get_input()
            
            # 2. Parse and normalize
            tokens = parser.parse(raw_input)
            if not tokens:
                continue
                
            # 3. Detect intent
            intent = intent_detector.detect(tokens)
            
            # Exit loop gracefully if intent is exit
            if intent == "exit":
                logger.info("JARVIS: Shutting down...")
                break
                
            # 4. Route to an action and execute
            result = router.route(intent, tokens)
            
            # Print the result back to the user
            print(f"JARVIS: {result}")
                
    except KeyboardInterrupt:
        logger.info("JARVIS: Process interrupted by user. Shutting down...")
        sys.exit(0)

if __name__ == "__main__":
    main()
