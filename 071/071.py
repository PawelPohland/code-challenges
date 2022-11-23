def find_extremes(numbers):
    if len(numbers) < 2:
        return []

    largest = numbers[0]
    smallest = numbers[0]

    for index in range(1, len(numbers)):
        if numbers[index] > largest:
            largest = numbers[index]
        elif numbers[index] < smallest:
            smallest = numbers[index]

    return largest, smallest


def find_extremes2(numbers):
    if numbers:
        return max(numbers), min(numbers)

    return []


if __name__ == "__main__":
    data = [
        [3, 4, 5, 6],
        [-1, -2, -3, -4],
        [0, 0, 0, 0, 0]
    ]

    for numbers in data:
        print(f"{numbers} => {find_extremes(numbers)}")
        print(f"{numbers} => {find_extremes2(numbers)}")
