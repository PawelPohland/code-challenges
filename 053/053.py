def convert_add(lst: list) -> int:
    return sum(list(map(lambda s: int(s), lst)))


def convert_add2(lst: list) -> int:
    return sum([int(s) for s in lst])


def convert_add3(lst: list) -> int:
    total = 0

    for s in lst:
        total += int(s)

    return total


if __name__ == "__main__":
    print(convert_add(['1', '3', '5']))
    print(convert_add2(['1', '3', '5']))
    print(convert_add3(['1', '3', '5']))
