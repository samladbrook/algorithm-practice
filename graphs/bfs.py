from collections import deque
from data_structures.adjacency_list import adjacency_list  # Import adjacency list builder from sibling package


def bfs_tree(adj_list, start):
    """
    Builds a BFS (Breadth-First Search) tree from a given adjacency list.
    """
    n = len(adj_list)                     # Number of vertices
    parent_array = [None] * n              # Will store BFS tree parents
    visited = [False] * n                  # Track visited vertices

    # BFS uses a queue — start by adding the root vertex
    queue = deque([start])
    visited[start] = True                  # Mark the start node as visited

    # Standard BFS loop
    while queue:
        node = queue.popleft()             # Dequeue the next vertex

        # Iterate through all neighbors of the current vertex
        for neighbour, weight in adj_list[node]:
            if not visited[neighbour]:     # If this neighbor hasn't been visited yet
                visited[neighbour] = True
                parent_array[neighbour] = node  # Record how we reached this vertex
                queue.append(neighbour)    # Add neighbor to the queue

    return parent_array


# --- Test ---
if __name__ == "__main__":
    # Simple directed, weighted graph with 2 vertices and one edge 0 -> 1 (weight 99)
    graph_string = """\
D 2 W
0 1 99
"""
    # Build adjacency list, then run BFS starting from vertex 0
    print(bfs_tree(adjacency_list(graph_string), 0))  # Expected output: [None, 0]
