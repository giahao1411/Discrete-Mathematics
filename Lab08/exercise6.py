from exercise1_5 import *

print("Andersen_Comedy issubset Comedy:", Andersen_Comedy.issubset(Comedy))
print(
    "Andersen_Comedy isdisjoint Shakespeare_Tragedy:",
    Andersen_Comedy.isdisjoint(Shakespeare_Tragedy),
)
print(
    "Shakespeare_Tragedy issuperset Tragedy:", Shakespeare_Tragedy.issuperset(Tragedy)
)
