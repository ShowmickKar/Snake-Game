import pygame
from cell import Cell


class Snake:
    def __init__(self, width, height):
        self.color = (155, 0, 7)
        self.size = 20
        self.__index = [15, 15]
        self.position = [self.__index[0] * self.size, self.__index[1] * self.size]
        self.__direction = [1, 0]
        self.rows = width // self.size
        self.score = 0
        self.length = 0
        self.body = [self.__index]
        self.path = [self.__direction]
        self.__dead = False

    def getDirection(self):
        return [self.__direction[0], self.__direction[1]]

    def setDirection(self, direction):
        self.__direction = direction

    def getIndex(self):
        return [self.__index[0], self.__index[1]]

    def move(self, grid):
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i] = self.body[i - 1]
            self.path[i] = self.path[i - 1]
        if self.__index[0] > self.rows - 1:
            self.__dead = True
            self.__index[0] = 0
        if self.__index[0] < 0:
            self.__dead = True
            self.__index[0] = self.rows - 1
        if self.__index[1] > self.rows - 1:
            self.__dead = True
            self.__index[1] = 0
        if self.__index[1] < 0:
            self.__dead = True
            self.__index[1] = self.rows - 1
        self.position = [self.__index[0] * self.size, self.__index[1] * self.size]
        try:
            direction = self.getDirection()
            self.__index[0] += direction[0]
            self.__index[1] += direction[1]
            index = self.getIndex()
            self.body[0] = index
            self.path[0] = direction
        except Exception as e:
            print(e)

    def dead(self):
        if self.__dead:
            return True
        for i in range(0, len(self.body) - 1):
            for j in range(i + 1, len(self.body)):
                if self.body[i] == self.body[j]:
                    return True

    def draw(self, window, index=None):
        pygame.draw.rect(
            window,
            self.color,
            (self.position[0], self.position[1], self.size, self.size),
        )
        for part in self.body:
            try:
                pygame.draw.rect(
                    window,
                    self.color,
                    (part[0] * self.size, part[1] * self.size, self.size, self.size),
                )
            except Exception as e:
                pass