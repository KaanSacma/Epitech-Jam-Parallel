from module.window import Window
from module.ball import Ball
from module.colors import *
import pygame


gameRunning = True
ball = Ball([1920 / 2, 50], (10, 10), ORANGE)


def event_game_handler(event, window):
    global gameRunning

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            gameRunning = False
        elif event.key == pygame.K_F12:
            window.set_fullscreen()
        elif event.key == pygame.K_z:
            setBallSpawnUp()
        elif event.key == pygame.K_s:
            setBallSpawnDown()
    elif event.type == pygame.QUIT:
        gameRunning = False


def setBallSpawnDown():
    global ball
    ball.set_speed(0)
    ball.set_spawn([1920 / 2, 1030])


def setBallSpawnUp():
    global ball
    ball.set_speed(0)
    ball.set_spawn([1920 / 2, 20])


def draw_donut_circle(window):
    circle_radius = 150
    circle_thickness = 10
    circle_x = 1920 / 2
    circle_y = 1080 / 2

    pygame.draw.circle(window, WHITE, (circle_x, circle_y), circle_radius)
    pygame.draw.circle(window, BLACK, (circle_x, circle_y), circle_radius-circle_thickness)


def drawField(window):
    pygame.draw.rect(window, BLACK, (0, 0, 1920, 1080))

    line = pygame.Surface((10, 2100))
    line.fill(WHITE)
    rotated_surface = pygame.transform.rotate(line, 180)
    rect = rotated_surface.get_rect()
    rect.center = (1920 / 2, 0)

    draw_donut_circle(window)
    window.blit(rotated_surface, rect)


def gameLoop(window, running):
    global gameRunning

    gameRunning = running
    while gameRunning:
        window.get_clock().tick(window.get_fps())
        for event in pygame.event.get():
            event_game_handler(event, window)
        drawField(window.get_screen())
        ball.update()
        ball.draw(window.get_screen())
        pygame.display.flip()
        pygame.display.update()
