import pygame
import math


class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, radius, color):
        pygame.sprite.Sprite.__init__(self)
        self._image = pygame.Surface(radius)
        self._image.fill(color)
        self._rect = self._image.get_rect()
        self._rect.center = pos
        self._speed = 5
        self._direction = [1, 1]

    def update(self, kicker):
        self._rect.x += self._speed * self._direction[0]
        self._rect.y += self._speed * self._direction[1]

        if self._rect.top < (900 / 2) - kicker.size_y / 2:
            self._rect.y -= self._speed * self._direction[1]
            self._direction[1] *= -1
            self.set_speed(self._speed - 3)
        if self._rect.bottom > (900 / 2) + kicker.size_y / 2:
            self._rect.y -= self._speed * self._direction[1]
            self._direction[1] *= -1
            self.set_speed(self._speed - 3)
        if self._rect.left < (1600 / 2) - kicker.size_x / 2:
            self._rect.x -= self._speed * self._direction[0]
            self._direction[0] *= -1
            self.set_speed(self._speed - 6)
        if self._rect.right > (1600 / 2) + kicker.size_x / 2:
            self._rect.x -= self._speed * self._direction[0]
            self._direction[0] *= -1
            self.set_speed(self._speed - 6)
        self.set_to_norm()

    def set_to_norm(self):
        distance = math.sqrt(math.pow(self._direction[0], 2) + math.pow(self._direction[1], 2))
        self._direction[0] /= distance
        self._direction[1] /= distance

    def add_force(self, force_x, force_y):
        self._direction[0] += force_x
        self._direction[1] += force_y
        self.set_to_norm()

    def set_speed(self, speed):
        self._speed = speed
        if self._speed > 50:
            self._speed = 50
        if self._speed < 5:
            self._speed = 5

    def set_direction(self, direction):
        self._direction = direction

    def set_spawn(self, pos):
        self._rect.center = pos

    def get_pos(self):
        return self._rect.center

    def get_radius(self):
        return self._rect.width

    def get_color(self):
        return self._image.get_at((0, 0))

    def draw(self, window):
        pygame.draw.circle(window, self.get_color(), self.get_pos(), self.get_radius())

