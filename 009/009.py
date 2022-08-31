def move_zeros_to_end(numbers):
    for index in range(len(numbers)):
        if numbers[index] == 0:
            numbers.append(0)
            numbers.remove(0)

    return numbers


if __name__ == "__main__":
    input = [
        [1, 0, 1, 2, 0, 1, 3],
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]
    ]

    for numbers in input:
        print(f"{numbers} => {move_zeros_to_end(numbers)}")
