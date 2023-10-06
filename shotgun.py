import pygame
import weapons


class Shotgun(weapons.Weapons):
    def __init__(self, name: str, reload_speed: float, firing_speed: float, projectile_speed: float,
                 magazine_size: int, bullets_remaining: int, color: str, pos_x: float, pos_y: float):
        super().__init__(name, reload_speed, firing_speed, projectile_speed,
                         magazine_size, bullets_remaining, color, pos_x, pos_y)

        self.color = "pink"
        self.image = pygame.Surface((50, 50))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)
