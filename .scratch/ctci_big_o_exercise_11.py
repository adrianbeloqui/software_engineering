"""
Cracking the Coding Interview - 6th version - Big O - Exercise 11 - Page 57/58
"""

numChars = 26

def printSortedStrings(remaining: int, prefix: str = "") -> None:
    if remaining == 0:
        if isInOrder(prefix):
            print(prefix)
    else:
        for index in range(numChars):
            char = ithLetter(index)
            printSortedStrings(remaining - 1, prefix + char)

def isInOrder(s: str) -> bool:
    for index, _ in enumerate(s):
        prev = ithLetter(index - 1)
        curr = ithLetter(index)
        if prev > curr:
            return False
    return True

def ithLetter(i: int) -> chr:
    return chr(ord("a") + i)

printSortedStrings(numChars)
