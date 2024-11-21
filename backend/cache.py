class Cache:
    def __init__(self):
        self.cache_data = {}

    def get(self, filename):
        return self.cache_data.get(filename, None)

    def put(self, filename, data):
        self.cache_data[filename] = data
