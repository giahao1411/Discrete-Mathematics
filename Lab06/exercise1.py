import math


def isPrime(n):
    if n <= 1:
        return True
    
    # loop from 2 to sprt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def nextPrime(n):
    # base case
    if n <= 1:
        return 2

    prime = n
    found = False

    # loop continuously until found prime greater than n
    while not found:
        prime += 1
        if isPrime(prime):
            found = True
    return prime


print(nextPrime(3))
print(nextPrime(8))
