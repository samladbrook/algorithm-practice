def change_greedy(amount, coinage):
    """
    Return change for a given amount using the greedy algorithm.

    Notes
    -----
    - This uses a greedy approach: at each step, use as many of the largest
      remaining coin as possible.
    - This works optimally for some coin systems (e.g., standard US coins)
      but not all.
    """
    current_amt = amount
    result_list = []

    # Ensure coin denominations are sorted largest → smallest
    coinage = sorted(coinage, reverse=True)

    # For each coin, take as many as possible without exceeding remaining amount
    for coin in coinage:
        count = current_amt // coin
        if count > 0:
            result_list.append((count, coin))
            current_amt -= count * coin

    # If we made exact change, return the result; otherwise, fail
    if current_amt == 0:
        return result_list
    else:
        return None


# --- Small test ---
if __name__ == "__main__":
    print(change_greedy(80, [1, 10, 25]))
    # Expected: [(3, 25), (1, 10)]
