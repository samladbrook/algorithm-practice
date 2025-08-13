"""A (now fixed) recursive search for the optimal path through
   a grid of weights, with memoization to avoid recomputation.
   Richard Lobb (orig), comments & memoization added.
"""

INFINITY = float('inf')  # Same as math.inf


def read_grid(filename):
    """
    Read from the given file an n x m grid of integer weights.

    The file must consist of n lines of m space-separated integers.
    n and m are inferred from the file contents.

    Notes
    -----
    THIS FUNCTION DOES NOT HAVE BUGS (per original comment).
    """
    with open(filename) as infile:
        lines = infile.read().splitlines()

    grid = [[int(bit) for bit in line.split()] for line in lines]
    return grid


def grid_cost(grid):
    """
    Compute the cheapest cost from the top row to the bottom row
    (1-origin in the original spec; here rows are 0..n-1).

    Movement rule
    -------------
    From a cell (r-1, c+delta) you may enter (r, c) where delta ∈ {-1, 0, 1}.
    Off-grid positions are treated as having infinite cost.

    Parameters
    ----------
    grid : list[list[int]]
        Non-empty rectangular grid of integer weights.

    Returns
    -------
    int
        Minimum achievable cost to reach any cell in the bottom row.
    """
    n_rows = len(grid)
    n_cols = len(grid[0])

    cache = {}  # Memoize cell costs keyed by (row, col)

    def cell_cost(row, col):
        """
        Cost of the cheapest path ending at (row, col).
        """
        # Bounds check: off-grid cells are "infinite"
        if row < 0 or row >= n_rows or col < 0 or col >= n_cols:
            return INFINITY

        # Memoized result?
        key = (row, col)
        if key in cache:
            return cache[key]

        # Base row: cost is the cell itself
        if row == 0:
            result = grid[row][col]
        else:
            # Recur to the three predecessors in the row above
            best_prev = min(
                cell_cost(row - 1, col - 1),
                cell_cost(row - 1, col),
                cell_cost(row - 1, col + 1),
            )
            result = grid[row][col] + best_prev

        cache[key] = result
        return result

    # Best path cost is the cheapest among bottom-row cells
    best = min(cell_cost(n_rows - 1, col) for col in range(n_cols))
    return best


def file_cost(filename):
    """
    Convenience wrapper: read grid from file and compute cheapest top→bottom cost.
    """
    return grid_cost(read_grid(filename))


# --- Small test / example ---
if __name__ == "__main__":
    # Expects a file like 'checkerboard.trivial.in' in the working directory.
    # Example file format:
    # 1 2 3
    # 4 5 6
    # 7 8 9
    try:
        print(file_cost('checkerboard.trivial.in'))
    except FileNotFoundError:
        print("Example file 'checkerboard.trivial.in' not found. Create it to run the demo.")
