import math

# (a)
sum_left_exp = 0
for x in range(11):
    for y in range(11):
        sum_left_exp += (x + y) ** 2

sum_right_exp = 0
for x in range(11):
    for y in range(11):
        sum_right_exp += (x + 2 * y) ** 2

if sum_left_exp > sum_right_exp:
    print("a. VALID")
else:
    print("a. INVALID")

# (b)
left_exp = math.factorial(20)
right_exp = 0
for x in range(11):
    right_exp += math.factorial(x)

if left_exp < right_exp:
    print("b. VALID")
else:
    print("b. INVALID")

# (c)
sum_left_exp_c = 0
for x in range(11):
    sum_left_exp_c += 3 * x**2

right_exp_c = 10**3

if sum_left_exp_c >= right_exp_c:
    print("c. VALID")
else:
    print("c. INVALID")

# (d)
sum_left_exp_d = 0
for x in range(5, 11):
    sum_left_exp_d += 4 * x**3 + 6 * x**2 + 2 * x

right_exp_d = 10**4 + 2 * 10**3 + 10**2 - 5**4 - 2 * 5**3 - 5**2

if sum_left_exp_d > right_exp_d:
    print("d. VALID")
else:
    print("d. INVALID")
