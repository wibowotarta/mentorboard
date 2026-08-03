# === Stage 79: Add a final self-check command that runs validations and demo operations ===
# Project: MentorBoard
#!/usr/bin/env python3
"""Self-check demo for MentorBoard."""

import sys, os

def check_file(path: str) -> bool:
    return os.path.isfile(path) and os.access(path, os.R_OK)

files = ["goals.py", "questions.py", "resources.py", "feedback.py", "progress.py"]
assert all(check_file(f) for f in files), "Missing MentorBoard modules"

from goals import Goal; from questions import Question; from resources import Resource
from feedback import Feedback; from progress import ProgressReport

g = Goal("Learn Python", "Intermediate")
q = Question("What is a list?")
r = Resource("Python docs: https://docs.python.org/3/")
fb = Feedback(g, q, r, score=85)
p = ProgressReport(g, fb, week=12)

print(f"Goal {g.title}: progress {p.week} weeks, feedback score {fb.score}")
assert p.is_complete() is False
print("All checks passed.")
