def count_words(text):
    return len(text.split(" "))


def count_words_detailed(text):
    return len(list(filter(lambda string: string.isalpha(), text.split())))


if __name__ == "__main__":
    text = "This text contains 5 words"
    print(text)
    print(f"count_words: {count_words(text)}")
    print(f"count_words_detailed: {count_words_detailed(text)}")
