def connected_components(physical_contact_info):
    """
    Finds connected components (or "bubbles") in an undirected contact graph.
    """
    lines = physical_contact_info.splitlines()
    first_line = lines[0].split()

    # Number of vertices in the graph
    num_vertices = int(first_line[1])

    # Initialize adjacency list for all vertices
    graph = {i: [] for i in range(num_vertices)}

    # Read edges and populate adjacency list
    for line in lines[1:]:
        parts = line.split()
        u, v = int(parts[0]), int(parts[1])

        # Ensure both vertices exist in the graph
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []

        # Add undirected edge (both directions)
        graph[u].append(v)
        graph[v].append(u)

    visited = set()         # Track visited vertices
    components = []         # Store connected components

    def dfs(node, component):
        """Recursive DFS to collect all vertices in the same component."""
        visited.add(node)
        component.add(node)
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                dfs(neighbour, component)

    # For each vertex, run DFS if not already visited
    for vertex in graph:
        if vertex not in visited:
            component = set()
            dfs(vertex, component)
            components.append(component)

    return components


# --- Test ---
if __name__ == "__main__":
    # Example: Graph with 1 vertex and no edges
    physical_contact_info = """\
U 1
"""
    # Sort each component and then sort the list of components for consistent output
    print(sorted(sorted(component) for component in connected_components(physical_contact_info)))
    # Expected: [[0]]
