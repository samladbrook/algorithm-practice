from data_structures.adjacency_list import adjacency_list  # Import adjacency list builder from sibling package


def dijkstra(adj_list, start):
    """
    Computes shortest paths from a starting vertex using Dijkstra's algorithm.
    """
    # Initialize distances (∞ for all except start) and parents
    distance = [float('inf')] * len(adj_list)
    parent = [None] * len(adj_list)
    distance[start] = 0

    # Priority queue (as a list for simplicity) storing (distance, vertex)
    pq = [(0, start)]

    # Main loop: process vertices in order of increasing distance
    while pq:
        # Get vertex with smallest known distance
        current_dist, u = min(pq)
        pq.remove((current_dist, u))

        # Skip if this distance is outdated
        if current_dist > distance[u]:
            continue

        # Relax edges from u to its neighbors
        for v, weight in adj_list[u]:
            if distance[v] > distance[u] + weight:
                distance[v] = distance[u] + weight
                parent[v] = u
                pq.append((distance[v], v))

    return parent, distance


# --- Test ---
if __name__ == "__main__":
    # Directed weighted graph with 3 vertices
    graph_string = """\
D 3 W
1 0 3
2 0 1
1 2 1
"""
    adj_list = adjacency_list(graph_string)
    print(dijkstra(adj_list, 1))  # Expected: shortest paths from vertex 1
    print(dijkstra(adj_list, 2))  # Expected: shortest paths from vertex 2
