# Algorithms and Data Structures

Implementations of classic algorithms and data structures, written as part of my university algorithms course. Includes explanations and example usage.

## About
This repository contains a curated collection of algorithms and data structures implemented in Python. Each implementation is designed to be clean, well-documented, and easy to understand.

The goal is to provide a reference for myself, with code that is easy to run and adapt. But also to show my experience in playing with different algorithms

## Contents

### Sorting Algorithms
- **Quick Sort** – [sorting/quicksort.py](sorting/quicksort.py)  
  Efficient divide-and-conquer algorithm that partitions and recursively sorts subarrays.  
- **Merge Sort** – [sorting/mergesort.py](sorting/mergesort.py)  
  Stable divide-and-conquer algorithm that merges sorted halves of an array.  
- **Heap Sort** – [sorting/heapsort.py](sorting/heapsort.py)  
  Comparison-based sort using a binary heap to produce a sorted array in-place.  
- **Key Positions (Counting/Radix Helper)** – [sorting/key_positions.py](sorting/key_positions.py)  
  Helper function for position mapping in counting and radix sort.

---

### Graph Algorithms
- **Breadth-First Search (BFS)** – [graphs/bfs.py](graphs/bfs.py)  
  Level-order graph traversal using a queue.  
- **Depth-First Search (DFS)** – [graphs/dfs.py](graphs/dfs.py)  
  Recursive or stack-based traversal for exploring graph depth-first.  
- **Dijkstra’s Algorithm** – [graphs/dijkstra.py](graphs/dijkstra.py)  
  Finds shortest paths from a source to all vertices in a weighted graph.  
- **Floyd-Warshall Algorithm** – [graphs/floyd_warshall.py](graphs/floyd_warshall.py)  
  Computes shortest paths between all vertex pairs in a weighted graph.  
- **Topological Sort (Build Order)** – [graphs/build_order.py](graphs/build_order.py)  
  Produces an order of vertices for DAGs based on dependencies.  
- **Strongly Connected Components** – [graphs/strongly_connected.py](graphs/connected_components.py)  
  Identifies groups of vertices with mutual reachability.  
- **Connected Components** – [graphs/connected_components](graphs/adjacency_list.py)  
  Identifies all connected components.
- **Distance Matrix** – [graphs/distance_matrix.py](graphs/distance_matrix.py)  
  Gets the correct distance matrix from starting vertex.

---

### Dynamic Programming
- **0/1 Knapsack – Top Down (Memoization)** – [dynamic_programming/knapsack_top_down.py](dynamic_programming/knapsack_top_down.py)  
  Recursive knapsack solution with memoization.  
- **0/1 Knapsack – Bottom Up (Tabulation)** – [dynamic_programming/knapsack_bottom_up.py](dynamic_programming/knapsack_bottom_up.py)  
  Iterative DP solution for knapsack.  
- **Longest Common Subsequence (LCS)** – [dynamic_programming/lcs.py](dynamic_programming/lcs.py)  
  Finds the length of the longest subsequence present in both sequences.  
- **Minimum Cost Path - Bottom Up** – [dynamic_programming/min_cost_path_bottom_up.py](dynamic_programming/min_cost_path_bottom_up.py)  
  Iterative DP version for minimum path cost. 
- **Minimum Cost Path – Top Down** – [dynamic_programming/min_cost_path_top_down.py](dynamic_programming/min_cost_path_top_down.py)  
  Memoized recursive solution for minimum path cost.  

---

### Greedy Algorithms
- **Coin Change (Greedy)** – [greedy/coins_change.py](greedy/coins_change.py)  
  Selects largest coin denominations first to reach target sum.

---

### Data Structures
- **Adjacency List Representation** – [data_structures/adjacency_list.py](data_structures/adjacency_list.py)  
  Graph representation storing each vertex’s neighbours as a list for efficient traversal and edge lookups.  
- **Adjacency Matrix Representation** – [data_structures/adjacency_matrix.py](data_structures/adjacency_matrix.py)  
  Graph representation using a 2D matrix where cell `(i, j)` indicates the presence and weight of an edge.  
- **Huffman Tree** – [data_structures/huffman_tree.py](data_structures/huffman_tree.py)  
  Data compression tree structure generating optimal prefix codes to minimise encoding size.  
- **1D KD-Tree** – [data_structures/kd_tree_1d.py](data_structures/kd_tree_1d.py)  
  Space-partitioning data structure optimised for 1D nearest-neighbour and range search queries.  
- **2D KD-Tree** – [data_structures/kd_tree_2d.py](data_structures/kd_tree_2d.py)  
  Space-partitioning data structure for efficient 2D nearest-neighbour and range searches.  
- **Quad Tree** – [data_structures/quad_tree_class.py](data_structures/quad_tree_class.py)  
  Tree structure dividing 2D space into four quadrants recursively, used for spatial indexing and collision detection.  


---
