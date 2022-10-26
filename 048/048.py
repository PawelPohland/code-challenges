def divide_or_square(number: int | float) -> int | float:
    if number % 5 == 0:
        return round(number ** 0.5, 2)

    return number % 5


def divide_or_square2(number: int | float) -> int | float:
    return round(number ** 0.5, 2) if number % 5 == 0 else number % 5


if __name__ == "__main__":
    print(f"divide_or_square(10) = {divide_or_square(10)}")
    print(f"divide_or_square2(10) = {divide_or_square2(10)}")
