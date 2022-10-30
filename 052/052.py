def only_floats(a, b) -> int:
    if type(a) == float and type(b) == float:
        return 2
    elif type(a) == float or type(b) == float:
        return 1
    else:
        return 0


def only_floats2(a, b) -> int:
    if isinstance(a, float) and isinstance(b, float):
        return 2
    elif isinstance(a, float) or isinstance(b, float):
        return 1
    else:
        return 0


if __name__ == "__main__":
    data = [(1.618, 3.14), (2.71, 100), (0, 1)]

    for a, b in data:
        print(f"only_floats({a}, {b}) = {only_floats(a, b)}")
        print(f"only_floats2({a}, {b}) = {only_floats2(a, b)}")