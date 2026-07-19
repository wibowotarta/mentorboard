# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: MentorBoard
from datetime import date, timedelta


def parse_date(date_str):
    """Parse a date string in YYYY-MM-DD format and return a date object."""
    try:
        parsed = date.fromisoformat(date_str)
        if parsed.year < 1900 or parsed.year > date.today().year + 1:
            raise ValueError(f"Date {date_str} is outside the valid range (1900-2100).")
        return parsed
    except Exception as e:
        raise ValueError(f"Invalid date format '{date_str}'. Expected YYYY-MM-DD. Error: {e}")


def days_between(date_a, date_b):
    """Return the number of days between two date objects."""
    if not isinstance(date_a, date) or not isinstance(date_b, date):
        raise TypeError("Both arguments must be datetime.date instances.")
    return abs((date_a - date_b).days)


def add_days(current_date, n_days):
    """Add a number of days to a given date and return the new date."""
    if n_days < 0:
        raise ValueError(f"Cannot subtract days. Got {n_days} days.")
    return current_date + timedelta(days=n_days)


def format_interval(start_date, end_date):
    """Return a human-readable interval string like '5 days'."""
    d = days_between(start_date, end_date)
    if d == 0:
        return "today"
    elif d == 1:
        return "yesterday"
    else:
        return f"{d} {'day' if d == 1 else 'days'} ago"
