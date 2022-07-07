import pytest
from ..busca_largura.index import bfs

example_graph1 = {
    0: [1, 2],
    1: [3, 4],
    2: [5],
    3: [],
    4: [5],
    5: [],
}

example_graph2 = {
    1: [8, 5, 2],
    2: [9],
    3: [],
    4: [],
    5: [],
    6: [10, 7],
    7: [],
    8: [6, 4, 3],
    9: [],
    10: [],
}

example_graph3 = {
  0: [1],
  1: [2],
  2: [3, 5],
  3: [4],
  4: [],
  5: []
}

visited = []

@pytest.fixture(autouse=True)
def run_before_each_test():
    visited.clear()

def test_exemplo_1():
    assert bfs(visited, example_graph1) == [0, 1, 2, 3, 4, 5]

def test_exemplo_2():
    assert bfs(visited, example_graph2, 1) == [1, 8, 5, 2, 6, 4, 3, 9, 10, 7]

def test_exemplo_3():
    assert bfs(visited, example_graph3) == [0, 1, 2, 3, 5, 4]


