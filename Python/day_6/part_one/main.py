from common import load_map
from part_one import CellState, Map


def main():
    string_map = load_map()
    actual_map = Map.from_string_map(string_map)
    actual_map.simulate()
    print(actual_map.count_cells_on_state(CellState.VISITED))


main()
