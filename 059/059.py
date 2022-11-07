def zeroed_code(numbers: list) -> list:
    return [0, *numbers[1:-1], 0]


def zeroed_code2(numbers: list) -> list:
    numbers[0] = 0
    numbers[-1] = 0

    return numbers


if __name__ == "__main__":
    numbers = [2, 5, 7, 8, 9]

    print(zeroed_code(numbers))
    print(zeroed_code2(numbers))
