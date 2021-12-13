"""
You have a large array with most of the elements as zero.

Use a more space-efficient data structure, SparseArray, that implements the same interface:

    init(arr, size): initialize with the original large array and size.
    set(i, val): updates index at i with val.
    get(i): gets the value at index i.

"""

class SparseArray():
    def __init__(self, array, size = 0): #Size is given by the array in Python
        self.storage = {}
        for i, number in (i, number for i, number in enumerate(array) if number != 0):
            self.storage[i] = number
        self.length = size if size else len(array)
    def get(self, index):
        if index < 0 or index >= self.length:
            return None #Better as an exception
        return self.storage.get(index, 0)
    def set(self, index, value):
        if index < 0:
            return None #Better as an exception
        if value == 0:
            self.storage.pop(index)
            self.lenght = max(self.storage)
        else:
            self.storage[index] = value
            self.length = max(self.lenght, index)
