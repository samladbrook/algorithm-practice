def quicksort(arr):
    """
    Sorts a list using the Quicksort algorithm.

    Notes
    -----
    - This is a recursive implementation of Quicksort.
    - The pivot is chosen as the middle element for simplicity.
    - The algorithm has an average time complexity of O(n log n),
      but worst-case complexity of O(n^2) if the pivot choice is poor.
    """
    if len(arr) <= 1:
        return arr  # Base case: already sorted
    else:
        pivot = arr[len(arr) // 2]  # Choose middle element as pivot
        left = [x for x in arr if x < pivot]      # Elements less than pivot
        middle = [x for x in arr if x == pivot]   # Elements equal to pivot
        right = [x for x in arr if x > pivot]     # Elements greater than pivot
        return quicksort(left) + middle + quicksort(right)


# --- Simple test ---
if __name__ == "__main__":
    test_data = [3, 6, 8, 10, 1, 2, 1]
    print("Original:", test_data)
    sorted_data = quicksort(test_data)
    print("Sorted:", sorted_data)
