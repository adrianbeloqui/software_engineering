# Pseudo code

# define intToBinString, receiving intVal:
#     if intVal is equal to zero:
#         return "0"
#     set strVal to ""
#     while intVal is greater than zero:
#         if intVal is odd:
#             prefix "1" to strVal
#         else:
#             prefix "0" to strVal
#         divide intVal by two, rounding down
#     return strVal

def int2binary_string(num: int) -> str:
    if num == 0:
        return "0"
    representation = ""
    while num > 0:
        representation += str(num % 2)
        num //= 2
    return representation

print(int2binary_string(5))
