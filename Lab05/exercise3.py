P = "You get good grade in the midterm exam"
Q = "You understand how to solve all the exercises in the book"

print(P)
print(Q)

a = "if " + Q + " then " + P
b = Q + " and You not get good grade in the midterm exam"
c = P + " if and only if " + Q

print("a.", a)
print(
    "a. Negation: P and ~Q - "
    + P
    + " and You not understand how to solve all the exercises in the book"
)
print("a. Converse: if P then Q - ", "if " + P + " then " + Q)
print(
    "a. Contrapositive: ~Q and P - "
    "You not understand how to solve all the exercises in the book and" + P,
)
print()
print("b.", b)
print("b. Negation: ~P or Q - ", "You not get good grade in the midterm exam or " + Q)
print("b. Converse: ~P and Q - ", "You not get good grade in the midterm exam and " + Q)
print(
    "b. Contrapositive: Q and ~P - ",
    Q + " or You not understand how to solve all the exercises in the book",
)
print()

print("c.", c)
print("c. Negation: Q and ~P - ", Q + " and You not get good grade in the midterm exam")
print("c. Converse: Q if and only if P - ", Q + " if and only if " + P)
print("c. Contrapositive: ~P and Q - ", "You not get good grade in the midterm exam and " + Q)
