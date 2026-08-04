"""
planner/planner.py

The Planner analyzes the user's input and decides what JARVIS
should do next.

It does NOT execute anything.
It only returns a decision.
"""


class Planner:
    """Determines how the user's request should be handled."""

    def analyze(self, text: str) -> dict:
        """
        Analyze the user input and return a decision.

        Returns:
            dict: A decision containing:
                type   -> tool / memory / conversation
                intent -> specific action
                target -> optional value
        """

        text = text.lower().strip()

        # ----------------------------
        # System Tools
        # ----------------------------
        if "time" in text:
            return {
                "type": "tool",
                "intent": "get_time"
            }

        if "date" in text:
            return {
                "type": "tool",
                "intent": "get_date"
            }

        if "computer name" in text:
            return {
                "type": "tool",
                "intent": "get_computer_name"
            }

        if "username" in text:
            return {
                "type": "tool",
                "intent": "get_username"
            }

        if "current directory" in text:
            return {
                "type": "tool",
                "intent": "get_cwd"
            }

        if "python version" in text:
            return {
                "type": "tool",
                "intent": "get_python_version"
            }

        # ----------------------------
        # Browser
        # ----------------------------
        if "open youtube" in text:
            return {
                "type": "tool",
                "intent": "open_website",
                "target": "https://youtube.com"
            }

        if "open google" in text:
            return {
                "type": "tool",
                "intent": "open_website",
                "target": "https://google.com"
            }

        # ----------------------------
        # Applications
        # ----------------------------
        if "open chrome" in text:
            return {
                "type": "tool",
                "intent": "open_app",
                "target": "chrome"
            }

        if "open notepad" in text:
            return {
                "type": "tool",
                "intent": "open_app",
                "target": "notepad"
            }

        # ----------------------------
        # Memory Questions
        # ----------------------------
        if "what is my name" in text:
            return {
                "type": "memory"
            }

        if "favorite color" in text:
            return {
                "type": "memory"
            }

        # ----------------------------
        # Default
        # ----------------------------
        return {
            "type": "conversation"
        }
