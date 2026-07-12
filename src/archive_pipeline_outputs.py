import argparse
import shutil
from datetime import datetime
from pathlib import Path
from typing import List, Optional


def get_project_root() -> Path:
    return Path(__file__).resolve().parents[1]


def build_archive_root(project_root: Path, timestamp: Optional[datetime] = None) -> Path:
    run_time = timestamp or datetime.now()
    return (
        project_root
        / "data"
        / "archive"
        / run_time.strftime("%Y")
        / run_time.strftime("%m")
        / run_time.strftime("%d")
        / run_time.strftime("%H")
        / run_time.strftime("%M")
    )


def ensure_unique_path(path: Path) -> Path:
    if not path.exists():
        return path

    counter = 1
    while True:
        if path.suffix:
            candidate = path.with_name(f"{path.stem}_{counter}{path.suffix}")
        else:
            candidate = path.parent / f"{path.name}_{counter}"

        if not candidate.exists():
            return candidate
        counter += 1


def archive_raw_files(raw_dir: Path, archive_root: Path) -> List[str]:
    archived_files: List[str] = []

    if not raw_dir.exists():
        return archived_files

    destination_dir = archive_root / "raw"
    destination_dir.mkdir(parents=True, exist_ok=True)

    for raw_file in sorted(raw_dir.glob("*.csv")):
        destination_path = ensure_unique_path(destination_dir / raw_file.name)
        shutil.move(str(raw_file), str(destination_path))
        archived_files.append(str(destination_path.relative_to(get_project_root())))

    return archived_files


def archive_report_folders(gold_dir: Path, archive_root: Path) -> List[str]:
    archived_folders: List[str] = []

    if not gold_dir.exists():
        return archived_folders

    destination_root = archive_root / "reports"
    destination_root.mkdir(parents=True, exist_ok=True)

    for report_dir in sorted(gold_dir.iterdir()):
        if not report_dir.is_dir():
            continue

        destination_dir = ensure_unique_path(destination_root / report_dir.name)
        shutil.move(str(report_dir), str(destination_dir))
        archived_folders.append(str(destination_dir.relative_to(get_project_root())))

    return archived_folders


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Move raw CSV files and generated report folders into timestamp-based archive folders."
    )
    parser.add_argument(
        "--project-root",
        default=str(get_project_root()),
        help="Project root path (defaults to the repository root).",
    )
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    raw_dir = project_root / "data" / "raw"
    gold_dir = project_root / "data" / "gold"
    archive_root = build_archive_root(project_root)
    archive_root.mkdir(parents=True, exist_ok=True)

    raw_archived = archive_raw_files(raw_dir, archive_root)
    report_archived = archive_report_folders(gold_dir, archive_root)

    print("=" * 60)
    print("Archive completed successfully")
    print("=" * 60)
    print(f"Archive root : {archive_root}")
    print(f"Raw files archived : {len(raw_archived)}")
    for item in raw_archived:
        print(f"  - {item}")

    print(f"Report folders archived : {len(report_archived)}")
    for item in report_archived:
        print(f"  - {item}")
    print("=" * 60)


if __name__ == "__main__":
    main()
