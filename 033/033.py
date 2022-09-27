from string import ascii_lowercase


def contains_all_alphabet_letters(string):
    for letter in ascii_lowercase:
        if letter not in string.lower():
            return False

    return True


def contains_all_alphabet_letters2(string):
    string_set = set(string.lower().replace(" ", ""))
    return string_set == set(ascii_lowercase)


if __name__ == "__main__":
    input = [
        "abcdefghijklmnopqrstuvwxyz",
        "The quick brown fox jumps over the lazy dog",
        "Hello"
    ]

    for string in input:
        print(f"{string} => {contains_all_alphabet_letters(string)}")
        print(f"{string} => {contains_all_alphabet_letters2(string)}")   