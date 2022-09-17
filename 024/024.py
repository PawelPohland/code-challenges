def string_letters_occurance(string):
    letters_occurance = {}

    for letter in string:
        if letter.isalpha():
            if letter in letters_occurance.keys():
                letters_occurance[letter] += 1
            else:
                letters_occurance[letter] = 1

    return letters_occurance


if __name__ == "__main__":
    string = "Special cases aren't special enough to break the rules."

    print(f"Letters orrucance in '{string}':")
    print(string_letters_occurance(string))
