# === Stage 44: Add backup creation for the data file ===
# Project: MentorBoard
def backup_data(data_file: str, archive_dir: str = "backups") -> str:
    os.makedirs(archive_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    src_path = Path(data_file).resolve()
    dst_path = Path(archive_dir) / f"{src_path.name}.{timestamp}"
    shutil.copy2(src_path, dst_path)
    return str(dst_path)
