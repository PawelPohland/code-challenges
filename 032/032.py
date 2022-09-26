def str_reverse(string):
    reversed_chars = []

    for index in range(len(string) - 1, -1, -1):
        reversed_chars.append(string[index])

    return ''.join(reversed_chars)


def str_reverse2(string):
    return string[::-1]


def str_reverse3(string):
    lst = list(string)
    lst.reverse()

    return ''.join(lst)


def str_reverse4(string):
    return ''.join(reversed(string))


if __name__ == "__main__":
    text = "This is a string!"
    print(f"{text} REVERSED {str_reverse(text)}")
    print(f"{text} REVERSED {str_reverse2(text)}")
    print(f"{text} REVERSED {str_reverse3(text)}")
    print(f"{text} REVERSED {str_reverse4(text)}")
