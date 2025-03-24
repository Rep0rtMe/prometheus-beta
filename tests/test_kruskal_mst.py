import pytest
from src.kruskal_mst import kruskal_minimum_spanning_tree, DisjointSet

def test_disjoint_set():
    """Test the DisjointSet data structure."""
    ds = DisjointSet(5)
    
    # Test initial state
    assert ds.find(0) != ds.find(1)
    
    # Test union and find
    assert ds.union(0, 1) == True
    assert ds.find(0) == ds.find(1)
    
    # Test cycle detection
    assert ds.union(0, 1) == False

def test_kruskal_simple_graph():
    """Test Kruskal's algorithm on a simple graph."""
    n = 4
    edges = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    
    mst = kruskal_minimum_spanning_tree(n, edges)
    
    # Expected MST edges (may vary, but total weight should be minimal)
    expected_mst_edges = [
        (2, 3, 4),
        (0, 3, 5),
        (0, 1, 10)
    ]
    
    # Check MST properties
    assert len(mst) == n - 1
    
    # Check that the MST contains the expected edges (order might differ)
    mst_set = set((u, v, w) for u, v, w in mst)
    expected_set = set((u, v, w) for u, v, w in expected_mst_edges)
    assert mst_set == expected_set

def test_kruskal_empty_graph():
    """Test Kruskal's algorithm with no edges."""
    n = 5
    edges = []
    
    mst = kruskal_minimum_spanning_tree(n, edges)
    assert mst == []

def test_kruskal_single_vertex():
    """Test Kruskal's algorithm with a single vertex."""
    n = 1
    edges = []
    
    mst = kruskal_minimum_spanning_tree(n, edges)
    assert mst == []

def test_kruskal_invalid_input():
    """Test Kruskal's algorithm with invalid inputs."""
    with pytest.raises(ValueError):
        kruskal_minimum_spanning_tree(0, [])
    
    with pytest.raises(ValueError):
        kruskal_minimum_spanning_tree(-1, [])

def test_kruskal_disconnected_graph():
    """Test Kruskal's algorithm on a disconnected graph."""
    n = 6
    edges = [
        (0, 1, 1),
        (2, 3, 2),
        (4, 5, 3)
    ]
    
    mst = kruskal_minimum_spanning_tree(n, edges)
    
    # Total number of MST edges should be the number of components
    assert len(mst) == 3