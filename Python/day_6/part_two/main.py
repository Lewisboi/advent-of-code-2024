from copy import deepcopy
from common import load_map
from part_one import Map, CellState, generate_map_lines, free_spaces


def main():
    string_map = load_map()
    lines, guard = generate_map_lines(string_map)
    count = 0
    for i, j in free_spaces(lines):
        lines_copy = deepcopy(lines)
        guard_copy = deepcopy(guard)
        lines_copy[i][j] = CellState.OBSTRUCTED
        map_instance = Map(lines=lines_copy, guard=guard_copy)
        if map_instance.is_looping():
            count += 1
    print(count)


main()
