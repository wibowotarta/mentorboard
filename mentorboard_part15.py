# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: MentorBoard
def dispatch(command, args):
    commands = {
        "help": lambda: print("Available commands: help, status, new-session"),
        "status": lambda: print("Current session: active, goals set, progress tracked"),
        "new-session": lambda: print("Starting new mentoring session"),
    }
    handler = commands.get(command)
    if handler:
        return handler()
    else:
        raise ValueError(f"Unknown command: {command}")
