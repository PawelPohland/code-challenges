def getNumbers1(min_num = 2000, max_num = 3200):
    result = []
    
    for number in range(min_num, max_num + 1):
        if number % 7 == 0 and number % 5 != 0:
            result.append(number)
    
    return ",".join(map(str, result));

# using list comprehension:
def getNumbers2(min_num = 2000, max_num = 3200):
    result = [number for number in range(min_num, max_num + 1) if number % 7 == 0 and number % 5 != 0];
    return ",".join(map(str, result));

if __name__ == "__main__":
    print(getNumbers1());
    print();
    print(getNumbers2());