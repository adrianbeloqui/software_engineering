"""
Palindrome Permutation:

Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards.
A permutation is a rearrengement of letters. The palindrome does not need to be
limited to just dictionary words

From the solutions in CtCi we learned after implementing the brute force approach:

Strings with even length (after removing all non-letter characters) must have all even counts of characters.
Strings of an odd length must have exactly one character with and odd count.
To be a permutation of a palindrome, a string can have no more than one character that is odd.
This will cover both the odd and the even cases.

Refer to https://github.com/careercup/CtCI-6th-Edition-Python/blob/master/chapter_01/p04_palindrome_permutation.py
for provided solutions
"""
import unittest
from test_base_class import Test


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome"""
    replaced_s = s.replace(" ", "")
    return replaced_s.lower() == replaced_s[::-1].lower()

def find_permutations(s: str, prefix: str, permutations=[]) -> bool:
    """Find all permutations of a string and check if each one is a palindrome"""
    if s == "":
        if is_palindrome(prefix):
            return True


    for index, letter in enumerate(s):
        tmp_s = s[0:index] + s[index + 1:]
        found = find_permutations(tmp_s, prefix + letter, permutations)
        if found:
            return found

    return False

def check_permutations(s: str) -> bool:
    """Extremely inefficient approach. Find every permutation of s and test
    if such is a palindrome

    O(n!)
    """
    s = s.replace(" ", "")
    if is_palindrome(s):
        return True
    return find_permutations(s, "")


class TestThis(Test):
    test_cases = [
        (["aab"], True),
        (["Tact Coa"], True),
        (["abc"], False),
        (["tactcoapapa"], True)
    ]

    test_functions = [
        check_permutations
    ]


if __name__ == "__main__":
    unittest.main()
    # print(is_palindrome("aba"))
    # print(check_permutations("aab"))
    # print(check_permutations("Tact Coa"))
    # print(check_permutations("Tact Cof"))
