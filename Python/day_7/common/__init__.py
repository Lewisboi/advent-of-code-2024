from pathlib import Path

INPUT_FILE_PATH = Path(__file__).parent / "input.txt"

RESULT_SEPARATOR = ":"
EQUATION_SEPARATOR = " "


def load_equations() -> list[tuple[int, list[int]]]:
    with open(INPUT_FILE_PATH, "r", encoding="utf-8") as input_file:
        return [
            (int(res), [int(n) for n in eq.strip().split(EQUATION_SEPARATOR)])
            for res, eq in (
                line.split(RESULT_SEPARATOR) for line in input_file.readlines()
            )
        ]
