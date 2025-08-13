def merge_sort(arr):
    """
    Sorts a list using the Merge Sort algorithm.

    Notes
    -----
    - Merge Sort is a divide-and-conquer algorithm.
    - Time complexity is O(n log n) for all cases.
    - Not in-place: uses extra space proportional to the list size.
    """
    if len(arr) <= 1:
        return arr  # Base case: already sorted

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.
    """
    merged = []
    i = j = 0

    # Compare elements from both lists and add the smallest
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements (only one of these will run)
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# --- Simple test ---
if __name__ == "__main__":
    test_data = [3, 6, 8, 10, 1, 2, 1]
    print("Original:", test_data)
    sorted_data = merge_sort(test_data)
    print("Sorted:", sorted_data)
