import pygame
from abc import ABC, abstractmethod
max_width = 2000
max_height = 1103


class Border:
    def __init__(self, camera, player):
        self.camera = camera
        self.player = player

    def scroll(self):
        self.camera.offset_float.x += (self.player.pos_x - self.camera.offset_float.x - 500)
        self.camera.offset_float.y += (self.player.pos_y - self.camera.offset_float.y - 500)
        self.camera.offset.x, self.camera.offset_y = int(self.camera.offset_float.x), int(self.camera.offset_float.y)
        self.camera.offset.x = max(self.camera.offset.x, 0)
        self.camera.offset.x = min(self.camera.offset.x, max_width)
        #self.camera.offset.y = max(self.camera.offset.y, 0)
        #self.camera.offset.y = min(500, max_height + self.camera.offset.y)



