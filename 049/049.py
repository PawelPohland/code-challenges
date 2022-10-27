def longest_value(dictionary):
    items = [(value, len(value)) for value in dictionary.values()]
    items = sorted(items, key=lambda item: item[1], reverse=True)

    return items[0][0]


def longest_value2(dictionary):
    return max(dictionary.values(), key=len)


if __name__ == "__main__":
    longest_value({'fruit': 'apple', 'color': 'green'})
    longest_value({'fruit': 'apple', 'color': 'green', 'car': 'Ford Focus'})

    longest_value2({'fruit': 'apple', 'color': 'green'})
    longest_value2({'fruit': 'apple', 'color': 'green', 'car': 'Ford Focus'})
