def zeros_last(numbers: list) -> list:
    if numbers.count(0) == 0:
        return sorted(numbers)
    else:
        return [num for num in numbers if num != 0] + [0] * numbers.count(0)


if __name__ == "__main__":
    print(zeros_last([2, 1, 4, 7, 6]))
    print(zeros_last([1, 4, 6, 0, 7, 0, 9]))
