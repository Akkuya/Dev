matrix =   [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
from typing import TypeVar

Element = TypeVar("Element", int, str)
def rotate_matrix(matrix: list[list[Element]]) -> list[list[Element]]:
    """
    
    Mutates? NO
    """
    new_matrix = []
    for i in range(len(matrix[0])):
        new_row = []
        for j in range(len(matrix) - 1, -1, -1):
            new_row.append(matrix[j][i])
        new_matrix.append(new_row)
    return new_matrix

print(rotate_matrix(matrix))
