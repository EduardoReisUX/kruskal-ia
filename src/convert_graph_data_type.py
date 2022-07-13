from typing import Any
""" 
recebe [ 
    [1, 2, 2], 
    [2, 5, 2], 
    [2, 3, 3], 
    [3, 4, 3],
    [0, 1, 4],
] de result de kruskal.py

retorna { 
    1: [2], 
    2: [5, 3], 
    3: [4],
    0: [1],
    4: [],      
    5: [],      
} para breadth-search.py
"""

def convert(result: 'list[list[int]]', print_results: bool = False):
    # print a lista result que recebe como parâmetro
    if print_results == True:
        print("[")
        for arr in result:
            print(f"  {arr},")
        print("]\n")

    result_dict: dict[int, Any] = {}

    for array in result:
        array.pop()
        for value in array:
            result_dict.update({ value: [] })

    for i in range(len(result)):
        if result[i][0] == result[i-1][0]:
            valor_anterior: 'list[int]' = result_dict.get(result[i-1][0])
            valor_anterior.append(result[i][1])

            result_dict.update({ result[i][0]: valor_anterior })
        else:
            result_dict.update({ result[i][0]: [result[i][1]] })

    # print o resultado da conversão da lista para dict[int, Any]
    if print_results == True:
        print('{')
        for arr in result_dict:
            print(f'  {arr}: {result_dict[arr]},')
        print('}')

    return result_dict

