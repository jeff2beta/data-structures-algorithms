def recursiveMax(arr, n):
    # Base case
    if n == 1:
        return arr[0]
    # Recursive call: compare the last element with result of the recursive call
    return max(recursiveMax(arr, n - 1), arr[n - 1])

numbers = [5, 7, 8, 5, 4, 9, 2, 10]

print(recursiveMax(numbers, len(numbers)))