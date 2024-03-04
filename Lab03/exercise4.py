# TODO: implement the rest of the function
def formalConvertPQ(S):
    # split expression
    exp = S.split(",")
    # For all case
    if "For all" in exp[0]:
        D = exp[0][len("For all") + 1 :]
        exp_2 = exp[1].split(" then")
        P = exp_2[0][len("if they ") + 1 :]
        Q = exp_2[1][len("they ") + 1 :]
        F = "For all x in D, P(x) -> Q(x)"
    elif "Exist" in exp[0]:
        D = exp[0][len("Exist") + 1 :]
        exp_2 = exp[1].split(" but")
        exp_3 = exp_2[0].split(" ")
        P = ""
        for i in range(2, len(exp_3)):
            P = P + exp_3[i] + " "
        P = P.rstrip()
        Q = exp_2[1][1:]
        F = "Exist D such that P(x) -> Q(x)"
    elif "For every" in exp[0]:
        D = exp[0][len("For every") + 1 :]
        if len(exp) == 3:
            P = exp[1][len("if they ") + 1 :]
            Q = exp[2][len("they ") + 1 :]
        else:
            exp_2 = exp[1].split("then ")
            P = exp_2[0][len("if they ") + 1 :]
            Q = exp_2[1][len("they ") + 1 :]
        F = "For every x in D, P(x) -> Q(x)"
    return D, P, Q, F


# test cases
sa = "For all people, if they are blond then they are westerners"
sb = "Exist a person, whose hair is black but is a westerner"
sc = "For all students, if they study correctly then they have high score"
sd = "For every mammal, if they live in the sea, they are either dolphins or whales"
se = "For every bird, if they don’t have wings and can swim then they are penguins"
sf = "Exist a bird, who have wing but can’t fly"

print("a.", formalConvertPQ(sa))
print("b.", formalConvertPQ(sb))
print("c.", formalConvertPQ(sc))
print("d.", formalConvertPQ(sd))
print("e.", formalConvertPQ(se))
print("f.", formalConvertPQ(sf))
