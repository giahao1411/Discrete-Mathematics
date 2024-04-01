def decimal_to_hex(decimal):
    hexadecimal = ""
    precision = 10

    for _ in range(precision):
        decimal *= 16
        integer_part = int(decimal)
        hexadecimal += hex(integer_part)[2:]
        decimal -= integer_part
        if decimal == 0:
            break
    return hexadecimal.upper()


print(decimal_to_hex(12))
