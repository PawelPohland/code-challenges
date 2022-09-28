def sum_of_odd_even(*numbers):
    sum_even = 0
    sum_odd = 0

    for num in numbers:
        if num % 2 == 0:
            sum_even += num
        else:
            sum_odd += num

    return sum_odd, sum_even


if __name__ == "__main__":
    input = [
        [2, 3, 6, 7, 8, 9],
        [-3, -4, -8, -5, -2, -6]
    ]

    for numbers in input:
        odd, even = sum_of_odd_even(*numbers)

        print(f"Numbers: {numbers}")
        print(f"Sum of odd numbers: {odd}")
        print(f"Sum of even numbers: {even}")
