import itertools


def implies(a, b):
    return (not a) or b


def checkValid(value):
    if value == True:
        print("VALID")
    else:
        print("INVALID")


table = list(itertools.product([False, True], repeat=4))

# p → r
# ¬p → q
# q → s
# ∴ ¬r → s
for item in table:
    # initiate variables
    p, q, r, s = item

    # evaluate expression
    premise1 = implies(p, r)
    premise2 = implies((not p), q)
    premise3 = implies(q, s)

    # evaluate conclusion
    conclusion = implies((not r), s)

    # check if valid
    if not (premise1 and premise2 and premise3) or conclusion:
        break
    else:
        check = True
        checkValid(check)
