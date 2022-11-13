def odd_even(numbers: list) -> int:
    max_even = 0
    max_odd = 0

    for number in numbers:
        if number % 2 == 0:
            # even
            if number > max_even:
                max_even = number
        else:
            # odd
            if number > max_odd:
                max_odd = number

    print(f"{max_even} - {max_odd} = {max_even - max_odd}")

    return max_even - max_odd


if __name__ == "__main__":
    odd_even([1, 2, 4, 6])
