def lcs(s1, s2):
    """
    Compute the Longest Common Subsequence (LCS) of two strings using
    recursion with memoization.
    
    Notes
    -----
    - LCS is the longest sequence that appears in both strings in the same order
      (not necessarily contiguous).
    - This implementation uses top-down dynamic programming with a cache to
      avoid recomputing subproblems.
    - Time complexity: O(len(s1) * len(s2))
    """
    cache = {}  # Memoization dictionary keyed by (i, j) positions

    def lcs_recursive(i, j):
        """
        Recursive helper function to compute LCS from positions i in s1 and j in s2.
        """
        # Return cached value if already computed
        if (i, j) in cache:
            return cache[(i, j)]

        # Base case: reached the end of either string
        if i == len(s1) or j == len(s2):
            result = ""
        # Characters match → take it and move both indices forward
        elif s1[i] == s2[j]:
            result = s1[i] + lcs_recursive(i + 1, j + 1)
        else:
            # Case 1: skip s1[i]
            result1 = lcs_recursive(i + 1, j)
            # Case 2: skip s2[j]
            result2 = lcs_recursive(i, j + 1)
            # Take the longer result
            result = result1 if len(result1) > len(result2) else result2

        # Save in cache and return
        cache[(i, j)] = result
        return result

    # Start recursion from the beginning of both strings
    return lcs_recursive(0, 0)


# --- Test ---
if __name__ == "__main__":
    s1 = "balderdash!"
    s2 = "balderdash!"
    print(lcs(s1, s2))  # Expected: "balderdash!"
