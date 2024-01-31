def count_sort(A: list) -> None:
    n = len(A)
    max_size = max(A)
    count_array = [0] * (max_size + 1)

    for i in range(n):
        count_array[A[i]] += 1

    i, j = 0, 0
    while i < (max_size + 1):
        if count_array[i] > 0:
            A[j] = i
            count_array[i] -= 1
            j += 1
        else:
            i += 1

A = [3, 5, 8, 9, 6, 2]
print('Original list:', A)
count_sort(A)
print('Sorted list:', A)
