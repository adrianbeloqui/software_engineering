def selection_sort(array: list) -> list:
    n = len(array)
    # Iterate the array leaving 2 slots at the end
    for i in range(n-1):
        # Track position of the smallest value
        position = i
        # Iterate from the next item through n
        for j in range(i+1, n):
            # selected the smallest value
            if array[j] < array[position]:
                # Update position of the smallest value
                position = j
        # Update current iterated element with the smallest element found
        temp = array[i]
        array[i] = array[position]
        array[position] = temp
    return array

def run():
    "Run method for test cases"

    cases = [
        [2, 1, 4, 3, 56, 34, 32, 23]
    ]
    for case in cases:
        print(selection_sort(case))

run()
