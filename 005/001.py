def reverse_words(text):
    result = []

    for word in text.split():
        result.append(''.join((map(lambda letter: letter.upper()
                                   if letter.islower() else letter.lower(), word[::-1]))))

    return ' '.join(result)


def reverse_words2(text):
    result = []

    for word in text.split():
        result.append(''.join(reversed(word.swapcase())))

    return ' '.join(result)


if __name__ == "__main__":
    input = ["Hello World", "Python is Awesome"]

    for text in input:
        print(f"{text} => {reverse_words(text)}")
        print(f"{text} => {reverse_words2(text)}")
