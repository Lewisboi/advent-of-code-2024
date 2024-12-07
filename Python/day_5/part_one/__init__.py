from abc import ABC, abstractmethod


class Rule(ABC):
    @abstractmethod
    def is_satisfied_by(self, input_list: list[int]) -> bool: ...
    @abstractmethod
    def enforce(self, input_list: list[int]) -> list[int]: ...


class PrecedenceRule(Rule):
    def __init__(self, pre: int, post: int):
        self.pre = pre
        self.post = post

    def is_satisfied_by(self, input_list: list[int]) -> bool:
        both_present = self.pre in input_list and self.post in input_list
        if not both_present:
            return True
        return input_list.index(self.pre) < input_list.index(self.post)

    def enforce(self, input_list: list[int]) -> list[int]:
        input_list = list(input_list)
        if not self.is_satisfied_by(input_list):
            try:
                pre_index = input_list.index(self.pre)
                post_index = input_list.index(self.post)
                input_list[pre_index] = self.post
                input_list[post_index] = self.pre
            except ValueError as e:
                raise e
        return input_list


class CompositeRule(Rule):
    def __init__(self):
        self._rules: list[Rule] = []

    def add_rule(self, rule: Rule) -> None:
        self._rules.append(rule)

    def is_satisfied_by(self, input_list: list[int]) -> bool:
        return all(r.is_satisfied_by(input_list) for r in self._rules)

    def enforce(self, input_list: list[int]) -> list[int]:
        transformed_list = input_list
        while not self.is_satisfied_by(transformed_list):
            for rule in self._rules:
                transformed_list = rule.enforce(transformed_list)
        return transformed_list
