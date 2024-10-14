"""
String Rotation

Assume you have a method isSubstring which checks if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call
to isSubstring (e.g., "waterbottle" is a rotation of "erbottlewat")
"""
from collections import namedtuple

TestCase = namedtuple('TestCase', ['args', 'expected'])

def string_rotation(s1: str, s2: str) -> bool:
    super_s3 = s2 * 2
    if is_substring(s1, super_s3):
        return True
    return False

def is_substring(s1: str, s2: str) -> bool:
    return s1 in s2

def test():
    test_cases = [
        TestCase(["bottlewater", "erbottlewat"], True),
        TestCase(["myhouse", "notasubstring"], False),
        TestCase(["thekittycat", "tycatthekit"], True),
        TestCase(["thesunisout", "outthesunis"], True),
    ]
    for test in test_cases:
        result = string_rotation(*test.args)
        assert result == test.expected

test()