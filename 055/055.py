def check_duplicates(lst: list) -> list | str:
    duplicates = []

    for i, s in enumerate(lst):
        if s in lst[i + 1:]:
            duplicates.append(s)

    return "No duplicats" if len(duplicates) == 0 else duplicates


if __name__ == "__main__":
    print(check_duplicates(['apple', 'orange', 'banana', 'apple']))
    print(check_duplicates(['Yoda', 'Moses', 'Josua', 'Mark']))
