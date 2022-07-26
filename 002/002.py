# n! = 1 * 2 * ... * (n - 1) * n
def factorial1(number):
    result = 1
    
    for i in range(1, number + 1):
        result *= i
    
    return result

# n! = 1 * 2 * ... * (n - 2) * (n-1)! * n
def factorial2(number):
    if number <= 1:
        return 1
    
    return factorial2(number - 1) * number

# using generator
def factorial3(number):
    result = 1
    
    for i in range(1, number + 1):
        result *= i
        yield result


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    
    print(f"{number}! = {factorial1(number)}")
    print(f"{number}! = {factorial2(number)}")
    
    factorials = [num for num in factorial3(number)]
    print(f"{number}! = {factorials[-1]}")