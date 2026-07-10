# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: MentorBoard
def delete_entry(db_path, table_name, record_id, confirm=False):
    """Delete a row from a SQLite table if confirmed."""
    try:
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {table_name} WHERE id = ?", (record_id,))
        deleted = cur.rowcount
        conn.commit()
        conn.close()
        return {"status": "deleted", "id": record_id, "rows_affected": deleted}
    except Exception as e:
        return {"status": "error", "message": str(e)}
