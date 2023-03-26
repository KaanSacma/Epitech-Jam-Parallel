import pygame
from module.colors import BLACK


class Kicker:
    def __init__(self, size_x, size_y, background):
        self.size_x = size_x
        self.size_y = size_y
        self._background = background
        self._background_rect = self._background.get_rect()

    def draw_background(self, window):
        window.fill(BLACK)
        window.blit(self._background, (0, 0))

    def draw(self, window, outline=None):
        self.draw_background(window)
