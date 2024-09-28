class Array:
    def __init__(self, size):
        self.size = size
        self.array = [None] * size

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        return self.array[index]

    def set(self, index, value):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")
        self.array[index] = value

    def __str__(self):
        return str(self.array)

# Example usage:
arr = Array(5)
arr.set(0, 10)
arr.set(1, 20)
arr.set(2, 30)
print(arr)  # Output: [10, 20, 30, None, None]
print(arr.get(1))  # Output: 20
