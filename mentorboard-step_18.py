# === Stage 18: Add an activity log with timestamps and action names ===
# Project: MentorBoard
class ActivityLog:
    def __init__(self):
        self.entries = []

    def log(self, action, timestamp=None):
        if timestamp is None:
            import datetime as dt
            timestamp = dt.datetime.now()
        entry = {"timestamp": timestamp.isoformat(), "action": action}
        self.entries.append(entry)
        return entry

    def get_summary(self):
        if not self.entries:
            return []
        actions = [e["action"] for e in self.entries]
        counts = {}
        for a in actions:
            counts[a] = counts.get(a, 0) + 1
        return [{"action": k, "count": v} for k, v in counts.items()]

    def get_last(self):
        if not self.entries:
            return None
        return self.entries[-1]
