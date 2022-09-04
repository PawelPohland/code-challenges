import string
import re
import os


def strip_punktuation(text):
    punctuation = string.punctuation.replace("\"", "").replace("\'", "")
    pattern = re.compile(r"[%s]" % re.escape(punctuation))
    return pattern.sub("", text).isalpha()


def file_count_words(path):
    path = os.path.expanduser(path)
    words_counter = 0

    if os.path.exists(path):
        with open(path, "rt") as file:
            for line in file.readlines():
                words_counter += len(
                    list(filter(strip_punktuation, line.split())))

    return words_counter


if __name__ == "__main__":
    words_counter = file_count_words("zen_of_python.txt")
    print(words_counter)
