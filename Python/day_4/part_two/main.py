import re
from common import load_map

PATTERN = r"(MAS)|(SAM)"
CENTER = "A"


def is_xmas(center: tuple[int, int], map_: list[list[str]]) -> bool:
    i, j = center
    if (i in (0, len(map_) - 1)) or (j in (0, len(map_[0]) - 1)):
        return False
    diag_a = "".join(map_[i + n][j + n] for n in (-1, 0, 1))
    diag_b = "".join(map_[i - n][j + n] for n in (-1, 0, 1))
    return re.match(PATTERN, diag_a) and re.match(PATTERN, diag_b)


def find_centers(map_: list[list[str]]) -> list[tuple[int, int]]:
    return [
        (i, j)
        for i in range(len(map_))
        for j in range(len(map_[0]))
        if map_[i][j] == CENTER
    ]


def main():
    count = 0
    map_ = load_map()
    for i, j in find_centers(map_):
        if is_xmas((i, j), map_):
            count += 1

    print(count)


main()
