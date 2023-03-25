import pygame


class Window:
    def __init__(self, size, name, fps=60, mode=None):
        self._size = size
        self._mode = mode
        if self._mode is not None:
            self._screen = pygame.display.set_mode(self._size, self._mode)
        else:
            self._screen = pygame.display.set_mode(self._size)
        self._name = name
        self._fps = fps
        self._clock = pygame.time.Clock()
        pygame.display.set_caption(self._name)

    def set_fullscreen(self):
        if self._mode is not None:
            self._mode = None
            self._screen = pygame.display.set_mode(self._size)
        else:
            self._mode = pygame.FULLSCREEN
            self._screen = pygame.display.set_mode(self._size, self._mode)

    def get_screen(self):
        return self._screen

    def get_clock(self):
        return self._clock

    def get_fps(self):
        return self._fps

    def size(self, new_size):
        self._size = new_size
        if self._mode is not None:
            self._screen = pygame.display.set_mode(self._size, self._mode)
        else:
            self._screen = pygame.display.set_mode(self._size)

    def fps(self, new_fps):
        self._fps = new_fps

    def mode(self, new_mode):
        self._mode = new_mode
        if self._mode is not None:
            self._screen = pygame.display.set_mode(self._size, self._mode)
        else:
            self._screen = pygame.display.set_mode(self._size)

    def name(self, new_name):
        self._name = new_name
        pygame.display.set_caption(self._name)


pygame.init()
info = pygame.display.Info()
WIDTH, HEIGHT = info.current_w, info.current_h
window = Window((WIDTH, HEIGHT), "Kicker", 60, None)
