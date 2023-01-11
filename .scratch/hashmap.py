 # Initialize empty hashmap.
MAX = 20
arr = [1,2,3,4,5,7]
hashmap = [False for i in range(MAX)];

# Insert array elements to hashmap
for i in range(len(arr)):
    hashmap[arr[i]] = True

print(hashmap)
