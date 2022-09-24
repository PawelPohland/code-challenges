def largest_at_end(numbers):
    print(numbers)
    max_num = numbers[0]

    # find largest item
    for num in numbers:
        if num > max_num:
            max_num = num

    # count how many times largest item occurs in numbers list
    max_num_count = len(list(filter(lambda num: num == max_num, numbers)))

    # remove each largest item
    for _ in range(max_num_count):
        numbers.remove(max_num)

    # add largest item(s) to the end of numbers list
    numbers += [max_num] * max_num_count

    return numbers


if __name__ == "__main__":
    print(largest_at_end([-1, 2, 200, -1000, 99999, 99999, 3, 4]))
