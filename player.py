import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, height: float, width: float, pos_x: float, pos_y: float, movement_speed: float, direction: str,
                 health: int, weapon: str, weapon_index: int, color: str, weapon_map={"pistol": 0},
                 weapon_arsenal=["pistol"], weapon_ammo=[50], current_weapon="pistol"):
        super().__init__()
        self.movement_speed = movement_speed
        self.height = height
        self.width = width
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.direction = direction
        self.health = health
        self.color = "red"
        self.weapon = weapon
        self.weapon_index = weapon_index
        self.weapon_map = weapon_map
        self.weapon_arsenal = weapon_arsenal
        self.weapon_ammo = weapon_ammo
        self.current_weapon = current_weapon
        self.image = pygame.Surface((height, width))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = (pos_x, pos_y)

    def update(self, keys_pressed):
        if self.health <= 0:
            self.kill()
        # for some reason, pressing the button once causes many print statements, could be how update works in pygame
        if keys_pressed[pygame.K_q]:
            self.weapon_index = (self.weapon_index - 1) % len(self.weapon_arsenal)
            self.current_weapon = self.weapon_arsenal[self.weapon_index]
            print(self.current_weapon, self.weapon_arsenal, self.weapon_index)
        if keys_pressed[pygame.K_e]:
            self.weapon_index = (self.weapon_index + 1) % len(self.weapon_arsenal)
            self.current_weapon = self.weapon_arsenal[self.weapon_index]
            print(self.current_weapon, self.weapon_arsenal, self.weapon_index)
        if keys_pressed[pygame.K_UP]:
            self.pos_y -= self.movement_speed
            self.direction = "up"
        if keys_pressed[pygame.K_DOWN]:
            self.pos_y += self.movement_speed
            self.direction = "down"
        if keys_pressed[pygame.K_RIGHT]:
            self.pos_x += self.movement_speed
            self.direction = "right"
        if keys_pressed[pygame.K_LEFT]:
            self.pos_x -= self.movement_speed
            self.direction = "left"
        self.rect.center = (self.pos_x, self.pos_y)

    def get_direction(self):
        return self.direction

    def get_position(self):
        return self.pos_x, self.pos_y

    def shoot(self, direction: str):
        pass
