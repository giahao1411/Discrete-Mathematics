def decimal_faction_to_binary(decimal):
    binary = ""
    precision = 10

    for _ in range(precision):
        decimal *= 2
        if decimal >= 1:
            binary += "1"
            decimal -= 1
        else:
            binary += "0"
        if decimal == 0:
            break
    return binary


print(decimal_faction_to_binary(0.625))
