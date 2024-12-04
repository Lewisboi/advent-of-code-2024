import re
from abc import ABC, abstractmethod
from common import load_input


PATTERN = r"mul\(-?\d+,-?\d+\)"


class Operation(ABC):
    @abstractmethod
    def operate(self) -> int: ...


class BinaryOp(Operation):
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right


class Mul(BinaryOp):
    def operate(self):
        return self.left * self.right


def matching_strings() -> list[str]:
    return re.findall(PATTERN, load_input())


def operation_list(matching: list[str]) -> list[Operation]:
    return list(map(into_operation, matching))


OPERATION_MAP: dict[str, BinaryOp] = {"mul": Mul}


def into_operation(string: str) -> Operation:
    instruction_string, rest = string.split("(")
    operator = OPERATION_MAP.get(instruction_string)
    if not operator:
        raise ValueError(f"invalid operator {string}")
    operands = rest[:-1]
    left, right = operands.split(",")
    left, right = int(left), int(right)
    return operator(left, right)


def main():
    print(sum(op.operate() for op in operation_list(matching_strings())))


main()
