"""
main.py
-------

This is the main entry point for the JARVIS application. It exists to 
bootstrap the core systems using the StartupManager and launch the Engine.
"""

import sys
from core.startup import StartupManager
from core.engine import JarvisEngine
from utils.logger import get_logger

def main():
    """Main execution entry point for JARVIS."""
    # 1. Initialize the startup sequence
    startup_manager = StartupManager()
    config = startup_manager.boot()
    
    logger = get_logger(__name__)
    
    # 2. Instantiate and run the Core Engine
    try:
        engine = JarvisEngine()
        engine.run()
    except KeyboardInterrupt:
        logger.info("JARVIS: Process interrupted by user. Shutting down...")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Critical Engine Failure: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
