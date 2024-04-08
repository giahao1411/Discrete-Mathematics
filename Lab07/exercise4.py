def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def waytochooseP(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return factorial(n) // factorial(n - k)


def find_k(n, target):
    left = 0
    right = n

    while left <= right:
        mid = (left + right) // 2
        permutations = waytochooseP(n, mid)

        if permutations == target:
            return mid
        elif permutations < target:
            left = mid + 1
        else:
            right = mid - 1

    # Check which value of k gives the closest number of permutations
    permutations_left = waytochooseP(n, left)
    permutations_right = waytochooseP(n, right)

    if abs(permutations_left - target) < abs(permutations_right - target):
        return left
    else:
        return right


n = 50
target = 10000

k = find_k(n, target)
print("The value of k that gives the number of permutations closest to 10,000 is:", k)
