"""
Cracking the Coding Interview - 6th version - Big O - Example 12 - Page 51
"""

def permutations(string: str, prefix: str) -> None:
    if len(string) == 0:
        print(prefix)
    else:
        for index, value in enumerate(string):
            rem = string[0:index] + string[index + 1:]
            print(f"calling permutations({rem}, {prefix + value})")
            permutations(rem, prefix + value)


permutations("abc", ";")
