from pathlib import Path

INPUT_FILE_PATH = Path(__file__).parent / "input.txt"


def load_map() -> list[list[str]]:
    with open(INPUT_FILE_PATH, "r") as input_file:
        return [list(line.strip()) for line in input_file.readlines()]
