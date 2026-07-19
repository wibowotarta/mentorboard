# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: MentorBoard
def get_upcoming_items(reminders, due_date=None):
    """Return reminder items sorted by date, filtering optional due_date."""
    if due_date is None:
        return sorted(reminders, key=lambda r: r['date'])
    upcoming = [r for r in reminders if r['date'] <= due_date]
    return sorted(upcoming, key=lambda r: r['date'])


def get_overdue_items(reminders):
    """Return reminder items past their date."""
    now = datetime.datetime.now()
    return [r for r in reminders if r['date'] < now]


def format_upcoming_report(items, max_count=5):
    """Format a compact text report of upcoming items."""
    lines = ["Upcoming Reminders:\n"]
    for item in items[:max_count]:
        name = item.get('title', 'Unknown')
        due = item['date'].strftime('%Y-%m-%d') if hasattr(item['date'], 'strftime') else str(item['date'])
        lines.append(f"  - {name} (due: {due})")
    return "\n".join(lines)
