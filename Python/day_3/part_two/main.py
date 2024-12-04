import re
from enum import Enum
from abc import ABC, abstractmethod
from common import load_input


PATTERN = r"(mul\(-?\d+,-?\d+\)|do\(\)|don't\(\))"


class Conditional(str, Enum):
    DO = "do"
    DONT = "don't"


class Operation(ABC):
    @abstractmethod
    def operate(self) -> int: ...


Instruction = Operation | Conditional


class BinaryOp(Operation):
    def __init__(self, left: int, right: int):
        self.left = left
        self.right = right


class Mul(BinaryOp):
    def operate(self):
        return self.left * self.right


def matching_strings() -> list[str]:
    return re.findall(PATTERN, load_input())


def instruction_list(matching: list[str]) -> list[Instruction]:
    return list(map(into_instruction, matching))


OPERATION_MAP: dict[str, BinaryOp] = {"mul": Mul}


def into_instruction(string: str) -> Instruction:
    instruction_string, rest = string.split("(")
    operator = OPERATION_MAP.get(instruction_string)
    if operator:
        operands = rest[:-1]
        left, right = operands.split(",")
        left, right = int(left), int(right)
        return operator(left, right)
    return Conditional(instruction_string)


class SwitchableOperation(Operation):
    def __init__(self, op: Operation | None = None):
        self.op = op
        self.enabled = True

    def operate(self):
        if not self.enabled:
            return 0
        return self.op.operate()

    def set_operation(self, op: Operation):
        self.op = op

    def switch(self):
        self.enabled = not self.enabled

    def switch_on(self):
        self.enabled = True

    def switch_off(self):
        self.enabled = False


def main():
    matching = matching_strings()
    instructions = instruction_list(matching)
    switchable = SwitchableOperation()
    count = 0
    for ins in instructions:
        if isinstance(ins, Operation):
            switchable.set_operation(ins)
            adds = switchable.operate()
            count += adds
        else:
            match ins:
                case Conditional.DONT:
                    switchable.switch_off()
                case Conditional.DO:
                    switchable.switch_on()
    print(count)


main()
