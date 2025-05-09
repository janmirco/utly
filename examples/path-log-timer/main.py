import logging

import utly


def main():
    # Set up output directory and logging
    output_dir = utly.path.set_up_output()
    utly.log.set_up(output_dir)

    # Use timer to measure performance
    with utly.timer.Timer("Special code block") as timer:
        logging.info("Some code...")
    timer.print_time(milli=False)


if __name__ == "__main__":
    main()
