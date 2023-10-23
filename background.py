import pygame


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        super().__init__()
        self.image = pygame.image.load(image_file).convert()
        pygame.transform.scale(self.image, (2200, 1103))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

