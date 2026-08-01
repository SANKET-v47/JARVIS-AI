# JARVIS AI

JARVIS is a modular AI system built with clean architecture principles.

## Architecture

The project is structured into the following core components:
- `core/`: Foundational startup, versioning, and project-wide constants.
- `brain/`: Central decision-making and planning.
- `agents/`: Individual AI agents for specific tasks.
- `memory/`: Short-term and long-term memory storage mechanisms.
- `voice/`: Speech-to-text and text-to-speech processing.
- `vision/`: Image and video processing capabilities.
- `tools/`: Extensible tools and integrations that the agents can use.
- `database/`: Database models and connection management.
- `config/`: Configuration management and loading.
- `logs/`: Application log output directory.
- `ui/`: User interfaces (CLI, Web, etc.).
- `api/`: API endpoints for external communication.
- `utils/`: Shared utilities and helpers like logging.
- `tests/`: Automated test suites.

## Setup

1. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Or .venv\Scripts\activate on Windows
   pip install -r requirements.txt
   ```
2. Copy `.env.example` to `.env` and fill in your keys.
3. Run the application:
   ```bash
   python main.py
   ```
