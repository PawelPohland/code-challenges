def equal_strings(str1: str, str2: str) -> bool:
    for char in str1:
        if char not in str2:
            return False

    for char in str2:
        if char not in str1:
            return False

    return len(str1) == len(str2)


def equal_strings2(str1: str, str2: str) -> bool:
    if len(str1) == len(str2):
        return len(set(str1).difference(set(str2))) == 0

    return False


def equal_strings3(str1: str, str2: str) -> bool:
    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1 == str2


if __name__ == "__main__":
    input = [("love", "evol"), ("abcdef", "abcgef")]

    for str1, str2 in input:
        print(f"'{str1}' and '{str2}' => {equal_strings(str1, str2)}")
        print(f"'{str1}' and '{str2}' => {equal_strings2(str1, str2)}")
        print(f"'{str1}' and '{str2}' => {equal_strings3(str1, str2)}")
