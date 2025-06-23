"""
Separate chaining
resolving collisions with linear probing
"""

N = 11
l = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
keys = []

for item in l:
    slot_found = False
    i = 0
    
    while not slot_found:
        k = (((3*item) + 5) + i**2) % 11
        if k not in keys:
            slot_found = True
            print(item, k)
            keys.append(k)
        else:
            i += 1
