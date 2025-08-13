def heapify(arr, n, i):
    """
    Ensures the subtree rooted at index i satisfies the max-heap property.
    """
    largest = i           # Assume the root is the largest
    left = 2 * i + 1       # Left child index
    right = 2 * i + 2      # Right child index

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heapsort(arr):
    """
    Sorts a list in ascending order using the Heap Sort algorithm.
    
    Notes
    -----
    - This is an in-place sorting algorithm.
    - Time complexity is O(n log n) for all cases.
    - Uses a max-heap structure.
    """
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap current root with last
        heapify(arr, i, 0)  # Heapify reduced heap

    return arr

# --- Simple test ---
if __name__ == "__main__":
    test_data = [3, 6, 8, 10, 1, 2, 1]
    print("Original:", test_data)
    sorted_data = heapsort(test_data)
    print("Sorted:", sorted_data)
