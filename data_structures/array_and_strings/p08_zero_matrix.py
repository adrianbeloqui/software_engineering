"""
Zero Matrix:

Write an algorithm such that if an element in an MxN matrix is 0, its entire row and column are set to 0
"""
from collections import namedtuple

TestCase = namedtuple('TestCase', ['args', 'expected'])

def zero_matrix(matrix: list) -> list:
    n = len(matrix)
    m = len(matrix[0])
    found_cero = False
    columns = []
    rows = []

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                found_cero = True
                columns.append(j)
                rows.append(i)

    if found_cero:
        for col in columns:
            for i in range(n):
                matrix[i][col] = 0

        for row in rows:
            for j in range(m):
                matrix[row][j] = 0

    return matrix


def test():
    test_cases = [
        TestCase([[1,2,3], [4,0,6], [7,8,9]], [[1,0,3], [0,0,0], [7,0,9]]),
        TestCase([[1,0], [2,4]], [[0, 0], [2,0] ]),
        TestCase([[1,2,3,7], [4,0,6,9]], [[1,0,3,7], [0,0,0,0]]),
        TestCase([[1,2], [0,7], [4,8], [6,9]], [[0,2], [0,0], [0,8], [0,9]]),
    ]
    for test in test_cases:
        result = zero_matrix(test.args)
        assert result == test.expected

test()
