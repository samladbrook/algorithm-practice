class Node:
    """Internal node of a binary tree (no value; just left/right subtrees)."""
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


class Leaf:
    """Leaf node that stores a single value."""
    def __init__(self, value):
        self.value = value


def binary_search_tree(nums, is_sorted=False):
    """
    Build a balanced binary tree from a list of numbers.
    """
    if not nums:
        return None

    # Sort once at the top (unless caller guarantees sorted input)
    if not is_sorted:
        nums = sorted(nums)

    n = len(nums)
    if n == 1:
        return Leaf(nums[0])  # Base case: single element becomes a Leaf

    # Split around the midpoint to keep the tree balanced
    mid = n // 2
    left = binary_search_tree(nums[:mid], True)
    right = binary_search_tree(nums[mid:], True)
    return Node(left, right)  # Internal node with two subtrees


def print_tree(node, prefix="", is_left=True):
    """
    Pretty-print the tree sideways using box-drawing characters.

    """
    if node is None:
        print(prefix + ("└── " if is_left else "┌── ") + "∅")
        return

    if isinstance(node, Leaf):
        print(prefix + ("└── " if is_left else "┌── ") + f"Leaf({node.value})")
    elif isinstance(node, Node):
        print(prefix + ("└── " if is_left else "┌── ") + "Node")
        # Recurse: left shown below, right shown above (conventional sideways print)
        if node.left:
            print_tree(node.left, prefix + ("    " if is_left else "│   "), True)
        if node.right:
            print_tree(node.right, prefix + ("    " if is_left else "│   "), False)


# --- Small test / example ---
if __name__ == "__main__":
    nums = [15, 3, 11, 21, 7, 0, 19, 33, 29, 4]
    tree = binary_search_tree(nums)
    print_tree(tree)
