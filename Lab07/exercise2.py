def richest(coins):
    if len(coins) == 1:
        return coins[0]

    previous_richest = richest(coins[:-1])
    current_man = coins[-1]
    return max(current_man, previous_richest)


coins = [10, 5, 15, 8, 20, 12]
richest_man = richest(coins)
print("The richest man has", richest_man, "gold coins.")
