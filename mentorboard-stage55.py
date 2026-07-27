# === Stage 55: Add a setting to disable colorized output ===
# Project: MentorBoard
class NoColor:
    """Disable colorized output when enabled via environment variable."""
    def __init__(self):
        self.enabled = False
        if os.environ.get("NO_COLOR"):
            self.enabled = True

    def disable(self):
        import sys
        for stream in [sys.stdout, sys.stderr]:
            stream.isatty() and stream.reconfigure(encoding="utf-8")
