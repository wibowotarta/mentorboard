# === Stage 3: Add validation helpers for required fields, identifiers, and short text values ===
# Project: MentorBoard
import re


def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email))


def validate_id(value):
    if not value or len(value) > 128:
        raise ValueError(f"ID must be a non-empty string of at most 128 characters. Got: {value!r}")
    return True


def validate_short_text(text, max_length=500):
    if text is None:
        raise ValueError("Short text cannot be empty.")
    if len(text) > max_length:
        raise ValueError(f"Text exceeds maximum length of {max_length}. Got: {len(text)} characters.")
    return True


def validate_required(value, field_name="field"):
    if not value or (isinstance(value, str) and not value.strip()):
        raise ValueError(f"{field_name} is required and cannot be empty.")
    return True
