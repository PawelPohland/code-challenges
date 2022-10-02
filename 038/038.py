def count_number(number, list):
    counter = 0

    for num in list:
        if num == number:
            counter += 1

    return counter


if __name__ == "__main__":
    print(
        f"count_number(4, [1, 6, 7, 4, 3, 4]) = {count_number(4, [1, 6, 7, 4, 3, 4])}")
