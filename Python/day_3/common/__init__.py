from pathlib import Path


INPUT_FILE_PATH = Path(__file__).parent / "input.txt"


def load_input() -> str:
    with open(INPUT_FILE_PATH, "r") as input_file:
        return input_file.read()
