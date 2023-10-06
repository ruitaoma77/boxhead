import pygame
import random
knockback = [-300, 300]


class Mob(pygame.sprite.Sprite):
    def __init__(self, health: int, movement_speed: float, damage: int, pos_x: float, pos_y: float, color: "str",
                 alive=True):
        super().__init__()
        self.health = health
        self.movement_speed = movement_speed
        self.damage = damage
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        self.alive = alive
        self.latest_location: list = []
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def update(self, player):
        self.move_towards_player(player)
        # redundant code?
        if self.health <= 0:
            self.alive = False
        if not self.alive:
            self.kill()

    def move_towards_player(self, player):
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x, player.rect.y - self.rect.y)
        # placeholder so game doesn't crash by trying to normalize a zero vector
        if dirvect == [0, 0]:
            self.pos_x += 200
            self.pos_y += 200
        else:
            dirvect.normalize()
            # Move along this normalized vector towards the player at current speed.
            dirvect.scale_to_length(self.movement_speed)
            self.latest_location = dirvect
        self.pos_x += dirvect[0]
        self.pos_y += dirvect[1]
        self.rect.center = (self.pos_x, self.pos_y)
