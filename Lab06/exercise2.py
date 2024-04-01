def primeFact(n):
    primeFactList = []
    i = 2

    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            primeFactList.append(i)
    if n > 1:
        primeFactList.append(n)
    return primeFactList


print(primeFact(60))
print(primeFact(315))
