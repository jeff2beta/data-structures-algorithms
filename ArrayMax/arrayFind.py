def arrayFind(x, arr):
    i = 0
    while i < len(arr):
        # finds element i in array
        if x == arr[i]:
            return i
        # Else searches the next element
        else:
            i += 1
    # If I doesn't find element returns -1
    return -1

numbers = [12, 34, 45, 33, 4, 7, 99]

print(arrayFind(2, numbers))