def build_order(dependencies):
    """
    Computes a valid build order (topological sort) for a directed graph.
    """
    # Split into lines and parse the first line to get number of vertices
    lines = dependencies.splitlines()
    first_line = lines[0].split()
    num_vertices = int(first_line[1])

    # Build adjacency list as a dictionary
    graph = {}
    for line in lines[1:]:
        parts = line.split()
        u, v = int(parts[0]), int(parts[1])
        if u not in graph:
            graph[u] = []
        graph[u].append(v)

    # State array for DFS: "U" = unvisited, "D" = visiting, "P" = processed
    states = ['U'] * num_vertices
    results = []

    def dfs(graph, i, states, results):
        """Recursive DFS that adds vertices to results after exploring children."""
        states[i] = "D"  # Mark as visiting
        for v in graph.get(i, []):
            if states[v] == "U": 
                dfs(graph, v, states, results)
        states[i] = "P"  # Mark as processed
        results.append(i)

    # Run DFS from all unvisited vertices to cover disconnected components
    for i in range(num_vertices):
        if states[i] == "U":
            dfs(graph, i, states, results)

    # Reverse results to get correct topological order
    return results[::-1]


# --- Test ---
dependencies = """\
D 3
"""
# Any permutation of [0, 1, 2] is valid when there are no edges
solution = build_order(dependencies)
if solution is None:
    print("Wrong answer!")
else:
    print(sorted(solution))  # Expected: [0, 1, 2]
