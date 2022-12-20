import os
from CPU import CPU
from Memory import Memory
from Graphics import Graphics
from Audio import Audio


def load_rom(filename):
    with open(filename, "rb") as f:
        return f.read()


def run_rom(rom_data):
    # Initialize the virtual CPU, memory, graphics, and audio systems
    cpu = CPU()
    memory = Memory()
    graphics = Graphics()
    audio = Audio()

    # Load the ROM data into memory
    for i in range(len(rom_data)):
        memory.write(0x0100 + i, rom_data[i])

    # Set the program counter to the start of the ROM
    cpu.pc = 0x0100

    # Run the ROM
    while True:
        # Fetch and execute the next instruction
        instruction = memory.read(cpu.pc)
        cpu.execute_instruction(instruction)

        # Update the graphics and audio
        graphics.update_screen()
        audio.update_audio()


def main():
    # Load the ROM file
    rom_data = load_rom("Pokemon - Blue Version (USA, Europe).gb")

    # Run the ROM
    run_rom(rom_data)


if __name__ == "__main__":
    main()
