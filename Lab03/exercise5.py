def nega(A):
    result = ""
    # Negative the Quantified
    if "For all" in A:
        result = A.replace("For all", "Exist")
    elif "Exist" in A:
        result = A.replace("Exsit", "For all")

    # Negative the P(x)
    if "not" in result:
        result = result.replace("not ", "")
    else:
        result = result.replace("are ", "are not ")
        result = result.replace("is ", "is not ")
        result = result.replace("they ", "they not ")
    return result


# Test cases
sa = "For all fishes, they need water to survive"
sb = "Exist a person, who is left handed"
sc = "Exist an employee in the company, who is late to work everyday"
sd = "For all fishes in this pond, they are Koi fish"

print("a.", nega(sa))
print("b.", nega(sb))
print("c.", nega(sc))
print("d.", nega(sd))
