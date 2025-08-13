class Item:
    """An item to (maybe) put in a knapsack."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"Item({self.value}, {self.weight})"


def max_value(items, capacity):
    """
    Compute the maximum value for the 0/1 knapsack via bottom-up DP,
    and reconstruct one optimal set of items.
    """
    n = len(items)

    # dp[i][w] = best value achievable using first i items with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Fill the DP table row by row (items), column by column (capacity)
    for i in range(1, n + 1):
        item = items[i - 1]
        for w in range(capacity + 1):
            if item.weight > w:
                # Can't take the item: inherit best from previous row
                dp[i][w] = dp[i - 1][w]
            else:
                # Option 1: skip item; Option 2: take item once
                dp[i][w] = max(dp[i - 1][w],
                               dp[i - 1][w - item.weight] + item.value)

    # ----- Reconstruct chosen items by backtracking through the table -----
    w = capacity
    selected_items = []
    for i in range(n, 0, -1):
        # If value changed from the row above, item i-1 was included
        if dp[i][w] != dp[i - 1][w]:
            item = items[i - 1]
            selected_items.append(item)
            w -= item.weight  # Reduce remaining capacity accordingly

    # DP value is at bottom-right; selected_items is one optimal set (in reverse pick order)
    return dp[n][capacity], selected_items


# --- Small test (same data as your example) ---
if __name__ == "__main__":
    items = [
        Item(45, 3),
        Item(45, 3),
        Item(80, 4),
        Item(80, 5),
        Item(100, 8),
    ]
    maximum, selected_items = max_value(items, 10)
    print(maximum)  # Expected: 170 (e.g., 80+45+45)

    # If a checker is available in your environment, use it; otherwise ignore.
    try:
        check_item_list(items, selected_items, maximum)  # Provided externally
    except NameError:
        pass
