"""
One Away:

There are three types of edits that can be performed on strings: insert a character, remove a character, 
or replace a character. Given two strings, write a function to check if they are one edit (or zero edits) away.

EXAMPLE
pale, ple -> true
pales, pale -> true
pale, bale -> true
pale, bake -> false
"""

from collections import namedtuple

TestCase = namedtuple('TestCase', ['args', 'expected'])


def one_away(a: str, b: str) -> bool:
    """
    This algorithm does not take into account order of the string
    """
    # Assuming ASCII
    char_count = [0 for i in range(26)]
    ord_a = ord('a')
    for char in a:
        char_count[ord(char) - ord_a] += 1

    diff_char = 0
    for char in b:
        if char_count[ord(char) - ord_a] != 0:
            char_count[ord(char) - ord_a] -= 1
        else:
            diff_char += 1

    # sum(char_count) is 0 and diff is 0 -> a and b have the same characters and counts
    # sum(char_count) is 0 and diff is 1 -> b has the same characters and counts as a + 1 character
    # sum(char_count) is 1 and diff is 0 -> a has the same characters and counts as a + 1 character
    # sum(char_count) is 1 and diff is 1 -> a and b differ only in 1 character 
    if ((sum(char_count) == 0 or sum(char_count) == 1) and (diff_char == 0 or diff_char == 1)):
        return True

    return False


def one_away2(a: str, b: str) -> bool:
    """This algorithm takes into account order of characters"""
    if abs(len(a) - len(b)) > 1:
        return False

    found_difference = False
    shorter_str = a if len(a) < len(b) else b
    longer_str = b if len(a) < len(b) else a
    idx1 = 0
    idx2 = 0
    while idx2 < len(longer_str) or idx1 < len(shorter_str):
        if idx1 >= len(shorter_str) or shorter_str[idx1] != longer_str[idx2]:
            if found_difference:
                return False
            found_difference = True

            if len(longer_str) == len(shorter_str):
                idx1 += 1
        else:
            idx1 += 1
        idx2 += 1
    return True

def test():
    test_cases = [
        TestCase(["pale", "ple"], True),
        TestCase(["pales", "pale"], True),
        TestCase(["pale", "bale"], True),
        TestCase(["pale", "bake"], False),
        TestCase(["pale", "elab"], False),
    ]
    for test in test_cases:
        print(f"Input: {test.args}")
        result = one_away2(*test.args)
        print(f"Output: {result}")
        assert test.expected == result

test()
