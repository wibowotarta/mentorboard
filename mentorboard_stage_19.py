# === Stage 19: Add undo support for the last simple mutation ===
# Project: MentorBoard
import copy, json

def last_undo():
    history = getattr(last_session, 'history', [])
    if not history:
        return None
    state = copy.deepcopy(history[-1])
    del history[-1]
    return state
