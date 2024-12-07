import re
from common import load_map

PATTERN = r"(XMAS)"


def searchable_lines(map_: list[list[str]]) -> list[str]:
    # Rows as strings
    rows: list[str] = ["".join(line) for line in map_]

    # Columns as strings
    cols: list[str] = [
        "".join(map_[i][j] for i in range(len(map_))) for j in range(len(map_[0]))
    ]

    # Helper to get diagonals
    def get_diagonal(start_row: int, start_col: int, direction: tuple[int, int]) -> str:
        diagonal: list[str] = []
        rows, cols = len(map_), len(map_[0])
        row, col = start_row, start_col
        while 0 <= row < rows and 0 <= col < cols:
            diagonal.append(map_[row][col])
            row, col = row + direction[0], col + direction[1]
        return "".join(diagonal)

    def reverse_string(string: str) -> str:
        return "".join(reversed(string))

    # Diagonals: Top-left to bottom-right
    diagonals: list[str] = []
    rows_count, cols_count = len(map_), len(map_[0])
    for col in range(cols_count):
        diagonals.append(get_diagonal(0, col, (1, 1)))
    for row in range(1, rows_count):
        diagonals.append(get_diagonal(row, 0, (1, 1)))

    # Diagonals: Bottom-left to top-right
    for col in range(cols_count):
        diagonals.append(get_diagonal(rows_count - 1, col, (-1, 1)))
    for row in range(rows_count - 2, -1, -1):
        diagonals.append(get_diagonal(row, 0, (-1, 1)))

    return (
        rows
        + cols
        + diagonals
        + list(map(reverse_string, rows))
        + list(map(reverse_string, cols))
        + list(map(reverse_string, diagonals))
    )


def main():
    occurences = 0
    searchable = searchable_lines(load_map())
    for searchable_line in searchable:
        occurences += len(re.findall(PATTERN, searchable_line))
    print(occurences)


main()
