def get_user_input():
    user_input = input("Enter comma-separated list of numbers: ")

    def is_number(value):
        value = value.strip()

        if len(value) == 0:
            return False

        return value.isdigit()

    return map(lambda value: int(value.strip()), filter(is_number, user_input.split(",")))


def gen_list_tuple1():
    user_input = get_user_input()

    result_list = list(user_input)
    result_tuple = tuple(result_list)

    print(f"List: {result_list}")
    print(f"Tuple: {result_tuple}")


def gen_list_tuple2():
    user_input = get_user_input()

    result_list = []
    result_tuple = ()

    for number in user_input:
        result_list.append(number)
        result_tuple += (number,)

    print(f"List: {result_list}")
    print(f"Tuple: {result_tuple}")


if __name__ == "__main__":
    gen_list_tuple1()
    print()
    gen_list_tuple2()
