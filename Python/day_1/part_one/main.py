from common import load_lists


def add_absolute_distances(list_a: list[int], list_b: list[int]) -> int:
    return sum(abs(a - b) for a, b in zip(list_a, list_b))


def main():
    a, b = load_lists()
    print(add_absolute_distances(a, b))


main()
