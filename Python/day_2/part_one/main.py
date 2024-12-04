from common import load_levels, is_safe, count_levels_with_condition


def count_safe_levels(levels: list[list[int]]) -> int:
    return sum(is_safe(lv) for lv in levels)


def main():
    print(count_levels_with_condition(load_levels(), is_safe))


main()
