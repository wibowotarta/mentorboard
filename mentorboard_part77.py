# === Stage 77: Add type hints to older helper functions that are missing them ===
# Project: MentorBoard
def format_progress_report(report: dict) -> str:
    """Return a human-readable string from a progress report dictionary."""
    sections = [f"{k}: {v}" for k, v in report.items() if isinstance(v, (str, int, float))]
    return "\n".join(sections)


def validate_goal(goal_data: dict) -> bool:
    """Check that goal data contains required non-empty fields."""
    required = {"title", "description"}
    for field in required:
        if not isinstance(goal_data.get(field), str) or not goal_data[field].strip():
            return False
    return True


def safe_divide(numerator: float, denominator: float, default: float = 0.0) -> float:
    """Perform division safely and return a fallback value on ZeroDivisionError."""
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return default


def merge_reports(base: dict, override: dict) -> dict:
    """Return a shallow copy of base with any non-None values from override applied."""
    result = {k: v for k, v in base.items() if isinstance(v, (str, int, float))}
    for key, val in override.items():
        if val is not None and isinstance(val, (str, int, float)):
            result[key] = val
    return result


def truncate_text(text: str, max_length: int) -> str:
    """Truncate text to a maximum length, appending an ellipsis when needed."""
    if len(text) <= max_length:
        return text
    return text[:max_length - 3] + "..."
