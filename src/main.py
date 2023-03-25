import pygame
from module.window import Window
from menu import create_menu

running = True
currentMenu = create_menu()


def event_handler(event, window):
    global running, currentMenu

    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            window.set_fullscreen()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        for i in range(len(currentMenu.get_buttons())):
            if currentMenu.get_button(i).is_hover(event.type):
                if currentMenu.get_button(i).get_function() is not None:
                    currentMenu.get_button(i).execute_function()
                return ()
    elif event.type == pygame.MOUSEMOTION:
        for i in range(len(currentMenu.get_buttons())):
            currentMenu.get_button(i).is_hover(event.type)


def main():
    global running, currentMenu
    pygame.init()
    window = Window((1920, 1080), "Kicker", 60, None)

    while running:
        window.get_clock().tick(window.get_fps())
        for event in pygame.event.get():
            event_handler(event, window)
        currentMenu.draw(window.get_screen(), None)
        pygame.display.flip()


if __name__ == '__main__':
    main()
