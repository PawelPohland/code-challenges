def sum_even(number):
    total = 0

    for num in range(1, number + 1):
        total += num if num % 2 == 0 else 0

    return total


def sum_even2(number):
    return sum([num for num in range(1, number + 1) if num % 2 == 0])


if __name__ == "__main__":
    num = 100
    print(f"Sum of even numbers [1, {num}] = {sum_even(num)}")
    print(f"Sum of even numbers [1, {num}] = {sum_even2(num)}")
