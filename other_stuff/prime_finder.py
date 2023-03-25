import math


def prime_finder(upper_limit):
    primes = [2, 3, 5, 7, 11]

    for number in range(13, upper_limit + 1, 2):
        if all([number % prime != 0 for prime in primes if prime < math.floor(math.sqrt(number)) + 1]):
            primes.append(number)
            print(number)

    return primes
