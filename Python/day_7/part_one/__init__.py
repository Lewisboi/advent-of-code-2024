from enum import Enum
from typing import Callable


class Operator(str, Enum):
    ADD = "+"
    MULT = "*"
    CONCAT = "||"

    def __repr__(self):
        return self.value


def equate(
    num: int,
    operands: list[int],
    operation_mapping: dict[Operator, Callable[[int, int], int]],
) -> list[list[Operator]] | None:
    if not operands:
        return None
    first, *rest = operands
    if not rest:
        if first == num:
            return [[]]
        return None
    if first > num:
        return None
    second, *rest = rest
    options = []
    for op_key, op in operation_mapping.items():
        result = op(first, second)
        inner_options = equate(num, [result] + rest, operation_mapping)
        if inner_options:
            for o in inner_options:
                options.append([op_key] + o)
    return options or None
