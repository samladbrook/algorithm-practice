def adjacency_matrix(graph_str):
    """Convert a graph string into an adjacency matrix.
    """
    # Split the graph string into lines and read the first line
    lines = graph_str.splitlines()
    first_line = lines[0].split()

    # Determine if the graph is directed or undirected
    directed = first_line[0] == "D"
    
    # Determine if the graph is weighted
    weighted = len(first_line) > 2 and first_line[2] == "W"

    # Number of vertices in the graph
    num_vertices = int(first_line[1])

    # Initialise adjacency matrix
    if weighted:
        # For weighted graphs: start with None (meaning no edge yet)
        matrix = [[None] * num_vertices for _ in range(num_vertices)]
    else:
        # For unweighted graphs: start with 0 (no edge)
        matrix = [[0] * num_vertices for _ in range(num_vertices)]

    # Process each edge line in the input
    for line in lines[1:]:
        parts = line.split()
        u, v = int(parts[0]), int(parts[1])
        
        # If weighted, parse the weight; otherwise default to 1
        weight = int(parts[2]) if weighted else 1
        
        # Set edge from u to v
        matrix[u][v] = weight
        
        # If undirected, also set edge from v to u
        if not directed:
            matrix[v][u] = weight

    return matrix


# Example usage:
graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""
print(adjacency_matrix(graph_string))
