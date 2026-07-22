# === Stage 41: Add plain text import for a simple line-based format ===
# Project: MentorBoard
def parse_line_block(text):
    """Parse a line-based text block into structured records."""
    records = []
    current_record = {}
    for line in text.strip().split('\n'):
        if not line:
            continue
        colon_idx = line.index(':')
        key = line[:colon_idx].strip()
        value = line[colon_idx + 1:].strip()
        if key == 'record':
            records.append(current_record)
            current_record = {}
        else:
            current_record[key] = value
    if current_record:
        records.append(current_record)
    return records
