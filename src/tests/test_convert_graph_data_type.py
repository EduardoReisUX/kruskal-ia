from ..convert_graph_data_type import convert

example_data1 = [
    [1, 2, 2], 
    [2, 5, 2], 
    [2, 3, 3], 
    [3, 4, 3], 
    [0, 1, 4],
]

result_example_data1 = {
  1: [2],
  2: [5, 3],
  5: [],
  3: [4],
  4: [],
  0: [1],
} 

def test_exemplo_1():
    assert convert(example_data1, print_results=True) == result_example_data1
