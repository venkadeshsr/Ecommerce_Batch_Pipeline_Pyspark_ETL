from datetime import datetime
from pathlib import Path

from src.archive_pipeline_outputs import build_archive_root


def test_archive_root_uses_day_only_structure():
    project_root = Path("/tmp/project")
    timestamp = datetime(2026, 7, 14, 15, 30, 45)

    archive_root = build_archive_root(project_root, timestamp)

    assert archive_root == project_root / "data" / "archive" / "2026" / "07" / "14"
