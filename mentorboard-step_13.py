# === Stage 13: Add file save support using a configurable path ===
# Project: MentorBoard
import os, json

def save_session(path: str, session):
    d = {k: v for k, v in session.items() if isinstance(v, (str, int, float, bool))}
    if 'resources' in d and isinstance(d['resources'], list):
        d['resources'] = [r.get('title', '')[:80] + ('...' if len(r) > 80 else '') for r in d['resources']]
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump(d, f, indent=2)

def load_session(path):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
