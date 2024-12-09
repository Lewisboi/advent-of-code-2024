from dataclasses import dataclass, field
from enum import Enum


class Direction(str, Enum):
    UP = "^"
    DOWN = "v"
    LEFT = "<"
    RIGHT = ">"

    def vector(self) -> tuple[int, int]:
        match self:
            case Direction.UP:
                return (-1, 0)
            case Direction.DOWN:
                return (1, 0)
            case Direction.LEFT:
                return (0, -1)
            case Direction.RIGHT:
                return (0, 1)

    def turn_clockwise(self) -> "Direction":
        match self:
            case Direction.UP:
                return Direction.RIGHT
            case Direction.DOWN:
                return Direction.LEFT
            case Direction.LEFT:
                return Direction.UP
            case Direction.RIGHT:
                return Direction.DOWN

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.__repr__()


@dataclass(repr=True)
class Guard:
    position: tuple[int, int]
    direction: Direction

    def avoid(self) -> None:
        self.direction = self.direction.turn_clockwise()

    def simulate_step(self) -> tuple[int, int]:
        curr_i, curr_j = self.position
        delta_i, delta_j = self.direction.vector()
        return (curr_i + delta_i, curr_j + delta_j)

    def take_step(self) -> None:
        self.position = self.simulate_step()

    def state(self) -> tuple[tuple[int, int], Direction]:
        return (self.position, self.direction)

    def __repr__(self):
        return self.direction.__repr__()

    def __str__(self):
        return self.__repr__()


class CellState(str, Enum):
    FREE = "."
    OBSTRUCTED = "#"
    VISITED = "X"

    def __repr__(self):
        return self.value

    def __str__(self):
        return self.__repr__()


class SimulationState(str, Enum):
    ONGOING = "ongoing"
    FINISHED = "finished"
    LOOPING = "looping"


def generate_map_lines(
    string_map: list[list[str]],
) -> tuple[list[list[CellState | Guard]], Guard]:
    lines = []
    for i, line in enumerate(string_map):
        new_line = []
        for j, elem in enumerate(line):
            try:
                direction = Direction(elem)
                guard = Guard((i, j), direction)
                new_line.append(guard)
            except ValueError:
                cell_state = CellState(elem)
                new_line.append(cell_state)
        lines.append(new_line)
    return lines, guard


def free_spaces(lines: list[list[CellState | Guard]]):
    for i, line in enumerate(lines):
        for j, elem in enumerate(line):
            match elem:
                case CellState.FREE:
                    yield (i, j)


@dataclass
class Map:
    lines: list[list[CellState | Guard]]
    guard: Guard
    guard_states: set[tuple[tuple[int, int], Direction]] = field(default_factory=set)

    @staticmethod
    def from_string_map(string_map: list[list[str]]) -> "Map":
        lines, guard = generate_map_lines(string_map)
        return Map(lines=lines, guard=guard)

    def is_inside(self, position: tuple[int, int]) -> bool:
        i, j = position
        return (0 <= i < len(self.lines)) and (0 <= j < len(self.lines[0]))

    def step(self) -> SimulationState:
        curr_state = self.guard.state()
        curr_pos, curr_dir = curr_state
        if curr_state in self.guard_states:
            return SimulationState.LOOPING
        if not self.is_inside(curr_pos):
            return SimulationState.FINISHED
        self.guard_states.add((curr_pos, curr_dir))
        current_i, current_j = curr_pos
        step = self.guard.simulate_step()
        if self.is_inside(step):
            simulated_i, simulated_j = step
            match self.lines[simulated_i][simulated_j]:
                case CellState.FREE | CellState.VISITED:
                    self.lines[current_i][current_j] = CellState.VISITED
                    self.guard.take_step()
                    self.lines[simulated_i][simulated_j] = self.guard
                case CellState.OBSTRUCTED:
                    self.guard.avoid()
            return SimulationState.ONGOING
        self.lines[current_i][current_j] = CellState.VISITED
        self.guard.take_step()
        return SimulationState.FINISHED

    def simulate(self) -> None:
        while self.step() == SimulationState.ONGOING:
            continue

    def is_looping(self) -> bool:
        self.simulate()
        match self.step():
            case SimulationState.FINISHED:
                return False
            case SimulationState.LOOPING:
                return True

    def count_cells_on_state(self, state: CellState) -> int:
        count = 0
        for line in self.lines:
            for elem in line:
                if elem == state:
                    count += 1
        return count

    def __repr__(self):
        return "\n".join("".join([str(elem) for elem in line]) for line in self.lines)
