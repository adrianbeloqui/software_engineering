def bubble_sort(array: list) -> list:
    n = len(array)
    for runs in range(n-1, 0, -1):
        for i in range(runs):
            if array[i] > array[i+1]:
                temp = array[i+1]
                array[i+1] = array[i]
                array[i] = temp
    return array

def run():
    "Run method for test cases"

    cases = [
        [2, 1, 4, 3, 56, 34, 32, 23]
    ]
    for case in cases:
        print(bubble_sort(case))

run()
