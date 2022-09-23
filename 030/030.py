def sum_primes(num):
    primes = []

    for number in range(2, num + 1, 1):
        is_prime = True
        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(number)

    return primes, sum(primes)


if __name__ == "__main__":
    max_number = 100
    primes = sum_primes(max_number)

    print(f"Prime numbers [1, {max_number}]:")
    print(f"{','.join(map(str, primes[0]))}")
    print(f"Sum = {primes[1]}")
