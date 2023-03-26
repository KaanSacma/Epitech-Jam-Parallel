import pygame
from module.colors import BLACK


class Menu:
    def __init__(self, background, buttons, name):
        self._background = background
        self._buttons = buttons
        self._name = name
        self._background_rect = self._background.get_rect()

    def set_name(self):
        pygame.display.set_caption(self._name)

    def get_button(self, i):
        return self._buttons[i]

    def get_buttons(self):
        return self._buttons

    def draw_background(self, window):
        window.fill(BLACK)
        window.blit(self._background, (-200, 0))

    def draw_buttons(self, window, outline=None):
        for button in self._buttons:
            button.draw(window, outline)

    def draw(self, window, outline=None):
        self.draw_background(window)
        self.draw_buttons(window, outline)
