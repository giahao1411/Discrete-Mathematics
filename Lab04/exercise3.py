import math
import sys


def isPrime(n):
    if n <= 1:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# (a) ∀x ∈ Z, 0 ≤ x ≤ 100, x^3 >= x
print("a. ∀x ∈ Z, 0 ≤ x ≤ 100, x^3 >= x")
print("Negation: ∃x ∈ Z, 0 ≤ x ≤ 100, x^3 < x")

for x in range(101):
    if x**3 < x:
        print("VALID")
        break

# (b) ∀x ∈ Z, 0 ≤ x ≤ 100, and x is even, x ∗ 3 + 1 is a prime number
print("b. ∀x ∈ Z, 0 ≤ x ≤ 100, and x is even, x ∗ 3 + 1 is a prime number")
print(
    "Negation: ∃x ∈ Z, 0 ≤ x ≤ 100, and x is not even, x ∗ 3 + 1 is not a prime number"
)

for x in range(101):
    if x % 2 != 0 and not isPrime(x * 3 + 1):
        print("VALID")
        break

# (c) ∀x ∈ Z, 1 ≤ x, y ≤ 100, and x is even, x ∗ 5 + 3 is a prime number
print("c. ∀x ∈ Z, 1 ≤ x, y ≤ 100, and x is even, x ∗ 5 + 3 is a prime number")
print(
    "Negation: ∃x ∈ Z, 1 ≤ x, y ≤ 100, and x is not even, x ∗ 5 + 3 is not a prime number"
)

for x in range(1, 101):
    if x % 2 != 0 and isPrime(x * 5 + 3):
        print("VALID")
        break

# (d) ∀c ∈ Z, 0 < c ≤ 100, c%4 = 0, ∃a, b ∈ Z+, c^2 = a^2 + b^2
print("d. ∀c ∈ Z, 0 < c ≤ 100, c%4 = 0, ∃a, b ∈ Z+, c^2 = a^2 + b^2")
print("Negation: ∃c ∈ Z, 0 < c ≤ 100, c%4 != 0, ∀a, b ∈ Z+, c^2 != a^2 + b^2")

for c in range(1, 101):
    if c % 4 != 0:
        for a in range(sys.maxsize):
            for b in range(sys.maxsize):
                if c**2 != a**2 + b**2:
                    print("VALID")
                    break
            break
        break

# (e) ∀c ∈ Z, 0 < c ≤ 100, c%5 = 0, ∃a, b ∈ Z+, c^2 = a^2 + b^2
print("e. ∀c ∈ Z, 0 < c ≤ 100, c%5 = 0, ∃a, b ∈ Z+, c^2 = a^2 + b^2")
print("Negation: ∃c ∈ Z, 0 < c ≤ 100, c%5 != 0, ∀a, b ∈ Z+, c^2 != a^2 + b^2")

for c in range(1, 101):
    if c % 5 != 0:
        for a in range(sys.maxsize):
            for b in range(sys.maxsize):
                if c**2 != a**2 + b**2:
                    print("VALID")
                    break
            break
        break

# (f) ∃c ∈ Z, 0 < c ≤ 100, c^2 ≤ c
print("f. ∃c ∈ Z, 0 < c ≤ 100, c2 ≤ c")
print("Negation: ∀c ∈ Z, 0 < c ≤ 100, c2 ≥ c")

for c in range(1, 101):
    if c**2 >= c:
        print("VALID")
        break
