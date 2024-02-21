import itertools


# define a function to calculate the implies
def implies(a, b):
    return (not a) or b


table = list(itertools.product([False, True], repeat=3))

print("p \t q \t r \t p and q -> r \t r -> p and q")
for item in table:
    print(
        item[0],
        "\t",
        item[1],
        "\t",
        item[2],
        "\t",
        implies(item[0] and item[1], item[2]),
        "\t\t",
        implies(item[2], item[0] and item[1]),
    )
