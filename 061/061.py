def dict_of_names(names: list) -> dict:
    starts_with_s = {}
    for name in names:
        if name.startswith("S") and not starts_with_s.get(name):
            starts_with_s[name] = names.count(name)

    return starts_with_s


def dict_of_names2(names: list) -> dict:
    return {name: names.count(name) for name in names if name.startswith("S")}


def dict_of_names3(names: list) -> dict:
    starts_with_s = []
    for name in names:
        if name.startswith("S"):
            starts_with_s.append(name)

    from collections import Counter
    return Counter(starts_with_s)


if __name__ == "__main__":
    names = ["Joseph", "Nathan", "Sasha", "Kelly", "Muhammad",
             "Jabulani", "Sera", "Patel", "Sera"]

    print(dict_of_names(names))
    print(dict_of_names2(names))
    print(dict_of_names3(names))
