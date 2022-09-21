def largest_num(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


def largest_num2(numbers):
    return max(numbers)


if __name__ == "__main__":
    input = [
        [1, 2, 3, 200, 4, 5, 6, 7, -1000, 8, 9, 10],
        [1, 2, 3, 4, 5, 800]
    ]

    for numbers in input:
        print(f"largest_num([{numbers}]) = {largest_num(numbers)}")
        print(f"largest_num([{numbers}]) = {largest_num2(numbers)}")
