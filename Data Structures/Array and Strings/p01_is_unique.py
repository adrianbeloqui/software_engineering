"""
Is Unique:

Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""
import math

def binary_search(array: list, value: any, min: int, max: int):
    if (min > max) or (min == max and value != array[min]):
        return -1
    mid = math.floor((min + max) / 2)
    if array[mid] == value:
        return mid
    elif array[mid] < value:
        return binary_search(array, value, mid + 1, max)
    return binary_search(array, value, min, mid - 1)

# This was the wrong approach using binary search, because the string is not sorted!!
# I would have to sort it first and then I could use a simpler algorithm to check 
# if neighboring characters in the array are different or not.
# def is_unique(string: str) -> bool: # O(n log n)
#     if string == "":
#         return True

#     for index, char in enumerate(string):
#         new_array = string[0:index] + string[index+1:]
#         if binary_search(new_array, char, 0, len(new_array) - 1) != -1:
#             return False
#     return True

def is_unique2(string: str) -> bool: # O(n) with a space vs runtime tradeoff
    if string == "":
        return True
    hashed = {char: True for char in string}
    return len(string) == len(hashed.keys())

def is_unique3(string: str) -> bool: # O(n) with a space vs runtime tradeoff
    if string == "":
        return True
    if len(string) > 128:
        return False

    ascii_values = [None] * 127
    for char in string:
        if ascii_values[ord(char)] is None:
            ascii_values[ord(char)] = True
        else:
            return False
    return True

# Implementation 1
#assert is_unique('') is True
#assert is_unique('abcd') is True
#assert is_unique('aabcd') is False

# Implementation 2
assert is_unique2('') is True
assert is_unique2('abcd') is True
assert is_unique2('aabcd') is False

# Implementation 3
assert is_unique3('') is True
assert is_unique3('abcd') is True
assert is_unique3('aabcd') is False
