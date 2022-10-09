def multiply(numbers, quantity):
    product = 1

    for index in range(0, quantity):
        product *= numbers[index]
    
    return product


def multiply2(numbers, quantity):
    if (quantity <= 0):
        return 1
    
    return multiply(numbers, quantity - 1) * numbers[quantity - 1]


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    print(f"multiply = {multiply(numbers, 3)}")
    print(f"multiply = {multiply2(numbers, 3)}")