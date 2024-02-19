# exercise 6


def calculateOperation(expression):
    operator = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        "/": lambda x, y: x / y if y != 0 else None,
        "%": lambda x, y: x % y,
        "^": lambda x, y: x**y,
    }

    for char in expression:
        if not char.isdigit():
            key = char
            break
    expression = expression.split(key)
    operating1 = int(expression[0])
    operating2 = int(expression[1])

    if key in operator:
        return operator[key](operating1, operating2)
    else:
        print("Invalid operator")
        return None


exp = "213-10"
print(calculateOperation(exp))
