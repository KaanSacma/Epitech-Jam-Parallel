import sys
from module.button import *
from module.image import *
from module.text import *
from module.menu import *


def close_game():
    pygame.display.quit()
    pygame.quit()
    sys.exit()


def create_menu():
    images = [
        Image("./assets/buttons/blue_button_static.png").get(),
        Image("./assets/buttons/blue_button_onHover.png").get(),
        Image("./assets/buttons/blue_button_onClick.png").get()
    ]
    buttons = [
        Button(images, [(1600 / 2) - 95, 300], None, Text("Play", "./assets/fonts/Kenney Pixel.ttf", 32, WHITE)),
        Button(images, [(1600 / 2) - 95, 440], close_game, Text("Quit", "./assets/fonts/Kenney Pixel.ttf", 32, WHITE))
    ]
    MainMenu = Menu(Image("./assets/images/background.jpeg").get(), buttons, "MainMenu")
    return MainMenu
