import sys
sys.setrecursionlimit(2000)


class Item:
    """An item to (maybe) put in a knapsack. Weight must be an int."""
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

    def __repr__(self):
        """The representation of an item"""
        return f"Item({self.value}, {self.weight})"


def max_value(items, capacity, i=0):
    """
    Compute the maximum achievable value for the 0/1 knapsack problem
    using top-down DP (recursion with memoization).
    """
    cache = {}

    # When i isn't provided, default to considering all items
    if i == 0:
        i = len(items)

    def loop_max(i, capacity):
        # Return memoized result if we've seen this subproblem
        if (i, capacity) in cache:
            return cache[(i, capacity)]

        # Base cases: no items or no capacity → value 0
        if i == 0 or capacity == 0:
            result = 0

        # If the i-th item's weight exceeds capacity, skip it
        elif items[i - 1].weight > capacity:
            result = loop_max(i - 1, capacity)

        else:
            # Either skip the item or take it; choose the better value
            result = max(
                loop_max(i - 1, capacity),
                items[i - 1].value + loop_max(i - 1, capacity - items[i - 1].weight),
            )

        cache[(i, capacity)] = result
        return result

    return loop_max(i, capacity)


# --- Small test (from your example) ---
if __name__ == "__main__":
    items = [
        Item(45, 3),
        Item(45, 3),
        Item(80, 4),
        Item(80, 5),
        Item(100, 8),
    ]

    # Capacity 10 → best is 80(4) + 45(3) + 45(3) = 170
    ans = max_value(items, 10)
    print(ans)            # Expected: 170
    assert ans == 170
