# Algorithm for Merge Sort

# Step 1: Find the middle index of the array. Middle = 1 + (last – first)/2
# Step 2: Divide the array from the middle.
# Step 3: Call merge sort for the first half of the array MergeSort(array, first, middle)
# Step 4: Call merge sort for the second half of the array. MergeSort(array, middle+1, last)
# Step 5: Merge the two sorted halves into a single sorted array.

import math

def merge(left_array: list, right_array: list) -> list:
    "Divide and Conquer approach for merge sort"
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left_array) and right_index < len(right_array):
        if left_array[left_index] < right_array[right_index]:
            result.append(left_array[left_index])
            left_index += 1
        else:
            result.append(right_array[right_index])
            right_index += 1

    return result + left_array[left_index:] + right_array[right_index:]

def merge_sort(array: list) -> list: # O(log n) time complexity
    """Merge Sort Algorithm"""

    if len(array) < 2:
        return array

    # Divide and conquer
    midpoint = math.floor(len(array) / 2)
    left_array = array[0:midpoint] # end of range is non-inclusive
    right_array = array[midpoint:]

    return merge(merge_sort(left_array), merge_sort(right_array)) # O(n) time complexity


def run():
    "Run method for test cases"

    cases = [
        [2, 1, 4, 3, 56, 34, 23, 32]
    ]
    for case in cases:
        print(merge_sort(case))

run()
