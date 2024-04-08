def thieves(day):
    if day == 1:
        return 1
    return day + thieves(day - 1)


def find_last_day(total_thieves):
    day = 1
    while thieves(day) <= total_thieves:
        day += 1
    return day - 1


total_thieves = 40
last_day = find_last_day(total_thieves)

print("The number of thieves sent on the last day is:", thieves(last_day))
print("It will take", last_day, "days until the boss can't send any more thieves.")
