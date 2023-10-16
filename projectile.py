import pygame
import pistol
import shotgun
import math


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos_x: float, pos_y: float, radius: float, direction: str, proj_vel: float, damage: float,
                 color):
        super().__init__()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.radius = radius
        self.direction = direction
        self.proj_vel = proj_vel
        self.damage = damage
        self.color = "black"
        self.image = pygame.Surface((radius, radius))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def update(self):
        if self.direction == "up":
            self.pos_y -= self.proj_vel
        elif self.direction == "down":
            self.pos_y += self.proj_vel
        elif self.direction == "right":
            self.pos_x += self.proj_vel
        elif self.direction == "left":
            self.pos_x -= self.proj_vel
        elif self.direction == "shotgun_up_1":
            self.pos_x -= self.proj_vel * math.sin(math.pi / 12)
            self.pos_y -= self.proj_vel * math.cos(math.pi / 12)
        elif self.direction == "shotgun_up_2":
            self.pos_x += self.proj_vel * math.sin(math.pi / 12)
            self.pos_y -= self.proj_vel * math.cos(math.pi / 12)
        elif self.direction == "shotgun_right_1":
            self.pos_x += self.proj_vel * math.cos(math.pi / 12)
            self.pos_y -= self.proj_vel * math.sin(math.pi / 12)
        elif self.direction == "shotgun_right_2":
            self.pos_x += self.proj_vel * math.cos(math.pi / 12)
            self.pos_y += self.proj_vel * math.sin(math.pi / 12)
        elif self.direction == "shotgun_left_1":
            self.pos_x -= self.proj_vel * math.cos(math.pi / 12)
            self.pos_y -= self.proj_vel * math.sin(math.pi / 12)
        elif self.direction == "shotgun_left_2":
            self.pos_x -= self.proj_vel * math.cos(math.pi / 12)
            self.pos_y += self.proj_vel * math.sin(math.pi / 12)
        elif self.direction == "shotgun_down_1":
            self.pos_x -= self.proj_vel * math.sin(math.pi / 12)
            self.pos_y += self.proj_vel * math.cos(math.pi / 12)
        elif self.direction == "shotgun_down_2":
            self.pos_x += self.proj_vel * math.sin(math.pi / 12)
            self.pos_y += self.proj_vel * math.cos(-math.pi / 12)

        self.rect.center = (self.pos_x, self.pos_y)
        # change the line below using constants rather than hard coded values
        if self.rect.top > 1000 or self.rect.bottom < 0 or self.rect.left > 1500 or self.rect.right < 0:
            self.kill()


