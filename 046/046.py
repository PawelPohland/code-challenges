def multiply(items, factor):
    for index, item in enumerate(items):
        items[index] = item * factor

    return items


def multiply2(items, factor):
    return [item * factor for item in items]


if __name__ == "__main__":
    print(multiply([6, 8, 10, 12], 2))
    print(multiply(["a", "b", "c"], 3))

    print(multiply2([6, 8, 10, 12], 2))
    print(multiply2(["a", "b", "c"], 3))
