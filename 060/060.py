def string_range(number: int) -> str:
    output = []
    for n in range(0, number, 1):
        output.append(str(n))

    return ".".join(output)


def string_range2(number: int) -> str:
    return ".".join([str(n) for n in range(number)])


if __name__ == "__main__":
    print(string_range(number=6))
    print(string_range2(number=6))
