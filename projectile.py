import pygame
import pistol
import shotgun


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
            self.rect.move_ip(0, -self.proj_vel)
        elif self.direction == "down":
            self.rect.move_ip(0, self.proj_vel)
        elif self.direction == "right":
            self.rect.move_ip(self.proj_vel, 0)
        else:
            self.rect.move_ip(-self.proj_vel, 0)
        # change the line below using constants rather than hard coded values
        if self.rect.top > 1000 or self.rect.bottom < 0 or self.rect.left > 1500 or self.rect.right < 0:
            self.kill()


