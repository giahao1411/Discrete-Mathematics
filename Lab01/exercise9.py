# exercise 9


# if - then combination
def ithCombine(p, q):
    return "if {}, then {}".format(p, q)


# and not combination
def panqCombine(p, q):
    return "{}, and not {}".format(p, q)


# not - or combination
def npoqCombine(p, q):
    return "not {}, or {}".format(p, q)


p = "is sunny"
q = "I go camping"

res1 = ithCombine(p, q)
res2 = panqCombine(p, q)
res3 = npoqCombine(p, q)

print(res1)
print(res2)
print(res3)
