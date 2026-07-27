# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: MentorBoard
def colorize(text, code):
    return f"\033[{code}m{text}\033[0m" if code else text

class _Colors:
    RED = "1;31"; GREEN = "1;32"; YELLOW = "1;33"; BLUE = "1;34"
    MAGENTA = "1;35"; CYAN = "1;36"; WHITE = "1;37"; BOLD = "1"

def fmt_goal(status, name):
    return colorize(f"[{status}] {name}", YELLOW if status == "active" else GREEN)

def print_report(report, colors=_Colors()):
    print(colorize("=== MENTORING SESSION REPORT ===", colors.BOLD))
    for section in report:
        print()
        title = section.get("title", "")
        items = section.get("items", [])
        if not title and not items:
            continue
        print(f"{colors.CYAN}{title}")
        for i, item in enumerate(items):
            marker = "•" if isinstance(item, dict) else str(i+1)
            val = item.get("value") or item
            if isinstance(val, tuple):
                status, name = val
                print(f"  {marker} {fmt_goal(status, name)}")
            elif isinstance(val, list):
                for q in val:
                    print(f"  - Q[{q.get('status','pending')}] {q.get('question','?')}")
            else:
                print(f"  {marker} {val}")
    print(colorize("=== END REPORT ===", colors.BOLD))

def log_feedback(mentor, student):
    return colorize(f"{mentor}: '{student}' — good progress!", GREEN)
