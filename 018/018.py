def factors_of_num(number):
    factors = []

    for num in range(2, number):
        if number % num == 0:
            factors.append(num)

    factors.append(number)
    return factors


if __name__ == "__main__":
    numbers = [10, 100]

    for number in numbers:
        print(f"factors_of_num({number}) = {factors_of_num(number)}")
