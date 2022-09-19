def ends_with_suffix(string, suffix):
    return string[-len(suffix):] == suffix


def ends_with_suffix2(string, suffix):
    return string.endswith(suffix)


if __name__ == "__main__":
    input = [("Hello", "ello"), ("Coding", "eng"), ("Nora", "rowing")]

    for string, suffix in input:
        print(f"{string} ends with {suffix} : {ends_with_suffix(string, suffix)}")
        print(f"{string} ends with {suffix} : {ends_with_suffix2(string, suffix)}")
