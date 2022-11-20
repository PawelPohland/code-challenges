def swap_values(numbers: list) -> list:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    return numbers


def swap_values2(numbers: list) -> list:
    return [numbers[-1], *numbers[1:-1], numbers[0]]


if __name__ == "__main__":
    numbers = [2, 4, 6, 7, 7]

    print(numbers)

    print(swap_values(numbers))
    print(swap_values2(numbers))
