"""
Cracking the Coding Interview - 6th version
Technical Questions - Optimize & Solve Technique #1: Look for BUD - Bottlenecks - Page 67

Problem:

Given an array of distinct integer values, count the number of pairs of integers that have difference k.
For example, given the array [1, 7, 5, 9, 2, 12, 3] and the difference k = 2,
there are four pairs with difference 2: (1, 3), (3, 5), (5, 7), (7, 9)

Notes learned from implementing this:

To avoid duplicate pairs, you can look up for x + k only, because if let's say 7 and 9 are in the array,
and you look for both x + k and x - k, you will get (7, 9) and (9, 7) in the final result. But, because
we iterate over the whole array, we can just look for x + k (or x - k, but just one!) and get a single
instance of the pair of those numbers that satisfy the problem.
"""

def brute_force(array: list, k: int) -> list:
    """Brute force approach

    The bottleneck here is the repeated search for the "other side" of the pair (x, ?)

    O(n^2)
    """
    pairs = []
    for index, value in enumerate(array): # O(n)
        next_index = index + 1
        while next_index < len(array): # O (n)
            other_value = array[next_index]
            if abs(value - other_value) == k:
                pairs.append((value, other_value))
            next_index += 1
    return pairs

print(brute_force([1, 7, 5, 9, 2, 12, 3], 2))


def binary_search(array: list, value: any, start: int, end: int):
    """Binary search implementation"""

    if start > end or (start == end and array[start] != value):
        return -1

    mid = (start + end) // 2
    if array[mid] == value:
        return mid
    if array[mid] < value:
        return binary_search(array, value, mid + 1, len(array) -1)
    return binary_search(array, value, start, mid - 1)

def optimizing_bottleneck(array: list, k: int) -> list:
    """More optimal algorithm than brute force doing a space vs time tradeoff
    by using a dictionary to remove duplicates, but using sorting and binary search 
    to speed up runtime

    O(n log n)
    """
    pairs = []
    array.sort() # Timsort (mix of merge sort and insertion sort) - O(n log n)
    for value in array: # O(n)
        found_index = binary_search(array, value + k, 0, len(array)) # O(log n)
        if found_index != -1:
            pairs.append((value, array[found_index]))
    return pairs, len(pairs)

print(optimizing_bottleneck([1, 7, 5, 9, 2, 12, 3], 2))

def even_more_optimal(array: list, k: int) -> list:
    """Even more optimal approach
    This approach transforms the array into a hash table/dictionary
    and then performs lookups of x + k or x - k

    O(n)
    """
    dictified = {i:i for i in array} # O(n)
    pairs = []
    for i in array: # O(n)
        other_val = dictified.get(i + k) # O(1)
        if other_val is not None:
            pairs.append((i, other_val))

    return pairs, len(pairs)

print(even_more_optimal([1, 7, 5, 9, 2, 12, 3], 2))
