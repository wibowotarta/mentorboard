# === Stage 63: Add relationships between records where useful ===
# Project: MentorBoard
# relationships between records
def link_records(records, max_links=3):
    """Link records by shared mentor/mentee/goal using Jaccard similarity."""
    import itertools
    keys = ["mentor", "mentee", "goal"]
    for i in range(len(records)):
        for j in range(i + 1, len(records)):
            if j - i > max_links: break
            scores = []
            for key in keys:
                vals_i = {r.get(key) for r in records[:i+1] if r.get(key)}
                vals_j = {r.get(key) for r in records[i:] if r.get(key)}
                union = vals_i | vals_j
                inter = vals_i & vals_j
                scores.append(len(inter) / len(union) if union else 0.0)
            avg_score = sum(scores) / len(scores)
            if avg_score > 0.3:
                records[i]["related"] = records[j]
