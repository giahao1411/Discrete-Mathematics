from exercise1_5 import *
from exercise6 import *
from exercise7 import *
from exercise8_9 import *
from exercise10 import *
from exercise11 import *
from exercise12 import *
from exercise13 import *

print("\nShakespeare Tragedy:", Shakespeare_Tragedy)
print("\nAndersen Comedy:", Andersen_Comedy)
print("\nWork set:", Work)
print("\nAuthor_Of['Hamlet']:", Author_Of["Hamlet"])
print(
    "\nWriten_By['Shakespeare']:",
    [k for k, v in Writen_By.items() if v == "Shakespeare"],
)
print("\nWork_Count:", Work_Count)
print("\nWord count in Exercise section:", exercise_word_count)
print("\nWord frequency count (sorted):", sorted_word_frequency)
