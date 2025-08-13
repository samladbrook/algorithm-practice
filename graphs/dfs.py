from data_structures.adjacency_list import adjacency_list  # Import adjacency list builder from sibling package

def dfs_tree(adj_list, start):
    """
    Builds a DFS (Depth-First Search) tree from a given adjacency list.
    """
    parent = [None] * len(adj_list)   # Will store DFS tree parents
    visited = [False] * len(adj_list) # Track visited vertices

    def dfs(v):
        """Recursive DFS that explores as deep as possible before backtracking."""
        visited[v] = True
        # Explore each neighbor of the current vertex
        for neighbor, weight in adj_list[v]:
            if not visited[neighbor]:
                parent[neighbor] = v  # Record parent when discovering a new vertex
                dfs(neighbor)         # Recurse into neighbor

    dfs(start)  # Start DFS from the given starting vertex
    return parent


# --- Test ---
if __name__ == "__main__":
    # Simple directed, weighted graph with 2 vertices and one edge 0 -> 1 (weight 99)
    graph_string = """\
D 2 W
0 1 99
"""
    # Build adjacency list, then run DFS starting from vertex 0
    print(dfs_tree(adjacency_list(graph_string), 0))  # Expected: [None, 0]
