"""
Check Permutations:

Given two strings, write a method to decide if one is a permutation of the other

Assumptions:

- Two equal strings are not permutations of each other
- two strings of different length are not permutations of each other
- strings do not contain spaces
"""

def check_permutation(string1: str, string2: str) -> bool:
    """Brute force approach - first implementation
    O(n log n)
    """

    # Assuming we are looking for permutations that don't take equality as a permutation
    if string1 == string2 or len(string1) != len(string2):
        return False

    string2 = [char for char in string2] # O(n)
    string2.sort() # O(n log n)

    string1 = [char for char in string1] # O(n)
    string1.sort() # O(n log n)

    return ''.join(string1) == ''.join(string2)

assert check_permutation("aaa", "aaa") is False
assert check_permutation("abc", "cba") is True
assert check_permutation("abc", "jdf") is False
assert check_permutation("opq", "rst") is False


def check_permutation2(string1: str, string2: str) -> bool:
    """Second approach - space vs runtime tradeoff
    O(n)
    """

    # Assuming we are looking for permutations that don't take equality as a permutation
    if string1 == string2 or len(string1) != len(string2):
        return False

    string2 = {char: True for char in string2} # O(n)

    for char in string1:
        if string2.get(char, None) is None:
            return False

    return True

assert check_permutation2("aaa", "aaa") is False
assert check_permutation2("abc", "cba") is True
assert check_permutation2("abc", "jdf") is False
assert check_permutation2("opq", "rst") is False
