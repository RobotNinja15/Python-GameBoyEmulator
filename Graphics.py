import pygame
import numpy as np


class Graphics:
    def __init__(self):
        self.screen = pygame.display.set_mode((160, 144))  # Create a 160x144 pixel window
        self.frame_buffer = [0] * 160 * 144  # Create a frame buffer to store pixel data

    def update_screen(self):
        # Convert the frame buffer to a NumPy array and then to a Pygame surface
        surface = pygame.surfarray.make_surface(np.array(self.frame_buffer).reshape(144, 160))
        self.screen.blit(surface, (0, 0))
        pygame.display.flip()

    def set_pixel(self, x, y, color):
        if x >= 0 and x < 160 and y >= 0 and y < 144:  # Check that the coordinates are within bounds
            self.frame_buffer[y * 160 + x] = color


graphics = Graphics()
graphics.set_pixel(0, 0, 0xFF0000)  # Set the top-left pixel to red
graphics.update_screen()  # Update the screen to display the red pixel


