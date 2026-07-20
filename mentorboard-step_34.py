# === Stage 34: Add support for multiple local user profiles ===
# Project: MentorBoard
import json, os
PROFILE_DIR = os.path.join(os.path.dirname(__file__), "profiles")

def load_profiles():
    if not os.path.isdir(PROFILE_DIR):
        return {}
    profiles = {}
    for f in os.listdir(PROFILE_DIR):
        if f.endswith(".json"):
            path = os.path.join(PROFILE_DIR, f)
            try:
                with open(path) as fh:
                    profiles[f[:-5]] = json.load(fh)
            except Exception:
                pass
    return profiles

def save_profile(name, data):
    os.makedirs(PROFILE_DIR, exist_ok=True)
    path = os.path.join(PROFILE_DIR, f"{name}.json")
    with open(path, "w") as fh:
        json.dump(data, fh, indent=2)
