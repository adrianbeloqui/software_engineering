"""
String Compression

Implement a method to perform basic string compression using the counts of repeated characters.
For example, the string aabcccccaaa would become a2b1c5a3. If the "compressed" string would not become
smaller than the original string, your method should return the original string. You can assume the
string has only uppercase and lowercase letters (a - z).
"""
from collections import namedtuple

TestCase = namedtuple('TestCase', ['args', 'expected'])

def compress(string: str) -> str:
    if len(string) == 0:
        return string

    compressed = []
    current_char = string[0]
    current_count = 1
    idx = 1
    while idx < len(string):
        if string[idx] == current_char:
            current_count += 1
        else:
            compressed.append(current_char)
            compressed.append(current_count)
            current_char = string[idx]
            current_count = 1
        idx += 1

    compressed.append(current_char)
    compressed.append(current_count)
    compressed = "".join(compressed)

    return (compressed if len(compressed) < len(string) else string)


def compress2(string: str) -> str:
    compressed = []
    compressed_length = 0
    current_count = 0
    idx = 0
    str_length = len(string)
    while idx < str_length:
        current_count += 1
        if (idx + 1) >= str_length or (string[idx + 1] != string[idx]):
            compressed.append(string[idx])
            value = str(current_count)
            compressed.append(value)
            current_count = 0
            compressed_length += 1 + len(value)
        idx += 1

    compressed = "".join(compressed)

    return (compressed if compressed_length < len(string) else string)

def test():
    test_cases = [
        TestCase("aabcccccaaa", "a2b1c5a3"),
        TestCase("abcde", "abcde"),
        TestCase("", ""),
        TestCase("fffgeeezzzziij", "f3g1e3z4i2j1"),
        TestCase("aabcdefgaheradfa", "aabcdefgaheradfa")
    ]

    for test in test_cases:
        result = compress2(test.args)
        print(f"Input: {test.args}")
        print(f"Output: {result}")
        assert test.expected == result

test()
