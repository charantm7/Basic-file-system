class ArrayStorage:
    def __init__(self, size):
        self.storage = [None] * size
        self.filename_index = {}

    def read(self, filename):
        index = self.filename_index.get(filename, -1)
        if index != -1:
            return self.storage[index]
        return None

    def write(self, filename, data):
        index = self._find_empty_slot()
        if index != -1:
            self.storage[index] = data
            self.filename_index[filename] = index

    def _find_empty_slot(self):
        for i in range(len(self.storage)):
            if self.storage[i] is None:
                return i
        return -1
