"""
Pairwise swap:

Write a program to swap odd and even bits in an integer with as few instructions as possible.
(e.g., bit 0 and bit 1 are swapped, bit 2 and bit 3 are swapped, and so on)
"""

def swap_bits2(n: int) -> int:
    seq_10 = 0xAAAAAAAA # 32 bits
    seq_01 = 0x55555555 # 32 bits
    evens = n & seq_10
    odds = n & seq_01
    n = (evens >> 1) | (odds << 1)
    return n

def swap_bits(n: int) -> int:
    # all 1s or all 0s
    if n == 0 or ((n + 1) & n) == 0:
        return n

    bit_count = count_bits(n)
    for i in range(0, bit_count, 2):
        ith = get_bit(n, i)
        next_ith = get_bit(n, i + 1)
        if ith != next_ith:
            clear_mask = ~(3 << i)
            n = clear_mask & n
            tmp_n = (ith << (i + 1)) | (next_ith << i)
            n = n | tmp_n
    return n

def count_bits(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n //= 2
    return count

def get_bit(n: int, i: int) -> int:
    mask = (1 << i)
    if (n & mask) > 0:
        return 1
    return 0

def test():
    test_cases = [
        (1,1),
        (0,0),
        (3,3),
        (7,7),
        (int("10", 2), int("01", 2)),
        (int("101", 2), int("1010", 2)),
        (int("1010", 2), int("101", 2)),
        (int("1011001010", 2), int("0111000101", 2)),
    ]

    for test in test_cases:
        arg = test[0]
        expected = test[1]
        print(f"Input: n = {arg}, binary = {arg:b}")
        output = swap_bits(arg)
        print(f"Output: {output}, binary = {output:b}")
        print(f"Valid: {expected == output}", end="\n\n")

test()
