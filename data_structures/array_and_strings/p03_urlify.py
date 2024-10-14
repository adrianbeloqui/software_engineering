"""
URLify:

Write a method to replace all spaces in a string with "%20".
You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string.

Example:

Input: "Mr John Smith     ", 13
Output: "Mr%20John%20Smith"
"""

def urlify(string: str, length: str) -> str:
    """First approach

    O(n)
    """
    string = [char for char in string[:length]]
    index = 0
    while index <= length - 1:
        if string[index] == " ":
            string[index] = "%20"
        index += 1
    return ''.join(string)

assert urlify("Mr John Smith     ", 13) == 'Mr%20John%20Smith'
assert urlify("this is another test     ", 20) == 'this%20is%20another%20test'

def urlify2(string: str, length: str) -> str:
    """Second approach

    O(n)
    """
    string = string[:length]
    return string.replace(" ", '%20')

assert urlify2("Mr John Smith     ", 13) == 'Mr%20John%20Smith'
assert urlify2("this is another test     ", 20) == 'this%20is%20another%20test'

def urlify3(string: str, length: str) -> str:
    """Third approach copied from CtCi

    O(n)
    """
    space_count = 0
    for i in range(0, length):
        if string[i] == " ":
            space_count += 1

    # we need 2 more slots for each space found to change a space for %20
    index = length + (space_count * 2)
    new_string = [None] * index

    for i in range(length -1, -1, -1):
        if string[i] == ' ':
            new_string[index - 1] = '0'
            new_string[index - 2] = '2'
            new_string[index - 3] = '%'
            index -= 3
        else:
            new_string[index - 1] = string[i]
            index -= 1
    return ''.join(new_string)

assert urlify3("Mr John Smith     ", 13) == 'Mr%20John%20Smith'
assert urlify3("this is another test     ", 20) == 'this%20is%20another%20test'


def urlify4(string: str, length: str) -> str:
    """4th approach

    O(n)
    """
    space_count = 0
    for i in range(0, length):
        if string[i] == " ":
            space_count += 1

    # we need 2 more slots for each space found to change a space for %20
    final_length = length + (space_count * 2)

    cursor = 0
    while cursor < final_length:
        if string[cursor] == " ":
            string = string[0:cursor] + "%20" + string[cursor+1:]
            cursor += 3
        else:
            cursor += 1
    return string[:final_length]

assert urlify4("Mr John Smith     ", 13) == 'Mr%20John%20Smith'
assert urlify4("this is another test     ", 20) == 'this%20is%20another%20test'
