import math

check_e = False

# (a) ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 15^2 + 16^2
for x in range(101):
    if not (x**2 == (15**2 + 16**2)):
        continue
    else:
        print("a. VALID")
        break

# (b) ∃x ∈ Z, 0 ≤ x ≤ 100, x^2 = 12^2 + 16^2
for x in range(101):
    if not (x**2 == (12**2 + 16**2)):
        continue
    else:
        print("b. VALID")
        break

# (c) ∃x ∈ Z, −50 ≤ x ≤ 50, x^2 ≥ 99x
for x in range(-50, 5 + 1):
    if not (x**2 >= 99 * x):
        continue
    else:
        print("c. VALID")
        break

# (d) ∃x ∈ Z, 50 ≤ x ≤ 100, x(x + 1)(x + 2)%6 != 0
for x in range(50, 100 + 1):
    if not (x * (x + 1) * (x + 2)) % 6 != 0:
        continue
    else:
        print("d. VALID")
        break

# (e) ∃x, y ∈ Z, 0 ≤ x ≤ 100, √(x + y) = √x + √y
for x in range(101):
    for y in range(101):
        if not (math.sqrt(x + y) == math.sqrt(x) + math.sqrt(y)):
            continue
        else:
            check_e = True
            break
if check_e is True:
    print("e. VALID")
else:
    print("e. INVALID")
