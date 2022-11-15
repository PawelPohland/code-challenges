def biggest_odd(digits: str) -> int:
    return max([int(digit) for digit in digits if int(digit) % 2 == 1])


if __name__ == "__main__":
    print(biggest_odd("23569"))
