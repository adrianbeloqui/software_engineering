"""
Rotate Matrix

Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method
to rotate the image by 90 degrees. Can you do this in place?

"""
from collections import namedtuple

TestCase = namedtuple('TestCase', ['args', 'expected'])


def rotate_matrix(matrix):
    """Super inefficient approach"""
    new_matrix = matrix[-1]
    for layer in range(len(matrix) -2, -1, -1):
        for idx, el in enumerate(matrix[layer]):
            if isinstance(new_matrix[idx], list):
                new_matrix[idx] = list(new_matrix[idx]) + list([el])
            else:
                new_matrix[idx] = [new_matrix[idx], el]
    return new_matrix


def test():
    test_cases = [
        TestCase([[1,2,3], [4,5,6], [7,8,9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
        TestCase([[1,3], [2,4]], [[2, 1], [4,3] ])
    ]
    for test in test_cases:
        result = rotate_matrix(test.args)
        assert result == test.expected

test()
