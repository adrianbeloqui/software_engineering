class ArrayList:
    """Basic auto-expanding array list implementation only handling appends"""
    def __init__(self) -> None:
        self.current_index = -1
        self.current_length = -1
        self.array = []

    def append(self, value: any) -> None:
        print(f"appending {value}")
        if self._should_expand():
            self._expand()
        self._append(value)
        self.current_index += 1

    def _should_expand(self) -> None:
        return self.current_index + 2 > self.current_length

    def _expand(self) -> None:
        if self.current_length == -1:
            self.current_length = 1
        else:
            self.current_length *= 2

        new_array = [None] * self.current_length
        for index, value in enumerate(self.array):
            new_array[index] = value
        self.array = new_array

    def _append(self, value: any):
        self.array[self.current_index + 1] = value

    def __str__(self) -> str:
        result = "["
        for i, _ in enumerate(self.array):
            if i < self.current_index:
                result += f"{_}, "
            elif i == self.current_index:
                result += f"{_}"
            else:
                break
        result += " ]"
        return result

array = ArrayList()
array.append(1)
array.append(2)
array.append(3)
array.append(4)
array.append(5)

print(array)
print(array.current_index)
print(array.current_length)
print(array.array)
