def recursive_insertion_sort(array: list, sorted_idx) -> list:
    if sorted_idx + 1 >= len(array):
        return array
    
    position = sorted_idx + 1
    cvalue = array[position]
    
    while position > 0 and cvalue < array[position - 1]:
        array[position] = array[position - 1]
        position -= 1
    
    array[position] = cvalue
    return recursive_insertion_sort(array, sorted_idx + 1)



def run():
    "Run method for test cases"

    cases = [
        [2, 1, 4, 3, 56, 34, 32, 23]
    ]
    for case in cases:
        print(recursive_insertion_sort(case, 0))

run()
