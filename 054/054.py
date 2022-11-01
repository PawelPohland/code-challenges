def word_index(words: list) -> int:
    longest_word_index = 0
    longest_word = 0

    for index, word in enumerate(words):
        if len(word) > longest_word:
            longest_word_index = index
            longest_word = len(word)

    return longest_word_index


if __name__ == "__main__":
    print(word_index(["Hate", "remorse", "vengeance"]))
    print(word_index(["Love", "Hate"]))
