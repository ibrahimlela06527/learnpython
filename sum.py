# recursive/recursion
def recSum(arr):
    if len(arr) == 0:  # Base case
        return 0
    return arr[0] + recSum(arr[1:])


# [20,5,30] = 55
# 20 + sum([5,30]) = 20 + 35
# 5 + sum([30]) = 35
# 30 + sum([]) = 30

# print(recSum([20, 5, 30]))


# Find max

def recMax(arr):
    if len(arr) == 0:  # Base case
        return 0
    return max(arr[0], recMax(arr[1:]))
    # subMax = recMax(arr[1:])
    # if arr[0]> subMax:
    #     return arr[0]
    # return subMax


print(recMax([20, 5, 30, 50, 300, 1350, 20, 10]))
