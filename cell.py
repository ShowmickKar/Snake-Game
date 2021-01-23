import pygame
import random

food_color = (6, 152, 7)


class Cell:
    def __init__(self, index, width, height, color=(0, 0, 0)):
        self.size = 20
        self.index = index
        self.position = (self.index[0] * self.size, self.index[1] * self.size)
        self.color = color

    def draw(self, window):
        pygame.draw.rect(
            window,
            self.color,
            (self.position[0], self.position[1], self.size, self.size),
        )


class Food(Cell):
    def __init__(self, width, height):
        self.size = 20
        self.index = [
            random.randint(0, width // self.size - 1),
            random.randint(0, width // self.size - 1),
        ]
        self.position = [self.index[0] * self.size, self.index[1] * self.size]
        self.color = food_color
        self.eated = False

    def reset(self, width):
        self.index = [
            random.randint(0, width // self.size - 1),
            random.randint(0, width // self.size - 1),
        ]
        self.position = [self.index[0] * self.size, self.index[1] * self.size]
