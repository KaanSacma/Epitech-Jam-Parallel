import pygame


class Image:
    def __init__(self, path):
        self._image = pygame.image.load(path)

    def get(self):
        return self._image
