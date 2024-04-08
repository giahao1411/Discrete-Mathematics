def waytochoose(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return waytochoose(n - 1, k) + waytochoose(n - 1, k - 1)


def find_k(n):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        ways = waytochoose(n, mid)

        if ways == 1000:
            return mid
        elif ways < 1000:
            left = mid + 1
        else:
            right = mid - 1

    if waytochoose(n, left) - 1000 < 1000 - waytochoose(n, right):
        return left
    else:
        return right


n = 50
k = find_k(n)
print(
    "The value of k that gives the number of ways to choose as close to 1000 as possible is:",
    k,
)
