def adjacency_list(graph_str):
    """
    Converts a graph description string into an adjacency list representation.
    """
    weighted = False
    lines = graph_str.splitlines()          # Split the graph description into lines
    first_line = lines[0].split()           # Parse the header line
    
    # Determine if the graph is directed
    directed = first_line[0] == "D"
    
    # Determine if the graph is weighted (optional third token "W")
    if len(first_line) > 2:
        if first_line[2] == "W":
            weighted = True
    
    # Number of vertices in the graph
    num_vertices = int(first_line[1])
    
    # Initialize an empty adjacency list (outer list with an empty list for each vertex)
    outer_list = [[] for _ in range(num_vertices)]
    
    # Process each edge line
    for line in lines[1:]:
        parts = list(line.split())
        u, v = int(parts[0]), int(parts[1])    # Extract vertex indices
        
        # Extract weight if graph is weighted
        weight = parts[2] if weighted and len(parts) > 2 else None
        if weighted and weight is not None:
            weight = int(weight)
        
        # Add edge from u to v
        outer_list[u].append((v, weight) if weighted else (v, None))
        
        # If undirected, add edge from v to u as well
        if not directed:
            outer_list[v].append((u, weight) if weighted else (u, None))
            
    return outer_list


# --- test ---
if __name__ == "__main__":
    # Example of an undirected, unweighted graph with 3 vertices
    graph_description = """\
U 3
0 1
1 2
"""
    adj_list = adjacency_list(graph_description)
    print("Adjacency List:", adj_list)
    # Expected:
    # [[(1, None)], [(0, None), (2, None)], [(1, None)]]
