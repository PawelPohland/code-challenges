def gen_dictionary1(max_key):
    dictionary = {}
    
    for k in range(1, max_key + 1, 1):
        dictionary[k] = k * k
    
    return dictionary


# using dictionary comprehension
def gen_dictionary2(max_key):
    dictionary = {key: key * key for key in range(1, max_key + 1, 1)}
    return dictionary;


if __name__ == "__main__":
    max_key = int(input("Enter a number: "))
    
    dictionary = gen_dictionary1(max_key)
    print(dictionary)
    
    dictionary = gen_dictionary2(max_key)
    print(dictionary)