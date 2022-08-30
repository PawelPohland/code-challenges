def sum_missing_nums(numbers):
    total = 0
    index = 0

    while index < len(numbers):
        first_num = numbers[index]

        index += 1

        if index >= len(numbers):
            break

        second_num = numbers[index]

        for num in range(first_num + 1, second_num, 1):
            total += num

    return total


def sum_missing_nums2(numbers):
    total = 0

    for num in range(min(numbers), max(numbers)):
        if num not in numbers:
            total += num

    return total


if __name__ == "__main__":
    input = [
        [2, 8, 9, 11, 13],
        [8, 10, 12],
        [1, 2, 3, 4, 5, 6, 7]
    ]

    for numbers in input:
        print(f"sum_missing_nums([{numbers}]) = {sum_missing_nums(numbers)}")
        print(f"sum_missing_nums([{numbers}]) = {sum_missing_nums2(numbers)}")