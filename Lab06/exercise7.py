def convertDecToBin(n):
    if n == 0:
        return n
    return n % 2 + 10 * (convertDecToBin(int(n // 2)))


print(convertDecToBin(10))
