# exercise 5


def calculateOperation(expression):
    for char in expression:
        if not char.isdigit():
            operator = char
            break
    expression = expression.split(operator)
    operating1 = int(expression[0])
    operating2 = int(expression[1])

    if operator == "+":
        return operating1 + operating2
    elif operator == "-":
        return operating1 + operating2
    elif operator == "*":
        return operating1 * operating2
    elif operator == "/":
        if operating2 == 0:
            print("Divide by zero")
            return None
        else:
            return operating1 / operating2
    elif operator == "%":
        return operating1 % operating2
    elif operator == "^":
        return operating1**operating2
    else:
        print("Invalid Operator")
        return None


exp = "23+13"
print(calculateOperation(exp))
