import itertools


def implies(a, b):
    return (not a) or b


def checkEquivalent(count, table):
    if count == len(table):
        print("Equivalent")
    else:
        print("Inequivalent")


table_1 = list(itertools.product([False, True], repeat=1))
table_2 = list(itertools.product([False, True], repeat=2))
table_3 = list(itertools.product([False, True], repeat=3))

# p ≡ ¬(¬p)
print("1. p ≡ ¬(¬p)")
count_1 = 0

for item in table_1:
    if item[0] == (not (not item[0])):
        count_1 = count_1 + 1
checkEquivalent(count_1, table_1)


# ¬(¬q ∧ p) ∧ (q ∨ p) ≡ q
print("2. ¬(¬q ∧ p) ∧ (q ∨ p) ≡ q")
count_2 = 0

for item in table_2:
    exp_left = (not ((not item[1]) and item[0])) and (item[1] or item[0])
    if exp_left == item[1]:
        count_2 = count_2 + 1
checkEquivalent(count_2, table_2)


# ¬(p ∨ q) ≡ (¬p ∨ ¬q)
print("3. ¬(p ∨ q) ≡ (¬p ∨ ¬q)")
count_3 = 0

for item in table_2:
    exp_left = not (item[0] or item[1])
    exp_right = (not item[0]) or (not item[1])
    if exp_left == exp_right:
        count_3 = count_3 + 1
checkEquivalent(count_3, table_2)


# (p ∨ q) → r ≡ (p → r) ∧ (q → r)
print("3. (p v q) → r ≡ (p → r) ∧ (q → r)")
count_4 = 0

for item in table_3:
    exp_left = implies(item[0] or item[1], item[2])
    exp_right = implies(item[0], item[2]) and implies(item[1], item[2])
    if exp_left == exp_right:
        count_4 = count_4 + 1
checkEquivalent(count_4, table_3)


# ¬(p ∧ q) ≡ (¬p ∧ ¬q)
print("¬(p ∧ q) ≡ (¬p ∧ ¬q)")
count_5 = 0

for item in table_2:
    exp_left = not item[0] and item[1]
    exp_right = (not item[0]) and (not item[1])
    if exp_left == exp_right:
        count_5 = count_5 + 1
checkEquivalent(count_5, table_2)


# (p ∨ ¬q) → ¬p ≡ (p ∨ (¬q)) → ¬p
print("(p ∨ ¬q) → ¬p ≡ (p ∨ (¬q)) → ¬p")
count_6 = 0

for item in table_2:
    exp_left = implies(item[0] or (not item[1]), (not item[0]))
    exp_right = implies(item[0] or (not item[1]), (not item[0]))
    if exp_left == exp_right:
        count_6 = count_6 + 1
checkEquivalent(count_6, table_2)


# ¬(p ∨ q) ≡ (¬p ∧ ¬q)
print("¬(p ∨ q) ≡ (¬p ∧ ¬q)")
count_7 = 0

for item in table_2:
    exp_left = not (item[0] or item[1])
    exp_right = (not item[0]) and (not item[1])
    if exp_left == exp_right:
        count_7 = count_7 + 1
checkEquivalent(count_7, table_2)
