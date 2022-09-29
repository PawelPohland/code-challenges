def to_target(numbers, target):
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (numbers[i], numbers[j])


def to_target2(numbers, target):
    for number in numbers:
        diff = target - number
        if diff in numbers:
            return (number, diff)


if __name__ == "__main__":
    input = [
        {"numbers": [1, 9, 20, 15], "target": 35},
        {"numbers": [0, 1, 5, 9, 81, 20, 35, 46, 91], "target": 10},
        {"numbers": [10, 20, 30, 40, 50, 60, 70, 80], "target": 100}
    ]

    for data in input:
        print(f"to_target({data['numbers']}, target = {data['target']}) = " +
              f"{to_target(data['numbers'], data['target'])} " +
              f"{to_target2(data['numbers'], data['target'])}")
