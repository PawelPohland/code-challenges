def add(numbers, quantity):
    total = 0

    for index in range(0, quantity):
        total += numbers[index]
    
    return total


def add2(numbers, quantity):
    if (quantity <= 0):
        return 0
    
    return add2(numbers, quantity - 1) + numbers[quantity - 1]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    print(f"sum = {add(numbers, 5)}")
    print(f"sum = {add2(numbers, 5)}")