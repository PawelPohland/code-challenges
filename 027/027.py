def sum_first_100_odd_nums():
    # first generate 100 odd numbers
    odd_numbers = [odd_num for odd_num in range(1, 200, 2)]

    # and then calculate the sum
    return odd_numbers, sum(odd_numbers)


def sum_first_100_odd_nums2():
    odd_numbers = []
    odd_counter = 0

    number = 1
    total = 0

    while odd_counter != 100:
        if number % 2 != 0:
            odd_counter += 1
            total += number
            odd_numbers.append(number)

        number += 1

    return odd_numbers, total


if __name__ == "__main__":
    odd_numbers, total = sum_first_100_odd_nums()
    print(odd_numbers)
    print(f"Sum = {total}, {len(odd_numbers)}")

    odd_numbers, total = sum_first_100_odd_nums2()
    print(odd_numbers)
    print(f"Sum = {total}, {len(odd_numbers)}")
