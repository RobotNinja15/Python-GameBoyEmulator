class Memory:
    def __init__(self):
        self.memory = [0] * 0xFFFF  # Create 64KB of memory

    def read(self, address):
        return self.memory[address]

    def write(self, address, value):
        self.memory[address] = value
