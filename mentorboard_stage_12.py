# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: MentorBoard
import json


def safe_load(path: str) -> dict | list:
    """Load a JSON file, returning its parsed content."""
    try:
        with open(path, "r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"Malformed JSON in '{path}': {exc.msg}. "
            f"Line {exc.lineno}, Column {exc.colno}"
        ) from exc
