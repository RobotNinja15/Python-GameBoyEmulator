class CPU:
    def __init__(self):
        self.registers = [0] * 8  # Create 8 registers
        self.memory = [0] * 0xFFFF  # Create 64KB of memory
        self.pc = 0  # Program counter

    def execute_instruction(self, instruction):
        if instruction == 0x00:  # NOP (No Operation)
            self.pc += 1  # Increment program counter
        elif instruction == 0x01:  # LD BC, nn
            self.registers[2] = self.memory[self.pc + 1]
            self.registers[3] = self.memory[self.pc + 2]
            self.pc += 3
        # Add more instructions here
