def calculate_characters(story_number):
    if story_number == 1:
        return 1
    else:
        return 2 ** (story_number - 1) + calculate_characters(story_number - 1)


total_characters = calculate_characters(547)
print("Total characters in Scheherazade's stories:", total_characters)
