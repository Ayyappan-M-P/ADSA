def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check the left side of the current row
        for i in range(col):
            if board[row][i] == 'Q':
                return False
        
        # Check upper left diagonal
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        # Check lower left diagonal
        for i, j in zip(range(row, n), range(col, -1, -1)):
            if board[i][j] == 'Q':
                return False
        
        return True

    def solve(board, col):
        if col == n:
            solutions.append(["".join(row) for row in board])
            return
        
        for row in range(n):
            if is_safe(board, row, col):
                board[row][col] = 'Q'
                solve(board, col + 1)
                board[row][col] = '.'  # Backtrack

    solutions = []
    empty_board = [['.' for _ in range(n)] for _ in range(n)]
    solve(empty_board, 0)
    return solutions

# Input N (e.g., N = 4 or N = 8)
N = 4

# Find all possible solutions for N-Queens
solutions = solve_n_queens(N)

# Display the solutions
for i, solution in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in solution:
        print(row)
    print()
