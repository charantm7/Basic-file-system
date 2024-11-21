class FileSystemFSM:
    def __init__(self):
        self.state = "IDLE"  # Possible states: IDLE, READING, WRITING
    
    def get_state(self):
        return self.state

    def change_state(self, new_state):
        if new_state in ["IDLE", "READING", "WRITING"]:
            self.state = new_state
