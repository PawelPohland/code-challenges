def hello_world(number, hello_num=3, world_num=5):
    if number % (hello_num * world_num) == 0:
        return "HelloWorld"
    elif number % hello_num == 0:
        return "Hello"
    elif number % world_num == 0:
        return "World"

    return number


if __name__ == "__main__":
    numbers = [3, 5, 15, 11]

    for number in numbers:
        print(f"hello_world({number}) => {hello_world(number)}")
