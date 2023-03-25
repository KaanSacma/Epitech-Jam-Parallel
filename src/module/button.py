import pygame
from module.states import *


class Button:
    def __init__(self, images, pos, function, text, to_menu=None):
        self._state = State("Static")
        self._images = images
        self._pos = pos
        self._function = function
        self._text = text
        self._to_menu = to_menu
        self._width, self._height = self._images[0].get_size()
        self._rect = self._images[self._state.get()].get_rect()
        self._rect.left, self._rect.top = [self._pos[0], self._pos[1]]

    def get_function(self):
        return self._function

    def get_text(self):
        return self._text

    def get_to_menu(self):
        return self._to_menu

    def execute_function(self):
        self._function()

    def draw(self, window, outline=None):
        window.blit(self._images[self._state.get()], self._rect)
        if self._text.get_text() != '':
            font = pygame.font.Font(self._text.get_font_path(), self._text.get_font_size())
            text = font.render(self._text.get_text(), 1, self._text.get_font_color())
            pos = (self._pos[0] + (self._width / 2 - text.get_width() / 2), self._pos[1] + (self._height / 2 - text.get_height() / 2))
            window.blit(text, pos)

    def is_hover(self, event_type):
        mouse_pos = pygame.mouse.get_pos()
        if self._pos[0] < mouse_pos[0] < self._pos[0] + self._width:
            if self._pos[1] < mouse_pos[1] < self._pos[1] + self._height:
                if event_type == pygame.MOUSEBUTTONDOWN:
                    self._state.name("onClick")
                elif event_type == pygame.MOUSEMOTION:
                    self._state.name("onHover")
                return True
            self._state.name("Static")
            return False
