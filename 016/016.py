def count_primes(number):
    primes_counter = 0

    for num in range(2, number):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes_counter += 1

    return primes_counter


def count_primes2(number):
    primes_counter = 0
    primes = []

    for num in range(2, number):
        is_prime = True

        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            primes.append(num)
            primes_counter += 1

    return primes_counter, primes


if __name__ == "__main__":
    print(count_primes(10), count_primes2(10))
