def count_dots(text: str) -> int:
    return text.count(".")


def count_dots2(text: str) -> int:
    return len(list(filter(lambda char: char == ".", text)))


def count_dots3(text: str) -> int:
    return len(text.split(".")) - 1


if __name__ == "__main__":
    input = ["p.y.t.h.o.n.", "pyt.h.on", "python"]

    for text in input:
        print(f"{text} => {count_dots(text)}")
        print(f"{text} => {count_dots2(text)}")
        print(f"{text} => {count_dots3(text)}")
