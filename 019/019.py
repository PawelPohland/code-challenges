def remove_duplicates(numbers):
    unique_numbers = []

    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)

    return sorted(unique_numbers)


def remove_duplicates2(numbers):
    return sorted(list(set(numbers)))


if __name__ == "__main__":
    input = [
        [1, 1, 2, 22, 3, 3, 3, 4, 5],
        [900, 9000, 900, 8000, 356, 786]
    ]

    for numbers in input:
        print(f"remove_duplicates({numbers}) => {remove_duplicates(numbers)}")
