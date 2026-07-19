# === Stage 31: Add compact table rendering for long lists ===
# Project: MentorBoard
def _compact_table(rows, headers):
    """Render a compact table that wraps long rows."""
    width = sum(len(h) for h in headers) + len(headers) * 3 - 1
    lines = [f"{'|'.join(f'{h:^5}' for h in headers)}"]
    for row in rows:
        cells = []
        for h, v in zip(headers, row):
            cells.append(v if v is not None else '')
            width = max(width, len(h) + 3 + len(str(cells[-1])))
        line = '|'.join(f'{c:^{width}}' % (h,) for c, h in zip(cells, headers))
        lines.append(line)
    return '\n'.join(lines)
