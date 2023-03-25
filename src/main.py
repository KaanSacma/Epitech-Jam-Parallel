import pygame
from module.window import Window

running = True


def event_handler(event, window):
    global running

    if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_F11:
            window.set_fullscreen()


def main():
    global running
    window = Window((1920, 1080), "Kicker", 60, None)

    while running:
        window.get_clock().tick(window.get_fps())
        for event in pygame.event.get():
            event_handler(event, window)
        window.get_screen().fill((0, 0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
