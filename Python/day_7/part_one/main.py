from common import load_equations
from typing import Callable
from part_one import equate, Operator


OPERATION_MAPPING: dict[Operator, Callable[[int, int], int]] = {
    Operator.ADD: lambda a, b: a + b,
    Operator.MULT: lambda a, b: a * b,
}


def main():
    equations = load_equations()
    print(
        sum(
            num
            for num, operands in equations
            if equate(num, operands, OPERATION_MAPPING)
        )
    )


main()
