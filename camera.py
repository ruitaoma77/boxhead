import pygame
vec = pygame.math.Vector2


class Camera:
    def __init__(self, player):
        self.player = player
        self.offset = vec(0, 0)
        self.offset_float = vec(0, 0)

    def setmethod(self, method):
        self.method = method

    def scroll(self):
        self.method.scroll()

