def insertion_sort(array: list) -> list:
    n = len(array)
    for i in range(1, n):
        c_value = array[i]
        position = i
        while position > 0 and array[position - 1] > c_value:
            array[position] = array[position - 1]
            position -= 1
        array[position] = c_value
    return array

def run():
    "Run method for test cases"

    cases = [
        [2, 1, 4, 3, 56, 34, 32, 23]
    ]
    for case in cases:
        print(insertion_sort(case))

run()
