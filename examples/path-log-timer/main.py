import logging
from pathlib import Path

import utly


def main():
    # Set up output directory and logging
    output_dir = utly.path.set_up_output(
        output_dir_root=Path.cwd() / "output/0000-00-00",
        no_overwrite=False,
    )
    utly.log.set_up(output_dir)

    # Use timer to measure performance
    with utly.timer.Timer("Special code block") as timer:
        logging.info("Some code...")
    timer.print_time(milli=False)


if __name__ == "__main__":
    main()
