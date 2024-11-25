def solve_n_queens(n):
    board = [-1] * n
    solution = []
    if solve(board, 0, solution):
        return solution
    return None

def solve(board, row, solution):
    n = len(board)
    if row == n:
        # A solution is found; copy the board to the solution
        solution[:] = board.copy()
        return True
    else:
        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                if solve(board, row + 1, solution):
                    return True
                # Reset the row position for backtracking
                board[row] = -1
    return False

def is_safe(board, row, col):
    # Check if it's safe to place a queen at (row, col)
    for i in range(row):
        if (
            board[i] == col
            or board[i] - i == col - row
            or board[i] + i == col + row
        ):
            return False
    return True

def print_solution(solution, n):
    # Print the solution in a readable format
    if not solution:
        print("No solution found.")
    else:
        print("Solution:")
        for i in range(n):
            row = ['.'] * n
            row[solution[i]] = 'Q'
            print(' '.join(row))

# Set N value for the board size
n = 4  # Change this value to solve for a different board size
solution = solve_n_queens(n)
print_solution(solution, n)
