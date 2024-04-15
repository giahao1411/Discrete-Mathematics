from exercise1_5 import *
from exercise7 import *
from exercise8_9 import *

Work_Count = {}
for work in Work:
    count = sum(work in s for s in (Andersen, Shakespeare, Tragedy, Comedy, Uncategory))
    Work_Count[work] = count
