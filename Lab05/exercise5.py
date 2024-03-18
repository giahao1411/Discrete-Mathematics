import itertools


def implies(p, q):
    return (not p) or q


table_4 = list(itertools.product([False, True], repeat=4))
table_5 = list(itertools.product([False, True], repeat=5))

print("p \t q \t r \t t \t q -> t \t p -> t \t r -> t")
for item in table_4:
    # initiate variables
    p, q, r, t = item

    # evaluate expression
    s1 = implies(q, t)
    s2 = implies(p, t)
    s3 = implies(r, t)

    # print truth table
    print(p, "\t", q, "\t", r, "\t", t, "\t", s1, "\t\t", s2, "\t\t", s3)


print("\np \t q \t r \t s \t v \t ¬q \t p -> (v and r) \t s and r \t ¬s -> ¬v")
for item in table_5:
    # initiate variables
    p, q, r, s, v = item

    # evaluate expression
    s1 = not q
    s2 = implies(p, v and r)
    s3 = s and r
    s4 = implies(not s, not v)

    # print truth table
    print(
        p,
        "\t",
        q,
        "\t",
        r,
        "\t",
        s,
        "\t",
        v,
        "\t",
        s1,
        "\t\t",
        s2,
        "\t\t",
        s3,
        "\t\t",
        s4,
    )
