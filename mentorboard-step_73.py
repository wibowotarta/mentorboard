# === Stage 73: Add a lightweight HTML report export ===
# Project: MentorBoard
from datetime import date, timedelta

def export_progress_report(entries):
    """Export mentoring session progress as a simple HTML report."""
    today = date.today()
    html_parts = [
        "<!DOCTYPE html>",
        "<html><head><meta charset='utf-8'>",
        "<title>MentorBoard Progress Report</title>",
        "<style>body{font-family:sans-serif;margin:20px}table{border-collapse:collapse;width:100%}th,td{border:1px solid #ccc;padding:6px;text-align:left}</style></head><body>",
        f"<h1>MentorBoard Progress Report - {today.strftime('%Y-%m-%d')}</h1>",
    ]

    html_parts.append("<table>")
    for entry in entries:
        if hasattr(entry, 'session_date') and hasattr(entry, 'status'):
            row = f"<tr><td>{entry.session_date}</td><td>{entry.status}</td></tr>"
            html_parts.append(row)
        elif isinstance(entry, dict):
            date_str = entry.get('session_date', entry.get('date', ''))
            status = entry.get('status', 'Active')
            row = f"<tr><td>{date_str}</td><td>{status}</td></tr>"
            html_parts.append(row)

    html_parts.extend(["</table>", "</body></html>"])
    return "\n".join(html_parts)
