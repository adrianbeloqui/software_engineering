"""
Insertion:


You are given two 32-bit numbers, N and M, and two bit positions, i and j.
Write a method to insert M into N such that M starts at bit j and ends at bit i. You
can assume that the bits j through i have enough space to fit all of M. That is, if
M = 10022, you can assume that there are at least 5 bits between j and i. You would not, for
example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.

EXAMPLE

Input: N = 10000000000, M = 10011, i = 2, j = 6
Output: N = 10001001100
"""
import math

def insertion(N: int, M: int, i: int, j: int) -> int:
    for ith in range(i, j+1):
        N = clearBit(N, ith)
    return N | (M << i)

def clearBit(num: int, i: int) -> int:
    mask = ~(1 << i)
    return num & mask

def test():
    test_cases = [
        ([int(math.pow(2, 10)), 19, 2, 6], int("10001001100", 2)),
        ((int("11111111111", 2), int("10011", 2), 2, 6), int("11111001111", 2))
    ]

    for t in test_cases:
        expected = t[1]
        args = t[0]
        print(f"Args in integers: {args}")
        print(f"Input: N = {args[0]:b}, M = {args[1]:b}, i = {args[2]}, j = {args[3]}")
        result = insertion(*args)
        print(f"Output: N = {result:b}")
        print(f"Valid: {result == expected}", end="\n\n")

test()
