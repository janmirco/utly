# ⚙️ Utly

For many of my projects, I frequently need utilities for setting up directories, logging, measuring performance, and more.
This project serves as a centralized collection of these handy tools to simplify and speed up development.

## Usage

How to use Utly can be found in the [examples](examples) directory.

## Installation

### Directly via GitHub

Go to your `uv` project and install `utly`.

```bash
uv add git+https://github.com/janmirco/utly.git
```

For future updates, simply run the following code block.

```bash
uv lock --upgrade
uv sync
```

### Locally in editable mode

1. Clone repository.

```bash
git clone https://github.com/janmirco/utly.git
```

2. Go to your `uv` project and install `utly` in editable mode.

```bash
uv add --editable <PATH_TO_HELLO_REPO>
```

## Software used

- Language: [Python](https://www.python.org/)
- Code execution: [GNU Make](https://www.gnu.org/software/make/)
- Package and project manager: [uv](https://docs.astral.sh/uv/)
