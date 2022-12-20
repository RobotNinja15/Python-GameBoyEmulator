import pygame
import numpy as np


class Audio:
    def __init__(self):
        pygame.mixer.init()  # Initialize the Pygame mixer

    def play_sound(self, frequency, duration):
        # Create a Pygame sound object and play it
        sound = pygame.sndarray.make_sound(self.generate_sound_data(frequency, duration))
        sound.play()

    def generate_sound_data(self, frequency, duration):
        # Generate an array of sound samples with a given frequency and duration
        sample_rate = 44100
        num_samples = int(duration * sample_rate)
        return (np.sin(2 * np.pi * np.arange(num_samples) * frequency / sample_rate)).astype(np.float32)
