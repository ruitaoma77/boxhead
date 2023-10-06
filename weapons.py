import pygame


class Weapons(pygame.sprite.Sprite):
    def __init__(self, name: str, reload_speed: float, firing_speed: float, projectile_speed: float,
                 magazine_size: int, bullets_remaining: int, color: str, pos_x: float, pos_y: float):
        super().__init__()
        self.name = name
        self.reload_speed = reload_speed
        self.firing_speed = firing_speed
        self.magazine_size = magazine_size
        self.bullets_remaining = bullets_remaining
        self.projectile_speed = projectile_speed
        self.color = "purple"
        self.pos_x = pos_x
        self.pos_y = pos_y

    def shoot(self, bullets_remaining: int):
        pass
