def quicksort(A: list, low: int, high: int) -> None:
    if low < high:
        pi = partition(A, low, high)
        quicksort(A, low, pi-1)
        quicksort(A, pi+1, high)

def partition(A: list, low: int, high: int) -> int:
    pivot = A[low]
    i = low + 1
    j = high
    while True:
        while i <= j and A[i] <= pivot:
            i += 1
        while i <= j and A[j] > pivot:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
        else:
            break
    A[low], A[j] = A[j], A[low]
    return j
        
A = [3, 5, 8, 9, 6, 2]
print('Original list:', A)
quicksort(A, 0, len(A)-1)
print('Sorted list:', A)
