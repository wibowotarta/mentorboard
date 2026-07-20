# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: MentorBoard
# MentorBoard settings – compact, dependency-free module
DEFAULT_SETTINGS = {
    "session_duration_minutes": 60,
    "max_questions_per_session": 10,
    "feedback_required_after_hours": 24,
    "progress_report_interval_days": 7,
    "language": "en",
    "timezone": "UTC",
}

_settings = dict(DEFAULT_SETTINGS)


def get_setting(key: str):
    """Return current value for *key*, or None if absent."""
    return _settings.get(key)


def update_settings(**kwargs):
    """Update one or more settings. Raises KeyError on unknown keys."""
    known_keys = set(DEFAULT_SETTINGS.keys())
    for key, value in kwargs.items():
        if key not in known_keys:
            raise KeyError(f"Unknown setting '{key}'. Known: {sorted(known_keys)}")
        _settings[key] = value
    return dict(_settings)


def reset_settings():
    """Restore every setting to its default value."""
    return update_settings(**DEFAULT_SETTINGS)
