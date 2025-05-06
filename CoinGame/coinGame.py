def coinGame(V):
    n = len(V)
    # Create a 2D array M with 0s
    M = [[0] * n for _ in range(n)]

    # Base case: One coin
    for i in range(n):
        M[i][i] = V[i]
        
    # Fill in the rest of the table 
    for s in range(2, n + 1):       # s is the length of the subarray
        for i in range(n - s + 1):
            j = i + s - 1
            M[i][j] = max(V[i] - M[i + 1][j], V[j] - M[i][j - 1])

    return M
    
V = [3, 9, 1, 2]
M = coinGame(V)

for row in M:
    print(row)