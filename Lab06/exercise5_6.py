def GCD(a, b):
    if a == 0:
        return b
    return GCD(b % a, a)


def LCM(a, b):
    return int(a * b / GCD(a, b))


print(GCD(36, 24))
print(LCM(36, 24))
