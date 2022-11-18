def convert_numbers(numbers: list) -> list:
    output_numbers = []

    for number in numbers:
        number_s = str(number)
        number_x = []
        for index, digit in enumerate(number_s[::-1]):
            number_x.append(digit)
            if (index + 1) % 3 == 0:
                number_x.append(",")

        converted_num = "".join(number_x[::-1])
        print(f"{number_s} => {converted_num}")

        output_numbers.append(converted_num)

    return output_numbers


def convert_numbers2(numbers: list) -> list:
    output_numbers = []

    for number in numbers:
        output_numbers.append(f"{number:,}")

    return output_numbers


if __name__ == "__main__":
    print(convert_numbers(
        [1000000, 2356989, 2354672, 9878098, 1000000000000000]))
    print(convert_numbers2(
        [1000000, 2356989, 2354672, 9878098, 1000000000000000]))
