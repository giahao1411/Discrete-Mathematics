from exercise12 import *
from collections import Counter

word_frequency = Counter(exercise_content.split())
sorted_word_frequency = dict(
    sorted(word_frequency.items(), key=lambda item: item[1], reverse=True)
)

