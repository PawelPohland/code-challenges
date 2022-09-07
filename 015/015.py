def str_without_even_indices(string):
    if len(string) <= 1:
        return string

    result = []

    for index, character in enumerate(string):
        if index % 2 != 0:
            result.append(character)

    return ''.join(result)


def str_without_even_indices2(string):
    if len(string) <= 1:
        return string

    return string[1::2]


if __name__ == "__main__":
    input_str = ["Coding", "Pizza", "Python", "A", ""]

    for string in input_str:
        print(f"{string} => {str_without_even_indices(string)}")
        print(f"{string} => {str_without_even_indices2(string)}")
