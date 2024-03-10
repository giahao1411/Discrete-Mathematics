# (a) Given:
P = "Phong has Visa"
S1 = "If Phong can fly, Phong will go to America"
S2 = "If Phong has Visa, Phong will go to America"
S3 = "If Phong can speak English, Phong will go to America"
# Conclusion:
C = "Phong goes to America"

print("a.\n", P, "\n", S1, "\n", S2, "\n", S3, "\n", C)
print("-> VALID")

# (b) Given:
P = "It’s hot yesterday"
S1 = "If it’s hot, it will rain the next day"
S2 = "If and only if it’s not rain, Nam goes outside"
S3 = "If it’s not hot, Nam will go outside"
# Conclusion:
C = "Nam goes outside"

print("b.\n", P, "\n", S1, "\n", S2, "\n", S3, "\n", C)
print("-> INVALID")

# (c) Given:
Q = "An wake up late"
R = "The traffic is flowing smooth"
S1 = "The traffic is always heavy on school day"
S2 = "If An wake up late, he will be late for school on school day"
S3 = "An only have to go to school on school day"
S4 = "If An don’t have to go to school, An can’t be late for school"
# Conclusion:
C = "An is late for school"

print("c.\n", P, "\n", R, "\n", S1, "\n", S2, "\n", S3, "\n", C)
print("-> INVALID")

# TODO: Prove/Disprove the conclusion C using the given data
# (d) Given:
P = "∃x, y ∈ R, (x + y)^2 ≤ x^2 + y^2"
Q = "∀x, y ∈ Z+, x + y ≥ x + y"
R = "∀x, y ∈ Z+, x + y + 2√(xy) ≥ x + y"
T = "∀x, y ∈ Z+, √(x + y) ≥ 0"
S1 = "∀x, y ∈ Z+, (x^2 ≥ y^2) → (x ≥ y)"
S2 = "∀x, y ∈ Z+, (x ≥ y) → (x^2 ≥ y^2)"
S3 = "∀x, y ∈ R+, (x ≥ y) → (x^2 ≥ y^2)"
S4 = "∀x, y ∈ R+, (x^2 ≥ y^2) → (x ≥ y)"
# Conclusion:
C = "∀x, y ∈ Z+, (√x + √y) ≥ √(x + y)"

print("d.\n", "P =", P, "\n Q =", Q, "\n R =", R, "\n T =", T)
print(" S1 =", S1, "\n S2 =", S2, "\n S3 =", S3, "\n S4 =", S4)
