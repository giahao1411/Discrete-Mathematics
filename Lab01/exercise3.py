# exercise 3


def sumN(n):
    sum = 0
    if n >= 0:
        for i in range(0, n + 1):
            sum = sum + i
    else:
        for i in range(n, 1):
            sum = sum + i
    return sum


print(sumN(2))
print(sumN(-5))
