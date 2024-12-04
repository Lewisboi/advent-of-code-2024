from pathlib import Path
from typing import Callable

INPUT_FILE_PATH = Path(__file__).parent / "input.txt"
SEP = " "


def load_levels() -> list[list[int]]:
    with open(INPUT_FILE_PATH, "r") as input_file:
        return [[int(n) for n in line.split(SEP)] for line in input_file.readlines()]


MIN_DIFFERENCE = 1
MAX_DIFFERENCE = 3


def is_safe(level: list[int]) -> bool:
    length = len(level)
    if length <= 1:
        return True
    curr, next, *rest = level
    diff = curr - next
    abs_diff = abs(diff)
    if abs_diff < MIN_DIFFERENCE or abs_diff > MAX_DIFFERENCE:
        return False
    global_direction = diff / abs_diff
    level = [next] + rest
    while len(level) >= 2:
        curr, next, *rest = level
        diff = curr - next
        abs_diff = abs(diff)
        if abs_diff < MIN_DIFFERENCE or abs_diff > MAX_DIFFERENCE:
            return False
        direction = diff / abs_diff
        if direction != global_direction:
            return False
        level = [next] + rest

    return True


def count_levels_with_condition(
    levels: list[int], condition: Callable[[list[int]], bool]
) -> int:
    return sum(condition(level) for level in levels)
