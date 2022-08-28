def reverse_key_values(dictionary):
    result = {}

    for key, value in dictionary.items():
        result[str(value)] = key

    return result


def reverse_key_values2(dictionary):
    return dict(list(map(lambda item: (str(item[1]), item[0]), dictionary.items())))


if __name__ == "__main__":
    dictionary = {
        "apple": "fruit",
        "dog": "animal",
        "ford": "brand",
        "domino's": "pizza"}

    print(dictionary)

    print(reverse_key_values(dictionary))
    print(reverse_key_values2(dictionary))
