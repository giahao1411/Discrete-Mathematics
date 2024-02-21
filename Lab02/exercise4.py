import itertools


def implies(a, b):
    return (not a) or b


def equivalent(p, q):
    return implies(p, q) and implies(q, p)


table_2 = list(itertools.product([False, True], repeat=2))
table_3 = list(itertools.product([False, True], repeat=3))
table_4 = list(itertools.product([False, True], repeat=4))

# expression 1
print("p \t q \t p ∨ q → p ∧ q → ¬p ∨ ¬q")
for item in table_2:
    exp1 = implies(item[0] or item[1], item[0]) and item[1]
    exp2 = implies(exp1, (not item[0]) or (not item[1]))
    print(item[0], "\t", item[1], "\t", exp2)
print("---------------------------")

# expression 2
print("p \t q \t r \t ¬p ∨ (q ∧ r) → r")
for item in table_3:
    exp = (not item[0]) or (item[1] and item[2])
    print(item[0], "\t", item[1], "\t", item[2], "\t", implies(exp, item[2]))
print("---------------------------")

# expression 3
print("p \t q \t r \t (p → q) ∧ (q → r)")
for item in table_3:
    exp1 = implies(item[0], item[1])
    exp2 = implies(item[1], item[2])
    print(item[0], "\t", item[1], "\t", item[2], "\t", exp1 and exp2)
print("---------------------------")

# expression 4
print("p \t q \t r \t (p ∨ (q ∧ r)) ↔ ((p ∨ q) ∧ (p ∨ r))")
for item in table_3:
    exp1 = item[0] or (item[1] and item[2])
    exp2 = (item[0] or item[1]) and (item[0] or item[2])
    print(item[0], "\t", item[1], "\t", item[2], "\t", equivalent(exp1, exp2))
print("---------------------------")


# expression 5
print("p \t q \t r \t t \t p ∨ q → ¬r ∨ t")
for item in table_4:
    exp1 = item[0] or item[1]
    exp2 = (not item[2]) or item[3]
    print(
        item[0], "\t", item[1], "\t", item[2], "\t", item[3], "\t", implies(exp1, exp2)
    )
print("---------------------------")

# expression 6
print("p \t q \t r \t t \t p ∨ t → q → (r → t)")
for item in table_4:
    exp1 = item[0] or item[3]
    exp2 = implies(item[1], implies(item[2], item[3]))
    print(
        item[0], "\t", item[1], "\t", item[2], "\t", item[3], "\t", implies(exp1, exp2)
    )
print("---------------------------")

# expression 7
print("p \t q \t r \t t \t (p ∨ (q ∧ r)) ↔ (((p ∨ q) ∧ (p ∨ r)) ∧ (t ∨ ¬t))")
for item in table_4:
    exp1 = item[0] or (item[1] and item[2])
    exp2 = ((item[0] or item[1]) and (item[0] or item[2])) and (
        item[3] or (not item[3])
    )
    print(
        item[0],
        "\t",
        item[1],
        "\t",
        item[2],
        "\t",
        item[3],
        "\t",
        equivalent(exp1, exp2),
    )
