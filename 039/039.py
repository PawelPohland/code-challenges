def sum_digits(number, divider=10):
    digits = []

    while number != 0:
        digit = number % divider
        digits.append(digit)

        number = number // divider

    return digits[::-1], sum(digits)


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    digits, sum_of_digits = sum_digits(number)

    str_digits = " + ".join(map(lambda digit: str(digit), digits))

    print(
        f"Sum of digits of number {number} is: {str_digits} = {sum_of_digits}")
