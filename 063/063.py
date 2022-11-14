def prime_numbers(number: int) -> list:
    primes = []

    for n in range(2, number + 1, 1):
        for dividor in range(2, n, 1):
            if n % dividor == 0:
                break
        else:
            primes.append(n)

    return primes


if __name__ == "__main__":
    number = int(input("Enter a number: "))
    print(prime_numbers(number))
