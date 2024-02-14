def selectionsort(A: list) -> None:
    n = len(A)

    for i in range(n):

        min_value = A[i]
        min_idx = i
        for j in range(i+1, n):
            if A[j] < min_value:
                min_idx = j
                min_value = A[j]

        A[i], A[min_idx] = A[min_idx], A[i]

def stable_selectionsort(A: list) -> None:
    n = len(A)

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if A[j] < A[min_idx]:
                min_idx = j

        while min_idx > i:
            A[min_idx-1], A[min_idx] = A[min_idx], A[min_idx-1]
            min_idx -= 1

def find_min(A: list, min: int, n: int, index: int) -> int:
    if index >= n:
        return min

    if A[index] < A[min]:
        return find_min(A, index, n, index+1)

    return find_min(A, min, n, index+1)

def recursive_selectionsort(A: list, n: int, index: int) -> None:
    if index >= n:
        return

    min_idx = find_min(A, index, n, index+1)

    A[index], A[min_idx] = A[min_idx], A[index]
    return recursive_selectionsort(A, n, index + 1)


A = [3,2,1,11,6,9,13,7]
# selectionsort(A)
# stable_selectionsort(A)
recursive_selectionsort(A, len(A), 0)
print(A)
