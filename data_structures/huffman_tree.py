"""A Huffman Coding module, for use in COSC262.
   Based on the provided skeleton; encode/decode implemented and commented.
   Richard Lobb (orig), comments & encode/decode added.
"""
import re

HAS_GRAPHVIZ = True
try:
    from graphviz import Graph
except ModuleNotFoundError:
    HAS_GRAPHVIZ = False


class Node:
    """Represents an internal node in a Huffman tree. It has a frequency count,
       minimum character in the tree, and left and right subtrees, assumed to be
       the '0' and '1' children respectively. The frequency count of the node
       is the sum of the children counts and its minimum character (min_char)
       is the minimum of the children min_chars.
    """
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.count = left.count + right.count
        self.min_char = min(left.min_char, right.min_char)

    def __repr__(self, level=0):
        return ((2 * level) * ' ' + f"Node({self.count},\n" +
                self.left.__repr__(level + 1) + ',\n' +
                self.right.__repr__(level + 1) + ')')

    def is_leaf(self):
        return False

    def plot(self, graph):
        """Plot the tree rooted at self on the given graphviz graph object.
           For graphviz node ids, we use the object ids, converted to strings.
        """
        graph.node(str(id(self)), str(self.count))  # Draw this node
        if self.left is not None:
            # Draw the left subtree
            self.left.plot(graph)
            graph.edge(str(id(self)), str(id(self.left)), '0')
        if self.right is not None:
            # Draw the right subtree
            self.right.plot(graph)
            graph.edge(str(id(self)), str(id(self.right)), '1')


class Leaf:
    """A leaf node in a Huffman encoding tree. Contains a character and its
       frequency count.
    """
    def __init__(self, count, char):
        self.count = count
        self.char = char
        self.min_char = char

    def __repr__(self, level=0):
        return (level * 2) * ' ' + f"Leaf({self.count}, '{self.char}')"

    def is_leaf(self):
        return True

    def plot(self, graph):
        """Plot this leaf on the given graphviz graph object."""
        label = f"{self.count},{self.char}"
        graph.node(str(id(self)), label)  # Add this leaf to the graph


class HuffmanTree:
    """Operations on an entire Huffman coding tree."""
    def __init__(self, root=None):
        """Initialise the tree, given its root. If root is None,
           the tree should then be built using one of the build methods.
        """
        self.root = root

    def _build_code_map(self):
        """Return dict mapping char -> bitstring by traversing the tree."""
        if self.root is None:
            raise ValueError("HuffmanTree has no root; build the tree first.")

        codes = {}

        # Edge case: tree with a single leaf → assign '0' as its code
        if self.root.is_leaf():
            codes[self.root.char] = '0'
            return codes

        def dfs(node, prefix):
            if node.is_leaf():
                # Assign current path as code for this character
                codes[node.char] = prefix or '0'  # safety for single-node trees
                return
            dfs(node.left, prefix + '0')
            dfs(node.right, prefix + '1')

        dfs(self.root, '')
        return codes

    def encode(self, text):
        """Return the binary string of '0' and '1' characters that encodes the
           given string text using this tree.
        """
        if text == "":
            return ""

        code_map = self._build_code_map()

        # Ensure every character is encodable
        for ch in text:
            if ch not in code_map:
                raise ValueError(f"Character {ch!r} not present in Huffman tree.")

        # Concatenate codes
        return ''.join(code_map[ch] for ch in text)

    def decode(self, binary):
        """Return the text string that corresponds to the given binary string of
           0s and 1s, using this tree.
        """
        if self.root is None:
            raise ValueError("HuffmanTree has no root; build the tree first.")
        if binary == "":
            return ""

        # Single-leaf tree: every bit corresponds to that one character.
        if self.root.is_leaf():
            # Any sequence of bits decodes to repeated char; length equals bits count.
            return self.root.char * len(binary)

        out = []
        node = self.root
        for bit in binary:
            if bit == '0':
                node = node.left
            elif bit == '1':
                node = node.right
            else:
                raise ValueError(f"Invalid bit {bit!r}; expected '0' or '1'.")

            # When we hit a leaf, append its char and reset to root
            if node.is_leaf():
                out.append(node.char)
                node = self.root

        # If we finish on an internal node, the bitstring ended mid-symbol
        if not node.is_leaf() and node is not self.root:
            raise ValueError("Binary string ended in the middle of a codeword.")

        return ''.join(out)

    def plot(self):
        """Plot the tree using graphviz, rendering to a PNG image and
           displaying it using the default viewer.
        """
        if HAS_GRAPHVIZ:
            g = Graph()
            self.root.plot(g)
            g.render('tree', format='png', view=True)
        else:
            print("graphviz is not installed. Call to plot() aborted.")

    def __repr__(self):
        """A string representation of self, delegated to the root's repr method"""
        return repr(self.root)

    def build_from_freqs(self, freqs):
        """Define self.root to be the Huffman tree for encoding a set of characters,
           given a map from character to frequency.
        """
        import heapq

        # Step 1: Create initial heap of (count, min_char, Leaf)
        heap = [(count, char, Leaf(count, char)) for char, count in freqs.items()]
        heapq.heapify(heap)

        # Step 2: Build tree until one node remains
        while len(heap) > 1:
            # Get two trees with smallest frequency (ties broken by min_char)
            count1, min_char1, tree1 = heapq.heappop(heap)
            count2, min_char2, tree2 = heapq.heappop(heap)

            # Combine into a new Node
            new_node = Node(tree1, tree2)
            new_entry = (count1 + count2, min(min_char1, min_char2), new_node)

            # Push the new node back into the heap
            heapq.heappush(heap, new_entry)

        # Step 3: Final tree becomes root
        self.root = heap[0][2]

    def build_from_string(self, s):
        """Convert the string representation of a Huffman tree, as generated
           by its __str__ method, back into a tree (self). There are no syntax
           checks on s so it had better be valid!
        """
        s = s.replace('\n', '')  # Delete newlines
        s = re.sub(r'Node\(\d+,', r'Node(', s)  # Strip counts from Node(…, …)
        self.root = eval(s)


# --- Small demo ---
if __name__ == "__main__":
    # Example from the notes
    freqs = {'a': 9, 'b': 8, 'c': 15, 'd': 3, 'e': 5, 'f': 2}
    tree = HuffmanTree()
    tree.build_from_freqs(freqs)

    print("Tree:")
    print(tree)

    # Encode and decode a short message using the built tree
    msg = "face"
    bits = tree.encode(msg)
    back = tree.decode(bits)

    print("Message:", msg)
    print("Encoded:", bits)
    print("Decoded:", back)

    # Quick check
    assert back == msg
