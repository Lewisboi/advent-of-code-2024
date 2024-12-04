from pathlib import Path


INPUT_FILE_PATH = Path(__file__).parent / "input.txt"


def load_lists(order: bool = False) -> tuple[list[int], list[int]]:
    list_a, list_b = [], []
    with open(INPUT_FILE_PATH, "r") as input_file:
        for line in input_file.readlines():
            a, *_, b = line.split(" ")
            a, b = int(a), int(b)
            list_a.append(a)
            list_b.append(b)
    if order:
        list_a.sort()
        list_b.sort()
    return list_a, list_b
