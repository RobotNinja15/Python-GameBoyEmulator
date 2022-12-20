class Memory:
    def __init__(self):
        self.memory = [0] * 65536  # Create a 65536-element list to store memory values

    def write(self, address, value):
        if address >= 0 and address < len(self.memory):  # Check that the address is within bounds
            self.memory[address] = value

    def read(self, address):
        if address >= 0 and address < len(self.memory):  # Check that the address is within bounds
            return self.memory[address]


