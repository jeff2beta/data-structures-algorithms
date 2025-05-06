def maxSubFaster(arr):
    n = len(arr)

    S = [0] * (n + 1)  # Create list of zeros
    for i in range(1, n + 1):
        # Add each element in arr and append each value as element in S
        S[i] = S[i - 1] + arr[i - 1]

    maxSum = float('-inf')
    # Iterates through S with j and k to sub each pair 
    for j in range(1, n + 1):
        for k in range(j, n + 1):
            # keeps track of the max sum by subtracting each k element by the j element - 1
            s = S[k] - S[j - 1]
            if s > maxSum:
                maxSum = s

    return maxSum

numbers = [4, -1, 2, 1, -5, 4]
print(maxSubFaster(numbers))     