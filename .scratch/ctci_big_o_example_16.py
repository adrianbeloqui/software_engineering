"""
Cracking the Coding Interview - 6th version - Big O - Example 16 - Page 54
"""

def powersOf2(n: int) -> int:
    if n < 1:
        return 0

    if n == 1:
        print(1)
        return 1

    next = n // 2
    print(f"-> call powersOf2({next})")
    prev = powersOf2(next)
    curr = prev * 2
    print(f"-> powersOf2({next}) -> {curr}")
    return curr



powersOf2(7)
