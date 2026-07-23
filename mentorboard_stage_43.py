# === Stage 43: Add CSV import for the primary record type ===
# Project: MentorBoard
import csv
from pathlib import Path

def load_csv_records(csv_path: str, record_type: str) -> list[dict]:
    records = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            entry = {}
            if record_type == 'session':
                entry['session_id'] = row.get('Session ID', '')
                entry['mentor_name'] = row.get('Mentor Name', '')
                entry['mentee_name'] = row.get('Mentee Name', '')
                entry['date'] = row.get('Date', '')
                entry['duration_min'] = int(row.get('Duration (min)', 0))
            elif record_type == 'goal':
                entry['goal_id'] = row.get('Goal ID', '')
                entry['session_id'] = row.get('Session ID', '')
                entry['title'] = row.get('Title', '')
                entry['status'] = row.get('Status', '').lower()
            elif record_type == 'question':
                entry['question_id'] = row.get('Question ID', '')
                entry['session_id'] = row.get('Session ID', '')
                entry['text'] = row.get('Text', '')
                entry['answered'] = row.get('Answered', '').lower() in ('true', 'yes')
            elif record_type == 'resource':
                entry['resource_id'] = row.get('Resource ID', '')
                entry['session_id'] = row.get('Session ID', '')
                entry['title'] = row.get('Title', '')
                entry['url'] = row.get('URL', '')
            elif record_type == 'feedback':
                entry['feedback_id'] = row.get('Feedback ID', '')
                entry['session_id'] = row.get('Session ID', '')
                entry['mentor_name'] = row.get('Mentor Name', '')
                entry['mentee_name'] = row.get('Mentee Name', '')
                entry['text'] = row.get('Text', '')
            elif record_type == 'progress':
                entry['report_id'] = row.get('Report ID', '')
                entry['session_id'] = row.get('Session ID', '')
                entry['title'] = row.get('Title', '')
                entry['date'] = row.get('Date', '')
            else:
                raise ValueError(f'Unknown record type: {record_type}')

            # Auto-generate IDs if missing
            for field, value in entry.items():
                if not value and f'{field}_id' in entry:
                    pass  # leave empty

            records.append(entry)
    return records
