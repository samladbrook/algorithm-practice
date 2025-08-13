def adjacency_list(graph_str):
    """Convert a graph string into an adjacency list.
    """
    # Split the graph string into lines and process the header
    lines = graph_str.splitlines()
    first_line = lines[0].split()

    # Determine if the graph is directed
    directed = first_line[0] == "D"

    # Determine if the graph is weighted
    weighted = len(first_line) > 2 and first_line[2] == "W"

    # Number of vertices
    num_vertices = int(first_line[1])

    # Initialise an empty adjacency list for each vertex
    outer_list = [[] for _ in range(num_vertices)]

    # Process each edge
    for line in lines[1:]:
        parts = line.split()
        u, v = int(parts[0]), int(parts[1])

        # If weighted, parse the weight; otherwise default to None
        weight = int(parts[2]) if weighted else None

        # Add edge u -> v
        outer_list[u].append((v, weight))

        # If undirected, also add v -> u
        if not directed:
            outer_list[v].append((u, weight))

    return outer_list


def initial_distance_matrix(adj_list):
    """Create an initial distance matrix from an adjacency list.
    """
    num_vertices = len(adj_list)

    # Start with infinity for all distances
    matrix = [[float('inf')] * num_vertices for _ in range(num_vertices)]

    # Distance from each vertex to itself is 0
    for v in range(num_vertices):
        matrix[v][v] = 0

    # Fill in distances from adjacency list
    for i, edges in enumerate(adj_list):
        for (u, weight) in edges:
            matrix[i][u] = weight

    return matrix


# Example usage
graph_str = """\
D 2 W
0 1 4
"""

adj_list = adjacency_list(graph_str)
print(initial_distance_matrix(adj_list))
