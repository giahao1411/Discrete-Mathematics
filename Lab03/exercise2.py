def formalConvert(S):
    # split the expression
    exp = S.split(",")

    # For all case
    if "For all" in exp[0]:
        D = exp[0][len("For all") + 1 : len(exp[0])]
        P = exp[1][len("they ") + 1 : len(exp[1])]
        F = "For all x in D, P(X)"
    # Exist case
    elif "Exist" in exp[0]:
        D = exp[0][len("Exist") + 1 : len(exp[0])]
        P = exp[1][len("who ") + 1 : len(exp[1])]
        F = "Exist D such that D is P(x)"
    # There is case
    elif "There is" in exp[0]:
        D = exp[0][len("There is") + 1 : len(exp[0])]
        P = exp[1][len("it ") + 1 : len(exp[1])]
        F = "There is D such that P(x)"
    return D, P, F


# Test cases
sa = "For all fishes, they need water to survive"
sb = "Exist a person, who is left handed"
sc = "Exist an employee in the company, who is late to work everyday"
sd = "For all fishes in this pond, they are Koi fish"
se = "There is at least one creature in the ocean, it can live on land"

# results
print("a.", formalConvert(sa))
print("b.", formalConvert(sb))
print("c.", formalConvert(sc))
print("d.", formalConvert(sd))
print("e.", formalConvert(se))
