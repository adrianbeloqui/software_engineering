"""
Separate chaining
resolving collisions with linear probing
"""

N = 11
l = [12, 44, 13, 88, 23, 94, 11, 39, 20, 16, 5]
keys = []

for i in l:
    slot_found = False
    iter = 5
    
    while not slot_found:
        k = ((3*i)+iter)%11
        if k not in keys:
            slot_found = True
            print(i, k)
            keys.append(k)
        else:
            iter += 1
