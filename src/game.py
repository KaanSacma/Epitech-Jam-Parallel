from module.window import Window
from module.ball import Ball
from module.kicker import Kicker
from module.colors import *
import pygame


gameRunning = True
ball = Ball([1600 / 2, 50], (10, 10), ORANGE)
kicker = Kicker(1200, 600)


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
    ball.set_spawn([1600 / 2, 1030])


def setBallSpawnUp():
    global ball
    ball.set_speed(0)
    ball.set_spawn([1600 / 2, 20])


def draw_donut_circle(window):
    circle_radius = 150
    circle_thickness = 10
    circle_x = 1600 / 2
    circle_y = 900 / 2

    pygame.draw.circle(window, WHITE, (circle_x, circle_y), circle_radius)
    pygame.draw.circle(window, BLACK, (circle_x, circle_y), circle_radius-circle_thickness)


def drawField(window):
    pygame.draw.rect(window, BLACK, (0, 0, 1600, 900))

    line = pygame.Surface((10, kicker.size_y))
    line.fill(WHITE)
    vertical_line = pygame.transform.rotate(line, 180)
    rect = vertical_line.get_rect()

    draw_donut_circle(window)

    rect.center = (1600 / 2, 900/2)
    window.blit(vertical_line, rect) # ligne milieu

    rect.center = (1600 / 2 - kicker.size_x/2, 900/2)
    window.blit(vertical_line, rect)  # ligne gauche

    rect.center = (1600 / 2 + kicker.size_x / 2, 900/2)
    window.blit(vertical_line, rect)  # ligne droite

    horizontal_line = pygame.Surface((kicker.size_x, 10))
    horizontal_line.fill(WHITE)
    rect = horizontal_line.get_rect()
    rect.center = (1600 / 2, 900 / 2 + kicker.size_y/2)
    window.blit(horizontal_line, rect)  # ligne haut

    rect.center = (1600 / 2, 900 / 2 - kicker.size_y/2)
    window.blit(horizontal_line, rect)  # ligne bas


def gameLoop(window, running):
    global gameRunning

    gameRunning = running
    while gameRunning:
        window.get_clock().tick(window.get_fps())
        for event in pygame.event.get():
            event_game_handler(event, window)
        drawField(window.get_screen())
        ball.update(kicker)
        ball.draw(window.get_screen())
        pygame.display.flip()
        pygame.display.update()
