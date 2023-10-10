def selection_sort(array: list) -> list:
    n = len(array)
    for i in range(n-1):
        position = i
        for j in range(i+1, n):
            if array[j] < array[position]:
                position = j
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
