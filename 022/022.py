import re


def replace_commas(string):
    return string.replace(",", ".")


def replace_commas2(string):
    return '.'.join(string.split(","))


def replace_commas3(string):
    result = ""

    for char in string:
        if char != ",":
            result += char
        else:
            result += "."

    return result


def replace_commas4(string):
    regexp = re.compile(f",", flags=re.IGNORECASE)
    return regexp.sub(".", string)


if __name__ == "__main__":
    input = ["Hello, World!", "3,456,344"]

    for string in input:
        print(f"{string} => {replace_commas(string)}")
        print(f"{string} => {replace_commas2(string)}")
        print(f"{string} => {replace_commas3(string)}")
        print(f"{string} => {replace_commas4(string)}")
