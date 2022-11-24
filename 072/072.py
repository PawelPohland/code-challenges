def log_numbers(number, max_number):
    num = number

    while num <= max_number:
        print(num)
        num += 1


def log_numbers2(number, max_number):
    for num in range(number, max_number + 1):
        print(num)


def log_numbers3(number, max_number):
    if (number > max_number):
        return

    print(number)

    log_numbers(number + 1, max_number)


if __name__ == "__main__":
    log_numbers(50, 60)
