# define a function to calculate the implies
def implies(a, b):
    if a:
        return b
    else:
        return True


# a - logical implies
def lLImplies(p, q):
    truths = zip(p, q)
    print("p \t q \t p implies q")

    for i in truths:
        if i[0]:
            p = True
        else:
            p = False
        if i[1]:
            q = True
        else:
            q = False
        print(p, "\t", q, "\t", implies(p, q))


# b - logical and
def lLAnd(p, q):
    truths = zip(p, q)
    print("p \t q \t p and q")

    for i in truths:
        if i[0]:
            p = True
        else:
            p = False
        if i[1]:
            q = True
        else:
            q = False
        print(p, "\t", q, "\t", p and q)


# c - logical or
def lLOr(p, q):
    truths = zip(p, q)
    print("p \t q \t p or q")

    for i in truths:
        if i[0]:
            p = True
        else:
            p = False
        if i[1]:
            q = True
        else:
            q = False
        print(p, "\t", q, "\t", p or q)


# define a function to calculate the exclusive or
def Xor(p, q):
    return (p and not q) or (not p and q)


# d - logical xor
def lLXor(p, q):
    truths = zip(p, q)
    print("p \t q \t p xor q")

    for i in truths:
        if i[0]:
            p = True
        else:
            p = False
        if i[1]:
            q = True
        else:
            q = False
        print(p, "\t", q, "\t", Xor(p, q))


# e - logical not
def lLNot(p):
    print("Not p")
    for i in p:
        if i == True:
            p = False
        else:
            p = True
        print(p)


# define a function to calculate the equivalent
def Equivalent(p, q):
    return implies(p, q) and implies(q, p)


# f - logical equivalent
def lLEquivalent(p, q):
    truths = zip(p, q)
    print("p \t q \t p equivalent q")

    for i in truths:
        if i[0]:
            p = True
        else:
            p = False
        if i[1]:
            q = True
        else:
            q = False
        print(p, "\t", q, "\t", Equivalent(p, q))


# test cases
p = [True, True, False, False]
q = [True, False, True, False]

lLImplies(p, q)
print("---------------------------")
lLAnd(p, q)
print("---------------------------")
lLOr(p, q)
print("---------------------------")
lLXor(p, q)
print("---------------------------")
lLNot(p)
print("---------------------------")
lLEquivalent(p, q)
