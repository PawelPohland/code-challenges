def register_check(register : dict) -> int:
    counter = 0

    for name, presence in register.items():
        if presence == "yes":
            counter += 1
    
    return counter


def register_check2(register : dict) -> int:
    return len([presence for presence in register.values() if presence == "yes"])


def register_check3(register : dict) -> int:
    return list(register.values()).count("yes")


if __name__ == "__main__":
    students = {
        "Michael": "yes",
        "John": "no",
        "Peter": "yes",
        "Mary": "yes"
    }

    print(register_check(students))
    print(register_check2(students))
    print(register_check3(students))