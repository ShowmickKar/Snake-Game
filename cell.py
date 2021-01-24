import pygame
import random

food_colors = [
    (6, 152, 7),
    (42, 110, 193),
    (123, 110, 193),
    (30, 43, 193),
    (2, 139, 102),
    (159, 178, 78),
    (215, 178, 78),
    (243, 81, 2),
    (243, 203, 2),
    (243, 168, 235),
]
color1 = (98, 93, 102)
color2 = (98, 106, 102)


class Cell:
    def __init__(self, index, width, height, color=(0, 0, 0)):
        self.size = 20
        self.index = index
        self.position = (self.index[0] * self.size, self.index[1] * self.size)
        self.color = color
        # if self.index[0] % 2 == self.index[1] % 2:
        #     self.color = color1
        # else:
        # self.color = color2

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
        self.color = random.choice(food_colors)
        self.eaten = False

    def reset(self, width):
        self.index = [
            random.randint(0, width // self.size - 1),
            random.randint(0, width // self.size - 1),
        ]
        self.position = [self.index[0] * self.size, self.index[1] * self.size]
        self.color = random.choice(food_colors)
