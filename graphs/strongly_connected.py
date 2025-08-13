from data_structures.adjacency_list import adjacency_list  # Use shared graph parser


def is_strongly_connected(adj_list):
    """
    Check if a directed graph is strongly connected using two DFS passes.
    """
    num_nodes = len(adj_list)
    if num_nodes == 0:
        return True  # Vacuously true for empty graph

    # ---------- Pass 1: reachability in the original graph ----------
    visited = set()
    stack = [0]  # Start from vertex 0 (arbitrary choice)
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            # Add unvisited neighbors
            neighbors = {nbr for nbr, _ in adj_list[node]}
            stack.extend(neighbors - visited)

    if len(visited) != num_nodes:
        return False  # Not all nodes reachable from 0

    # ---------- Build transpose (reverse all edges) ----------
    transposed = [set() for _ in range(num_nodes)]
    for u in range(num_nodes):
        for v, _ in adj_list[u]:
            transposed[v].add(u)

    # ---------- Pass 2: reachability in the transposed graph ----------
    visited.clear()
    stack = [0]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(transposed[node] - visited)

    # If 0 reaches everyone in the transpose, every node can reach 0 in original.
    # Combined with pass 1, this implies mutual reachability for all pairs.
    return len(visited) == num_nodes


# --- Test ---
if __name__ == "__main__":
    graph_string = """\
D 3
0 1
1 0
0 2
"""
    # Expected: False (vertex 2 cannot reach others)
    print(is_strongly_connected(adjacency_list(graph_string)))
