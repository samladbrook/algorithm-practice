INFINITY = float('inf')


def read_grid(filename):
    """
    Read an n×m grid of integers from a file.

    Each line contains m space-separated integers.
    Returns a list of lists of ints.
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()
    return [[int(bit) for bit in line.split()] for line in lines]


def grid_cost(grid):
    """
    Compute the cheapest cost from the top row to the bottom row
    using bottom-up dynamic programming (tabulation).
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    # dp[r][c] = min cost to reach cell (r, c) from some top-row cell
    dp = [[0] * n_cols for _ in range(n_rows)]

    # Base row: cost is just the cell's own weight
    for col in range(n_cols):
        dp[0][col] = grid[0][col]

    # Fill table row by row
    for row in range(1, n_rows):
        for col in range(n_cols):
            # Best predecessor from the row above (col-1, col, col+1)
            min_prev = INFINITY
            for delta_col in (-1, 0, 1):
                prev_col = col + delta_col
                if 0 <= prev_col < n_cols:
                    min_prev = min(min_prev, dp[row - 1][prev_col])

            dp[row][col] = grid[row][col] + min_prev

    # Best cost is the minimum in the bottom row
    return min(dp[n_rows - 1])


def file_cost(filename):
    """
    Convenience: read a grid from `filename` and return its cheapest top→bottom cost.
    """
    return grid_cost(read_grid(filename))


# --- Small test / demo ---
if __name__ == "__main__":
    # Example 3×3 grid inline (so this runs without a file):
    demo_grid = [
        [1, 2, 3],
        [4, 1, 6],
        [7, 1, 2],
    ]
    print("Demo grid cost:", grid_cost(demo_grid))  # Expected: 1 + 1 + 1 = 3

    # Optional: try a file if present
    try:
        print("File grid cost:", file_cost("checkerboard.trivial.in"))
    except FileNotFoundError:
        pass
