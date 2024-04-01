def Odyssey(n):
    O = []  # noqa: E741
    if n < 2:
        return O
    else:
        O.append(2)
        for i in range(3, n, 2):
            flag = True
            for j in range(0, len(O)):
                if i % O[j] == 0:
                    flag = False
                    break
            if flag:
                O.append(i)
        return O


print(Odyssey(10))
print(Odyssey(5))
print(Odyssey(20))
