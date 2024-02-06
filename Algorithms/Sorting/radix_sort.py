def radix_sort(A: list) -> None:
    n = len(A)
    max_size = max(A)

    # Get number of digits of largest number
    digits = 0
    while max_size > 0:
        max_size //= 10
        digits += 1

    # digits go from less significant to most significant (right to left)
    counter = 0
    while counter < digits:
        sort_digits = [None] * 10
        # Sort elements in A based on digit on sort_digits array
        for i in range(n):
            digit = (A[i] // 10**counter) % 10
            element = A[i]

            if sort_digits[digit] is None:
                sort_digits[digit] = [element]
            else:
                sort_digits[digit].append(element)


        # Put elements back in A in the appropiate order following the
        # order established in sort_digits
        z = 0
        for i in range(10):
            if sort_digits[i] is not None:
                for x in sort_digits[i]:
                    A[z] = x
                    z += 1
        counter += 1


def radix_sort2(A: list) -> None:
    n = len(A)
    max_size = max(A)
    # Get number of digits of largest number
    digits = len(str(max_size))
    bins = [[]] * 10

    for i in range(digits):
        for j in range(n):
            e = (A[j] // pow(10, i)) % 10
            if len(bins[e]) > 0:
                bins[e].append(A[j])
            else:
                bins[e] = [A[j]]
        k = 0
        for x in range(10):
            for y in bins[x]:
                A[k] = y
                k += 1


A = [3, 5, 8, 9, 6, 2]
print('Original list:', A)
radix_sort2(A)
print('Sorted list:', A)
