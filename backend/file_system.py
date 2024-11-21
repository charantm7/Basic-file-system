from .cache import Cache
from .storage import ArrayStorage
from .fsm import FileSystemFSM

class FileSystemManager:
    def __init__(self):
        self.storage = ArrayStorage(100)  # Array-based storage with a size of 100
        self.cache = Cache()
        self.fsm = FileSystemFSM()
    
    def read_file(self, filename):
        state = self.fsm.get_state()
        if state == "IDLE":
            self.fsm.change_state("READING")
            data = self.cache.get(filename)
            if data is None:
                data = self.storage.read(filename)
                self.cache.put(filename, data)
            self.fsm.change_state("IDLE")
            return data
        return None

    def write_file(self, filename, data):
        state = self.fsm.get_state()
        if state == "IDLE":
            self.fsm.change_state("WRITING")
            self.storage.write(filename, data)
            self.cache.put(filename, data)
            self.fsm.change_state("IDLE")
