"""
Flip Bit to Win:

You have an integer and you can flip exactly one bit from 0 to a 1.
Write code to find the length of the longest sequence of 1s you could create.

EXAMPLE

Input: 1775 (or: 11011101111)
Output: 8
"""

def count_bits(n: int) -> int:
    bits = 0
    while n > 0:
        bits += 1
        n //= 2
    return bits

def flip2win(n: int) -> int:
    """With this implementation you try all possible permutations
    by finding the longest sequence for each bit until the longest
    sequence becomes larger than the remaining bits to iterate
    """
    longest, current, flipped = 0, 0, False
    for _ in range(count_bits(n)):
        # Shift right n by the number of bits we have iterated through already
        tmp_n = n >> _
        current = 0
        # Count longest sequence of 1s with 1 flip allowed
        while tmp_n > 0:
            # Get bit 1 or 0
            if tmp_n % 2:
                current += 1
            elif flipped is False:
                current += 1
                flipped = True
            else:
                longest = max(longest, current)
                flipped = False
                break

            longest = max(longest, current)
            tmp_n //= 2

        # Small optimization
        # If the itered bits is equal or larger than the largest sequence found
        # then, it is impossible to get a bigger sequence of 1s for the remaining
        # bits
        if longest <= _:
            break
    return longest

# print(flip2win(109))

def flip2win2(n: int) -> int:
    """With this implementation you loose track of the location in the bits
    so for a number like 109 (1101101) you get longest path is 4 when in reality it is 5
    """
    longest, current, flipped = 0, 0, False
    while n > 0:
        if n & 1:
            current += 1
            n = n >> 1
        else:
            if not flipped:
                current += 1
                flipped = True
                n = n >> 1
            else:
                longest = max(current, longest)
                flipped = False
                current = 0
    return longest

# print(flip2win2(109))

def flip2win3(n: int) -> int:
    bit_count = count_bits(n)
    original_bit_count = bit_count
    longest, current, flipped = 0, 0, False

    while bit_count > 0:
        if (n >> (original_bit_count - bit_count)) & 1:
            current += 1
        else:
            if flipped is False:
                temp_bit_count = bit_count
                flipped = True
                current += 1
            else: # bit was flipped once already
                bit_count = temp_bit_count  # rewind search
                flipped = False
                current = 0
        bit_count -= 1

        longest = max(current, longest)

    return longest

print(flip2win3(109))
