# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: MentorBoard
def _merge_imports(existing, new):
    merged = []
    for line in new:
        stripped = line.strip()
        if (stripped.startswith("import ") and " as " not in stripped) or \
           (stripped.startswith("from ") and ")" in stripped):
            base = stripped.split("(")[0].replace(",", "").strip()
            if base not in merged:
                existing.append(stripped)
                merged.append(base)
        elif stripped.startswith("import "):
            parts = [p.strip() for p in stripped.replace(",", " ").split()]
            head = parts[1] if len(parts) > 1 else parts[0]
            if head not in merged:
                existing.append(stripped)
                merged.append(head)
        elif stripped.startswith("from ") and ")" in stripped:
            inner = stripped.split("(")[1].rstrip(")").strip()
            head = inner.split(",")[0].split()[0]
            if head not in merged:
                existing.append(stripped)
                merged.append(head)
    return existing
