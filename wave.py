import pygame


class Wave(pygame.sprite.Sprite):
    def __init__(self, wave_number: int, mobs_remaining: int, mobs_spawned: int, total_mobs_in_wave: int,
                 mob_types: list, wave_end: bool, spawn_complete: bool):
        super().__init__()

        self.wave_number = wave_number
        self.mobs_remaining = mobs_remaining
        self.mobs_spawned = mobs_spawned
        self.total_mobs_in_wave = total_mobs_in_wave
        self.mob_types = mob_types
        self.wave_end = wave_end
        self.spawn_complete = spawn_complete

    def update(self):
        if self.mobs_spawned == self.total_mobs_in_wave:
            self.spawn_complete = True
        if self.mobs_remaining == 0:
            self.wave_end = True
