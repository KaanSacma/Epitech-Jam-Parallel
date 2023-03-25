class Color:
    def __init__(self, red, green, blue):
        self._red = red
        self._green = green
        self._blue = blue

    def get_color(self):
        return self._red, self._green, self._blue


WHITE = Color(255, 255, 255).get_color()
BLACK = Color(0, 0, 0).get_color()
RED = Color(255, 0, 0).get_color()
GREEN = Color(0, 255, 0).get_color()
BLUE = Color(0, 0, 255).get_color()
YELLOW = Color(255, 255, 0).get_color()
CYAN = Color(0, 255, 255).get_color()
MAGENTA = Color(255, 0, 255).get_color()
GRAY = Color(128, 128, 128).get_color()
LIGHT_GRAY = Color(211, 211, 211).get_color()
DARK_GRAY = Color(169, 169, 169).get_color()
ORANGE = Color(255, 165, 0).get_color()
LIGHT_ORANGE = Color(255, 200, 0).get_color()
DARK_ORANGE = Color(255, 140, 0).get_color()
PURPLE = Color(128, 0, 128).get_color()
LIGHT_PURPLE = Color(153, 50, 204).get_color()
DARK_PURPLE = Color(75, 0, 130).get_color()
BROWN = Color(165, 42, 42).get_color()
LIGHT_BROWN = Color(139, 69, 19).get_color()
DARK_BROWN = Color(101, 67, 33).get_color()
PINK = Color(255, 192, 203).get_color()
LIGHT_PINK = Color(255, 182, 193).get_color()
DARK_PINK = Color(255, 105, 180).get_color()
