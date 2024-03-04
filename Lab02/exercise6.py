import itertools


def implies(a, b):
    return (not a) or b


def checkValid(value):
    if value == True:
        print("VALID")
    else:
        print("INVALID")


table_4 = list(itertools.product([False, True], repeat=4))
table_5 = list(itertools.product([False, True], repeat=5))
check_a, check_b, check_c, check_d = False, False, False, False


# p → r
# ¬p → q
# q → s
# ∴ ¬r → s
for item in table_4:
    # initiate variables
    p, q, r, s = item

    # evaluate expression
    premise1 = implies(p, r)
    premise2 = implies((not p), q)
    premise3 = implies(q, s)

    # evaluate conclusion
    conclusion = implies((not r), s)

    # check if valid
    if not (premise1 and premise2 and premise3) and conclusion:
        continue
    else:
        check_a = True

# p → (q → r)
# p ∨ s
# t → q
# ¬s
# ∴ ¬r → ¬t
for item in table_5:
    # initiate variables
    p, q, r, s, t = item

    # evaluate expression
    premise1 = implies(p, implies(q, r))
    premise2 = p or s
    premise3 = implies(t, q)
    premise4 = not s

    # evaluate conclusion
    conclusion = implies((not r), (not t))

    # check if valid
    if not (premise1 and premise2 and premise3 and premise4) and conclusion:
        continue
    else:
        check_b = True


# p → q
# ¬r ∨ s
# p ∨ r
# ∴ ¬q → s
for item in table_4:
    # initiate variables
    p, q, r, s = item

    # evaluate expression
    premise1 = implies(p, q)
    premise2 = (not r) or s
    premise3 = p or r

    # evaluate conclusion
    conclusion = implies((not q), s)

    # check if valid
    if not (premise1 and premise2 and premise3) and conclusion:
        continue
    else:
        check_c = True

# p
# p → r
# p → (q ∨ ¬r)
# ¬q ∨ ¬s
# ∴ s
for item in table_4:
    p, q, r, s = item

    premise1 = p
    premise2 = implies(p, r)
    premise3 = implies(p, q or (not r))
    premise4 = (not q) or (not r)

    conclusion = s

    if not (premise1 and premise2 and premise3 and premise4) and conclusion:
        continue
    else:
        check_d = True

checkValid(check_a)
checkValid(check_b)
checkValid(check_c)
checkValid(check_d)
