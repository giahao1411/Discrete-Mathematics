def convertbase(a, base1, base2):
    # Convert list 'a' from base 'base1' to base 10
    decimal_value = 0
    for digit in a:
        decimal_value = decimal_value * base1 + digit

    # Convert decimal value to base 'base2'
    result = []
    while decimal_value > 0:
        remainder = decimal_value % base2
        result.insert(0, remainder)
        decimal_value //= base2

    return result


print(convertbase([1, 1, 1], 10, 16))
