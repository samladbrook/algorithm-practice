from data_structures.adjacency_list import adjacency_list  # Import adjacency list builder from sibling package


def initial_distance_matrix(adj_list):
    """
    Creates the initial distance matrix from an adjacency list.
    """
    num_ver = len(adj_list)
    # Initialize all distances to infinity
    matrix = [[float('inf')] * num_ver for _ in range(num_ver)]

    # Distance from a vertex to itself is always 0
    for j in range(num_ver):
        matrix[j][j] = 0

    # Fill matrix with edge weights from adjacency list
    for i in range(num_ver):
        for v, weight in adj_list[i]:
            matrix[i][v] = weight

    return matrix


def floyd(distance):
    """
    Floyd–Warshall algorithm for all-pairs shortest paths.
    """
    # Make a deep copy so original distance matrix remains unchanged
    new_distance = [row.copy() for row in distance]
    n = len(new_distance)

    # Triple nested loop: try each vertex as an intermediate point
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # If a shorter path is found via k, update the distance
                if new_distance[i][j] > new_distance[i][k] + new_distance[k][j]:
                    new_distance[i][j] = new_distance[i][k] + new_distance[k][j]

    return new_distance


# --- Test ---
if __name__ == "__main__":
    # Directed weighted graph with 3 vertices
    graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""
    # Build adjacency list
    adj_graph = adjacency_list(graph_str)

    # Create initial distance matrix
    matrix = initial_distance_matrix(adj_graph)

    print("Initial distance matrix:")
    print(matrix)

    # Run Floyd–Warshall
    shortest_paths = floyd(matrix)

    print("Shortest path distances:")
    print(shortest_paths)

    print("Final distance matrix (should be unchanged):")
    print(matrix)  # matrix stays the same because floyd() returns a copy
