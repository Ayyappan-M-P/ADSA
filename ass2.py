def matrix_chain_multiplication(matrices):
    n = len(matrices)
    
    # Initialize the DP table to store minimum multiplication counts
    dp = [[0] * n for _ in range(n)]
    
    # Initialize the bracket table to store the optimal parenthesization
    bracket = [[0] * n for _ in range(n)]
    
    # Fill in the DP table
    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            dp[i][j] = float('inf')
            for k in range(i, j):
                cost = dp[i][k] + dp[k+1][j] + matrices[i-1][0] * matrices[k][1] * matrices[j][1]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    bracket[i][j] = k
    
    # Reconstruct the optimal parenthesization
    def print_parenthesization(i, j):
        if i == j:
            return f"A{i}"
        else:
            k = bracket[i][j]
            left = print_parenthesization(i, k)
            right = print_parenthesization(k + 1, j)
            return f"({left} x {right})"
    
    optimal_parenthesization = print_parenthesization(1, n - 1)
    
    return optimal_parenthesization, dp[1][n-1]

# Input matrices
matrices = [(2, 3), (3, 4), (4, 2)]

# Find the optimal parenthesization and minimum scalar multiplications
optimal_parenthesization, min_scalar_multiplications = matrix_chain_multiplication(matrices)

print("Optimal Parenthesization:", optimal_parenthesization)
print("Minimum Scalar Multiplications:", min_scalar_multiplications)
