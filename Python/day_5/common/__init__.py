from pathlib import Path

INPUT_FILE_PATH = Path(__file__).parent / "input.txt"
RULE_SEP = "|"
UPDATE_SEP = ","


def load_rules_and_updates() -> tuple[list[int], list[int]]:
    with open(INPUT_FILE_PATH, "r") as input_file:
        rules = []
        updates = []
        current_sep = RULE_SEP
        current_list = rules
        for line in input_file.readlines():
            line = line.strip()
            if line == "":
                current_sep = UPDATE_SEP
                current_list = updates
                continue
            current_list.append([int(num) for num in line.split(current_sep)])
        return rules, updates
