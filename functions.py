import pygame


def draw_text(text: str, font, text_col, x: int, y: int, screen):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
