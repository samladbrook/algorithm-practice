def key_positions(seq, key):
    """
    Computes the starting index positions for each key value in a stable counting sort.
    """
    # Step 1: Find the maximum key value
    k = max(key(x) for x in seq)
    
    # Step 2: Create and initialize C array
    C = [0] * (k + 1)
    
    # Step 3: Count occurrences of each key
    for x in seq:
        C[key(x)] += 1
    
    # Step 4: Cumulative sum to find starting positions
    for i in range(1, len(C)):
        C[i] += C[i-1]
    
    # Step 5: Shift C right by one position
    for i in range(len(C)-1, 0, -1):
        C[i] = C[i-1]
    C[0] = 0
    
    return C


# --- test ---
if __name__ == "__main__":
    # For numbers from -3 to 2, the key is the square of the number.
    # Keys: 9, 4, 1, 0, 1, 4
    # Sorted keys: 0, 1, 1, 4, 4, 9
    result = key_positions(range(-3, 3), lambda x: x**2)
    print("Starting positions:", result)
    # Expected: key 0 starts at index 0, key 1 starts at 1, key 4 starts at 3, key 9 starts at 5
