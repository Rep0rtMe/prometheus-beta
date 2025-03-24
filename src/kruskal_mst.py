from typing import List, Tuple, Dict

class DisjointSet:
    """
    Disjoint Set (Union-Find) data structure to detect cycles in graph.
    """
    def __init__(self, vertices: int):
        """
        Initialize disjoint set with each vertex in its own set.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices
    
    def find(self, item: int) -> int:
        """
        Find the root of a set with path compression.
        
        :param item: Vertex to find the root for
        :return: Root of the set containing the vertex
        """
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]
    
    def union(self, x: int, y: int) -> bool:
        """
        Union of two sets with union by rank.
        
        :param x: First vertex
        :param y: Second vertex
        :return: True if union is successful (no cycle), False otherwise
        """
        x_root = self.find(x)
        y_root = self.find(y)
        
        # If roots are same, a cycle is detected
        if x_root == y_root:
            return False
        
        # Union by rank
        if self.rank[x_root] < self.rank[y_root]:
            x_root, y_root = y_root, x_root
        
        self.parent[y_root] = x_root
        
        if self.rank[x_root] == self.rank[y_root]:
            self.rank[x_root] += 1
        
        return True

def kruskal_minimum_spanning_tree(n: int, edges: List[Tuple[int, int, int]]) -> List[Tuple[int, int, int]]:
    """
    Find the Minimum Spanning Tree using Kruskal's Algorithm.
    
    :param n: Number of vertices
    :param edges: List of edges, where each edge is (u, v, weight)
    :return: List of edges in the Minimum Spanning Tree
    
    Time Complexity: O(E log E), where E is the number of edges
    Space Complexity: O(V), where V is the number of vertices
    
    Raises:
    - ValueError: If input is invalid
    """
    # Validate inputs
    if n <= 0:
        raise ValueError("Number of vertices must be positive")
    
    if not edges:
        return []
    
    # Sort edges by weight in ascending order
    sorted_edges = sorted(edges, key=lambda x: x[2])
    
    # Initialize Disjoint Set
    disjoint_set = DisjointSet(n)
    
    # Store Minimum Spanning Tree edges
    mst_edges = []
    
    # Process edges
    for u, v, weight in sorted_edges:
        # Check if adding this edge creates a cycle
        if disjoint_set.union(u, v):
            mst_edges.append((u, v, weight))
        
        # Stop when MST is complete (n-1 edges)
        if len(mst_edges) == n - 1:
            break
    
    return mst_edges