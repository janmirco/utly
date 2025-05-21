import logging
from pathlib import Path
from typing import Callable


def set_up(output_dir: Path, log_file_name: str = "app.log") -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="[%(levelname)s] %(asctime)s - %(message)s",
        handlers=[
            logging.StreamHandler(),  # terminal output
            logging.FileHandler(output_dir / Path(log_file_name)),  # file output
        ],
    )


def start(msg: str, log_func: Callable = logging.debug) -> None:
    log_func(f"Starting {msg}...")


def end(msg: str, log_func: Callable = logging.debug) -> None:
    log_func(f"Finished {msg}.")


def cwd(log_func: Callable = logging.debug) -> None:
    log_func(f"Current working directory: {Path.cwd()}")
