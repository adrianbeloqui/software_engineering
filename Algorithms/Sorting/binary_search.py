# The Binary Search algorithm works as follows:
# 1. Set the search space equal to the sorted array
# 2. Find midpoint in array (length divided by 2 and choose the floor of the division)
# 3. Take the middle element of the search space and compare it to the target value.
#    - If the target equals the middle element, you have found the target value.
#      Return the index of the middle element and terminate the function.
#    - If the target is smaller than the middle element, halve the search space by
#      discarding all elements to the right of the middle element and continue the
#      search on its left side because the array is sorted in ascending order.
#      Repeat this step until the target is found.
#    - If the target is greater than the middle element, halve the search space by
#      discarding all elements to the left of the middle element and continue the search
#      on its right side because the array is sorted in ascending order.
#    - Repeat this step until the target is found.
# 4. If there’s no match in the array, return -1

import math

def recursive_binary_search(array: list, value: any) -> int:
    """Binary Search Algorithm - Recursive approach

    This approach focuses on determining if the element is found or not in the array,
    the actual index of the element is not tracked.
    """

    midpoint = math.floor(len(array)/2)

    if midpoint == 0:
        return -1

    midpoint_element = array[midpoint]
    if midpoint_element == value:
        return midpoint

    if midpoint_element > value:
        return recursive_binary_search(array[0:midpoint], value)

    return recursive_binary_search(array[midpoint:], value)

def recursive_binary_search2(array: list, value: any, start: int, end: int) -> int:
    """Binary Search Algorithm - Recursive approach 2

    This approach focuses on being able to return the index of the element found
    """
    if start > end or (start == end and array[start] != value):
        return -1

    midpoint = math.floor((start + end)/2)

    if array[midpoint] == value:
        return midpoint

    if array[midpoint] > value:
        return recursive_binary_search2(array, value, start, midpoint - 1)

    return recursive_binary_search2(array, value, midpoint + 1, len(array) - 1)

def nonrecursive_binary_search(array: list, value: any) -> int:
    """Binary Search Algorithm - Non-recursive approach"""
    start = 0
    end = len(array) - 1

    while start <= end:
        midpoint = math.floor((start + end)/2)
        if array[midpoint] == value:
            return midpoint
        if array[midpoint] > value:
            end = midpoint - 1
        else:
            start = midpoint + 1

    return -1

def run():
    """Run method for multiple test cases"""

    # lists must be sorted
    cases = [
        [1, 2, 3, 56, 89, 100, 123, 345],
        [1, 21, 33, 56, 89, 101, 123, 345]
    ]
    print("Recursive Approach 1")
    for case in cases:
        print(case)
        found_element = recursive_binary_search(case, 100)
        print("Not found!") if found_element == -1 else print("Found element")
        print()

    print("Recursive Approach 2")
    for case in cases:
        print(case)
        element_index = recursive_binary_search2(case, 100, 0, len(case) - 1)
        print("Not found!") if element_index == -1 else print(f"Found element on index {element_index}")
        print()

    print("Non-recursive Approach 2")
    for case in cases:
        print(case)
        element_index = nonrecursive_binary_search(case, 100)
        print("Not found!") if element_index == -1 else print(f"Found element on index {element_index}")
        print()

run()
