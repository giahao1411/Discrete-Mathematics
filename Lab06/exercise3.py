import math


def isPrime(n):
    if n <= 1:
        return False

    # loop from 2 to sprt(n)
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def printPrime(N):
    primeList = []
    for i in range(N):
        if isPrime(i):
            primeList.append(i)
    return " ".join(map(str, primeList))


print(printPrime(60))
