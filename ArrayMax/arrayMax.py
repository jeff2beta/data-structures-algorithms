def arrayMax(arr, n):
    max = arr[0]
    for i in range(1, len(arr)):
        if max < arr[i]:
           max = arr[i]
    return max

numbers = [2, 7, 2, 1, 7, 22, 6]

print(arrayMax(numbers, len(numbers)))


