# (a) p → r
# ¬p → q
# q → s
# ∴ ¬r → s

print("a.")
print("p → r")
print("¬p → q")
print("q → s")
print("∴ ¬r → s")
print(
    "We have ¬r which is ¬r then ¬p, ¬p then q, q then s. Therefore the conclusion is VALID"
)

# (b) p → (q → r)
# p ∨ s
# t → q
# ¬s
# ∴ ¬r → ¬t

print("b.")
print("p → (q → r)")
print("p ∨ s")
print("t → q")
print("¬s")
print("∴ ¬r → ¬t")
print(
    "We have p V s which is p can be true or not, but with ¬s, we have that p is true"
)
print(
    "p true then q → r, with assumption of ¬r, ¬r then ¬q, ¬q then ¬t. Therefore, the conclusion is VALID"
)

# (c) p → q
# ¬r ∨ s
# p ∨ r
# ∴ ¬q → s

print("c.")
print("p → q")
print("¬r ∨ s")
print("p ∨ r")
print("∴ ¬q → s")
print(
    "We have ¬q then ¬p, ¬p then r but ¬r ∨ s, r then ¬s. Therefore, the conclusion is INVALID"
)

# (d) p
# p → r
# p → (q ∨ ¬r)
# ¬q ∨ ¬s
# ∴ s

print("d.")
print("p")
print("p → r")
print("p → (q ∨ ¬r)")
print("¬q ∨ ¬s")
print("∴ s")
print(
    "We have p, then r, and q ∨ ¬r, with r then ¬q, ¬q ∨ ¬s. Therefore the conclusion is INVALID"
)
