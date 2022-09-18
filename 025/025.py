def starts_with_prefix(string, prefix):
    return string[:len(prefix)] == prefix


def starts_with_prefix2(string, prefix):
    return string.startswith(prefix)


if __name__ == "__main__":
    input = [("Hello", "He"), ("Coding", "Con"), ("Nora", "Circum")]

    for string, prefix in input:
        print(f"{string} starts with {prefix} : {starts_with_prefix(string, prefix)}")
        print(f"{string} starts with {prefix} : {starts_with_prefix2(string, prefix)}")
