"""
Conversion:

Write a function to determine the number of bits you would need to flip to convert
integer A to integer B

EXAMPLE

Input: 29 (or: 11101), 15 (or: 01111)
Output: 2
"""

def flips_to_convert(a: int, b: int) -> int:
    """
    Note: this implementation is not the most efficient.

    The official implementation uses the equation c = c & (c - 1)
    to reduce the number of iterations by just iterating by the amount
    of bits set to one from least siginificant to most significant since
    that equation removes the least segnificiant bit set to 1 from c
    """
    count = 0
    while b > 0 or a > 0:
        if (a & 1) ^ (b & 1):
            # Different bits
            count += 1
        a = a >> 1
        b = b >> 1
    return count

def test():
    test_cases = [
        [(int("11101", 2), int("01111", 2)), 2],
        [(int("10000", 2), int("01111", 2)), 5],
    ]
    for test in test_cases:
        args = test[0]
        expected = test[1]
        print(f"Input: a = {args[0]:b}, b = {args[1]:b}")
        result = flips_to_convert(args[0], args[1])
        print(f"Output: {result}")
        print(f"Valid output: {expected == result}", end="\n\n")

test()
