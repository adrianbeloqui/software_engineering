import ctypes

class DynamicArray:
    def __init__(self) -> None:
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)
        
    def __repr__(self) -> str:
        return str(self)
        
    def __str__(self):
        return "["+ ", ".join(str(self._A[i]) for i in range(self._n)) +"]"
        
    def __len__(self):
        return self._n
    
    def __getitem__(self, index):
        if index < 0:
            index = self._n + index
    
        if not 0 <= index < self._n:
            raise IndexError("Invalid index")
        return self._A[index]
    
    def capacity(self):
        return self._capacity
    
    def is_empty(self):
        return self._n == 0
    
    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1
    
    def insert(self, index: int, obj):
        if index < 0:
            index = self._n + index

        if self._n == self._capacity:
            self._resize(2 * self._capacity, index)
        else:
            for j in range(self._n, index, -1):
                self._A[j] = self._A[j-1]

        self._A[index] = obj
        self._n += 1
    
    def prepend(self, obj):
        return self.insert(0, obj)
    
    def pop(self):
        if self._n > 0:
            obj = self._A[self._n - 1]
            self._n -= 1

            # Reduce capacity of array if N is 25% or less than capacity
            if ((self._n * 100) // self._capacity) <= 25:
                self._resize(self._capacity // 2)
        else:
            raise ValueError("Array is empty")
        return obj
    
    def delete(self, index: int):
        if index < 0:
            index = self._n + index

        if not 0 <= index < self._n:
            raise IndexError("Invalid index")

        for i in range(index, self._n - 1):
            self._A[i] = self._A[i+1]

        self._n -= 1
        
        # Reduce capacity of array if N is 25% or less than capacity
        if ((self._n * 100) // self._capacity) <= 25:
            self._resize(self._capacity // 2)
    
    def remove(self, obj):
        found = self.find(obj)
        if found is not None:
            for i in range(found, self._n - 1):
                self._A[i] = self._A[i+1]
            self._n -= 1
            
            # Reduce capacity of array if N is 25% or less than capacity
            if ((self._n * 100) // self._capacity) <= 25:
                self._resize(self._capacity // 2)
            
            return True
        return None
    
    def find(self, obj):
        # O(n)
        for i in range(self._n):
            if self._A[i] == obj:
                return i
        return None
    
    def _resize(self, capacity, index = -1):
        B = self._make_array(capacity)
        shift = 1 if index > -1 else 0
    
        for i in range(index):
            B[i] = self._A[i]
    
        # To support inserts in any part of the array
        for j in range(self._n-1, index-1, -1):
            B[j+shift] = self._A[j]
    
        self._A = B
        self._capacity = capacity
    
    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()