"""
Cracking the Coding Interview - 6th version - Big O - Exercise 10 - Page 57

Sum the digits in a number. For example, if n = 1234, then the sum of the digits is 10
"""

def sumDigits(n: int) -> int:
    """O(log n)"""
    sum = 0
    iterations = 0

    while n > 0:
        iterations += 1
        sum += n % 10
        n //= 10

    print(f"took {iterations} iterations")
    return sum

print(sumDigits(1000000000))

def sumDigits2(n: int) -> int:
    """O(n). More expensive due to type casting and iteration through the whole array of lenght n"""
    str_int = str(n)
    sum = 0
    iterations = 0
    for _, value in enumerate(str_int):
        iterations += 1
        sum += int(value)

    print(f"took {iterations} iterations")
    return sum

print(sumDigits2(1000000000))
