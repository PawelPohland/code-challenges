def duplicate_finder(numbers):
    duplicated = numbers[0]

    for index in range(1, len(numbers)):
        if duplicated == numbers[index]:
            return duplicated


if __name__ == "__main__":
    input = [
        [900, 9000, 900, 8000, 356, 786],
        [1, 85, 55, 654, 35, 78, 1]
    ]

    for numbers in input:
        print(f"duplicate_finder({numbers}) => {duplicate_finder(numbers)}")
