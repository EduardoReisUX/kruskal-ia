import pytest
from ..busca_profundidade.index import dfs

example_graph1 = {
    5: [3, 7],
  3: [2, 4],
  7: [8],
  2: [],
  4: [8],
  8: []
}

visited = []

@pytest.fixture(autouse=True)
def run_before_each_test():
    visited.clear()

def test_exemplo_1():
    assert dfs(visited, example_graph1, 5) == [5, 3, 2, 4, 8, 7]


