def lowercase_letters(names : list) -> tuple:
    lowercase_names = ()
    
    for name in names:
        if name.islower():
            lowercase_names += (name,)
    
    return sorted(lowercase_names, reverse=True)


def lowercase_letters2(names : list) -> tuple:
    return sorted(tuple(filter(lambda name: name.islower(), names)), reverse=True)


if __name__ == "__main__":
    names = ["kerry", "dickson", "John", "Mary", "carol", "Rose", "adam"]

    print(lowercase_letters(names))
    print(lowercase_letters2(names))