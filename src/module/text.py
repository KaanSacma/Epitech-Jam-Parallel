from module.colors import *


class Text:
    def __init__(self, text="", font_path="./assets/fonts/Kenney Pixel.ttf", font_size=16, font_color=WHITE):
        self._text = text
        self._font_path = font_path
        self._font_size = font_size
        self._font_color = font_color

    def get_text(self):
        return self._text

    def get_font_path(self):
        return self._font_path

    def get_font_size(self):
        return self._font_size

    def get_font_color(self):
        return self._font_color
