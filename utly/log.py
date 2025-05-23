import logging
from pathlib import Path


def set_up(
    output_dir: Path,
    level: int = logging.INFO,
    format: str = "[%(levelname)s] %(asctime)s - %(message)s",
    terminal_output: bool = True,
    file_output: bool = True,
    file_name: str = "app.log",
) -> None:
    """
    By default, logs to both terminal and file.
    If both outputs are disabled, attaches a NullHandler to silence all logging output.
    """

    handlers = []
    if terminal_output:
        handlers.append(logging.StreamHandler())
    if file_output:
        handlers.append(logging.FileHandler(output_dir / Path(file_name)))

    logging.basicConfig(
        level=level,
        format=format,
        handlers=handlers if handlers else [logging.NullHandler()],
    )
