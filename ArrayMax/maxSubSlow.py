# This is the brute force method O(n^3)
# Compares each element in each subarray and adds up each subarray

def maxSubSlow(arr):
    maxSum = float('-inf')  # Start with the smallest number possible
    n = len(arr)
    for j in range(n):      # Start index of subarray
        for k in range(j, n):   # End index of subarray
            currentSum = 0
            for i in range(j, k + 1):
                currentSum += arr[i]
            if currentSum > maxSum:
                maxSum = currentSum

    return maxSum

numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(maxSubSlow(numbers))


