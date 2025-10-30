from datetime import datetime
from pathlib import Path


def set_up_output(
    output_dir_root: Path = Path.cwd() / "output",
    no_overwrite: bool = True,
) -> Path:
    if no_overwrite:
        current_time = datetime.now().isoformat()
        output_dir = output_dir_root / current_time
    else:
        output_dir = output_dir_root
    output_dir.mkdir(parents=True, exist_ok=True)
    return output_dir


def set_up_data(data_dir: Path) -> Path:
    if not data_dir.exists():
        raise FileNotFoundError(f"Given data directory does not exist: {data_dir}")
    return data_dir
