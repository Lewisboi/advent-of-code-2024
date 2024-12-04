from common import load_lists


def frequency(number: int, list_of_numbers: list[int]) -> int:
    return list_of_numbers.count(number)


def add_frequencies(source_list: list[int], comparison_list: list[int]) -> int:
    return sum(a * frequency(a, comparison_list) for a in source_list)


def main():
    a, b = load_lists()
    print(add_frequencies(a, b))


main()
