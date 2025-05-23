import logging
from pathlib import Path


def set_up(output_dir: Path, log_file_name: str = "app.log") -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(asctime)s - %(message)s",
        handlers=[
            logging.StreamHandler(),  # terminal output
            logging.FileHandler(output_dir / Path(log_file_name)),  # file output
        ],
    )
