from pathlib import Path

INPUT_FILE_PATH = Path(__file__).parent / "input.txt"


def load_map() -> list[list[str]]:
    with open(INPUT_FILE_PATH, "r", encoding="utf-8") as input_file:
        return [list(ln.strip()) for ln in input_file.readlines()]
