import pytest
from src.edmonds_karp_max_flow import edmonds_karp_max_flow

def test_simple_flow():
    """Test a simple graph with a clear maximum flow."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    assert edmonds_karp_max_flow(graph, 0, 5) == 10

def test_disconnected_graph():
    """Test a graph where there's no path from source to sink."""
    graph = {
        0: {1: 10},
        1: {0: 10},
        2: {3: 5},
        3: {2: 5}
    }
    assert edmonds_karp_max_flow(graph, 0, 3) == 0

def test_complex_flow():
    """Test a more complex graph with multiple potential paths."""
    graph = {
        0: {1: 3, 2: 3},
        1: {2: 1, 3: 3},
        2: {3: 2, 4: 2},
        3: {4: 3, 5: 2},
        4: {5: 3},
        5: {}
    }
    assert edmonds_karp_max_flow(graph, 0, 5) == 3

def test_single_edge_graph():
    """Test a graph with just one edge."""
    graph = {
        0: {1: 5},
        1: {}
    }
    assert edmonds_karp_max_flow(graph, 0, 1) == 5

def test_invalid_source_or_sink():
    """Test that an error is raised when source or sink is not in graph."""
    graph = {
        0: {1: 10},
        1: {}
    }
    with pytest.raises(ValueError):
        edmonds_karp_max_flow(graph, 2, 1)
    with pytest.raises(ValueError):
        edmonds_karp_max_flow(graph, 0, 2)

def test_symmetric_flow():
    """Test a symmetric graph where multiple paths exist."""
    graph = {
        0: {1: 10, 2: 10},
        1: {2: 2, 3: 4, 4: 8},
        2: {4: 9},
        3: {5: 10},
        4: {3: 6, 5: 10},
        5: {}
    }
    result = edmonds_karp_max_flow(graph, 0, 5)
    assert result == 10