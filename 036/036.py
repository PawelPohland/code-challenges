def count_repeated(string):
    repeated = {}

    for char in string:
        if char in repeated.keys():
            repeated[char] += 1
        else:
            repeated[char] = 1

    repeated = sorted([key for key, value in repeated.items() if value > 1])

    print(f"Total number of repeated characters: {len(repeated)}")
    if repeated:
        print(f"{' '.join(repeated)}")
    else:
        print("None")


if __name__ == "__main__":
    input = ["Hello", "Corporation", "Python"]

    for word in input:
        count_repeated(word)
