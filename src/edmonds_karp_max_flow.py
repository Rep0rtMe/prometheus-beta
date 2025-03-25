from typing import List, Dict
from collections import deque

def edmonds_karp_max_flow(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> int:
    """
    Implements the Edmonds-Karp algorithm to find the maximum flow in a network.
    
    Args:
        graph (Dict[int, Dict[int, int]]): Adjacency list representation of the graph.
                                           Keys are nodes, values are dictionaries of 
                                           adjacent nodes and their edge capacities.
        source (int): The source node from which flow originates.
        sink (int): The sink node where flow terminates.
    
    Returns:
        int: The maximum flow from source to sink.
    
    Raises:
        ValueError: If source or sink are not in the graph or if graph is invalid.
    """
    # Validate input graph
    if source not in graph or sink not in graph:
        raise ValueError("Source or sink node not in graph")
    
    # Create a deep copy of the graph to avoid modifying the original
    graph = {node: edges.copy() for node, edges in graph.items()}
    
    def bfs_find_path(graph: Dict[int, Dict[int, int]], source: int, sink: int) -> List[int]:
        """
        Find an augmenting path using Breadth-First Search.
        
        Args:
            graph (Dict[int, Dict[int, int]]): Residual graph.
            source (int): Start node.
            sink (int): End node.
        
        Returns:
            List[int]: Path from source to sink, or empty list if no path exists.
        """
        # Track parent nodes for path reconstruction
        parent = {source: None}
        queue = deque([source])
        
        while queue:
            current = queue.popleft()
            
            # If we've reached the sink, reconstruct and return the path
            if current == sink:
                path = []
                while current is not None:
                    path.append(current)
                    current = parent[current]
                return list(reversed(path))
            
            # Explore neighbors with remaining capacity
            for neighbor, capacity in graph.get(current, {}).items():
                if capacity > 0 and neighbor not in parent:
                    parent[neighbor] = current
                    queue.append(neighbor)
        
        return []  # No path found
    
    max_flow = 0
    
    # Keep finding augmenting paths
    while True:
        # Find an augmenting path
        path = bfs_find_path(graph, source, sink)
        
        # If no path exists, we're done
        if not path:
            break
        
        # Find the minimum edge capacity along the path
        path_flow = float('inf')
        for i in range(len(path) - 1):
            current, next_node = path[i], path[i+1]
            path_flow = min(path_flow, graph[current].get(next_node, 0))
        
        # Add to max flow
        max_flow += path_flow
        
        # Update graph capacity
        for i in range(len(path) - 1):
            current, next_node = path[i], path[i+1]
            
            # Reduce edge capacity
            graph[current][next_node] -= path_flow
            
            # Add reverse edge if it doesn't exist
            if next_node not in graph:
                graph[next_node] = {}
            if current not in graph[next_node]:
                graph[next_node][current] = 0
            graph[next_node][current] += path_flow
            
            # Remove zero-capacity edges to prevent reusing 
            if graph[current][next_node] == 0:
                del graph[current][next_node]
    
    return max_flow