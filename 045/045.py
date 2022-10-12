def sort_alpha(string):
    words = string.lower().split(" ")
    letters_sorted = []

    for word in words:
        letters_sorted.append("".join(sorted(word)))

    return " ".join(letters_sorted)


if __name__ == "__main__":
    print(sort_alpha("Hello World"))
    print(sort_alpha("Wonderful World"))
