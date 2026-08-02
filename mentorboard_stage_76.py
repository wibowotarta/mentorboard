# === Stage 76: Add graceful keyboard interrupt handling in the CLI entry point ===
# Project: MentorBoard
import signal, sys

def _handle_sigint(signum, frame):
    print("\nMentorBoard interrupted. Exiting...")
    sys.exit(0)

signal.signal(signal.SIGINT, _handle_sigint)
signal.signal(signal.SIGTERM, _handle_sigint)
