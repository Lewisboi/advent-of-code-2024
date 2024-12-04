from common import is_safe, count_levels_with_condition, load_levels


def is_safe_with_removal(level: list[int]) -> bool:
    if is_safe(level):
        return True
    for index in range(len(level)):
        level_with_removal = [elem for i, elem in enumerate(level) if i != index]
        if is_safe(level_with_removal):
            return True
    return False


def main():
    print(count_levels_with_condition(load_levels(), is_safe_with_removal))


main()
