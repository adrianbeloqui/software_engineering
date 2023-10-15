def shell_sort(array: list) -> list:
    n = gap = len(array)
    while gap > 0:
        gap //= 2
        if gap < 1:
            break

        for i in range(gap, n):
            if i + gap < n:
                swap(array, i, i + gap, "right")
            if i - gap >= 0:
                swap(array, i, i - gap, "left")
    return array
                
def swap(array: list, i: int, other_i: int, swap_type: str) -> None:
    if swap_type == "left":
        if array[i] < array[other_i]:
            tmp = array[i]
            array[i] = array[other_i]
            array[other_i] = tmp
    if swap_type == "right":
        if array[i] > array[other_i]:
            tmp = array[i]
            array[i] = array[other_i]
            array[other_i] = tmp

def shell_sort2(array: list) -> list:
    n = len(array)
    gap = n // 2
    while gap > 0:
        i = gap
        while i < n:
            c_value = array[i]
            j = i - gap
            if j >= 0 and array[j] > array[j+gap]:
                array[j+gap] = array[j]
                j -= gap
            array[j+gap] = c_value
            i += 1
        gap //= 2
    return array


def run():
    "Run method for test cases"

    cases = [
        [2, 1, 4, 3, 56, 34, 32, 23]
    ]
    for case in cases:
        print("Original array:", case)
        print("Sorted array:", shell_sort(case))
        print("Sorted array:", shell_sort2(case))

run()
