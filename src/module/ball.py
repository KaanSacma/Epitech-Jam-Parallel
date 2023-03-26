import pygame
from module.colors import BLACK

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, radius, background):
        pygame.sprite.Sprite.__init__(self)
        self._image = pygame.Surface(radius)
        self._background = background
        self._background_rect = self._background.get_rect()
        self._rect = self._image.get_rect()
        self._background_rect.center = pos
        self._speed = 5
        self._direction = [1, 1]

    def update(self, kicker):
        self._background_rect.x += self._speed * self._direction[0]
        self._background_rect.y += self._speed * self._direction[1]
        if self._background_rect.top < (900 / 2) - kicker.size_y / 2:
            self._direction[1] *= -1
        if self._background_rect.bottom > (900 / 2) + kicker.size_y / 2:
            self._direction[1] *= -1
        if self._background_rect.left < (1600 / 2) - kicker.size_x / 2:
            self._direction[0] *= -1
        if self._background_rect.right > (1600 / 2) + kicker.size_x / 2:
            self._direction[0] *= -1

    def set_speed(self, speed):
        self._speed = speed

    def set_direction(self, direction):
        self._direction = direction

    def set_spawn(self, pos):
        self._background_rect.center = pos

    def get_pos(self):
        return self._background_rect.center

    def get_radius(self):
        return self._background_rect.width

    def draw_background(self, window):
        window.blit(self._background, self.get_pos())

    def draw(self, window):
        self.draw_background(window)
        ##pygame.draw.circle(window, BLACK, self.get_pos(), self.get_radius())
