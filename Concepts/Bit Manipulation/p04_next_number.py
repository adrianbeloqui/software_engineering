"""
Next Number:

Given a positive integer, print the next smallest and the next largest number that
have the same number of 1 bits in their binary representation
"""

def count_bits(n: int) -> int:
    bits = 0
    while n > 0:
        bits += 1
        n //= 2
    return bits

def next_number(n: int) -> None:
    """"
    THIS IMPLEMENTATION OF THE ALGORITHM IS NOT CORRECT
    """
    next_largest = get_next(n, smallest=False)
    next_smallest = get_next(n, smallest=True)
    print(f"Next largest is: {next_largest} and in binary {next_largest:b}")
    print(f"Next smallest is: {next_smallest} and in binary {next_smallest:b}")
    print(f"Original number is: {n} and in binary {n:b}")

def get_next(n: int, smallest=True) -> int:
    bit_count = count_bits(n)
    flipped = False
    args = []
    if smallest:
        args = [bit_count -1, 0, -1]
    else:
        args = [bit_count]
    for ith in range(*args):
        if ((n >> ith) & 1) and flipped is False:
            n = clear_ith_bit(n, ith)
            flipped = True
        elif flipped is True:
            n = set_ith_bit(n, ith)
            break
    return n

def clear_ith_bit(n: int, i: int) -> int:
    mask = ~(1 << i)
    return n & mask

def set_ith_bit(n: int, i: int) -> int:
    mask = 1 << i
    return n | mask

next_number(0b10110)
