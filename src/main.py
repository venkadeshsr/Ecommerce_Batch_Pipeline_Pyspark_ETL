import subprocess
import sys
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parent
    jobs_dir = project_root / "jobs"

    jobs = [
        jobs_dir / "job_bronze_to_silver.py",
        jobs_dir / "job_gold_reports.py",
    ]

    for job_path in jobs:
        print(f"Running {job_path.name}")
        completed = subprocess.run(
            [sys.executable, str(job_path)],
            cwd=str(project_root),
            check=False,
        )
        if completed.returncode != 0:
            raise SystemExit(f"Job failed: {job_path.name}")

    print("Pipeline completed successfully")


if __name__ == "__main__":
    main()
