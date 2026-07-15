# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: MentorBoard
class DryRun:
    """Context manager that records mutating commands and replays them in dry-run mode."""
    def __init__(self, session):
        self.session = session
        self.recorded = []
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            for cmd in self.recorded:
                cmd()
        return False
    
    def record(self, fn):
        self.recorded.append(lambda fn=fn: fn())
