from module.window import Window
from module.ball import Ball
from module.kicker import Kicker
from module.colors import *
import pygame


gameRunning = True
ball = Ball([1600 / 2, 900 / 2], (10, 10), ORANGE)
kicker = Kicker(1200, 600)
z_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False
e_pressed = False
ZERO_pressed = False


def event_game_handler(event, window):
    global gameRunning, z_pressed, s_pressed, up_pressed, down_pressed, kicker, ball

    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            gameRunning = False
        elif event.key == pygame.K_F12:
            window.set_fullscreen()
        elif event.key == pygame.K_z:
            z_pressed = True
        elif event.key == pygame.K_s:
            s_pressed = True
        elif event.key == pygame.K_UP:
            up_pressed = True
        elif event.key == pygame.K_DOWN:
            down_pressed = True
        elif event.key == pygame.K_e:
            e_pressed = True
        elif event.key == pygame.K_KP0:
            ZERO_pressed = True

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_z:
            z_pressed = False
        elif event.key == pygame.K_s:
            s_pressed = False
        elif event.key == pygame.K_UP:
            up_pressed = False
        elif event.key == pygame.K_DOWN:
            down_pressed = False
        elif event.key == pygame.K_e:
            e_pressed = False
            kicker.kick(0, ball)
        elif event.key == pygame.K_KP0:
            ZERO_pressed = False
            kicker.kick(1, ball)

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
    global kicker
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

    kicker.draw(window)


def gameLoop(window, running):
    global gameRunning

    gameRunning = running
    while gameRunning:
        window.get_clock().tick(window.get_fps())
        for event in pygame.event.get():
            event_game_handler(event, window)
        if z_pressed:
            kicker.playerMovement(0, -1)
        if s_pressed:
            kicker.playerMovement(0, 1)
        if up_pressed:
            kicker.playerMovement(1, -1)
        if down_pressed:
            kicker.playerMovement(1, 1)
        if e_pressed:
            kicker.charging(0)
        if ZERO_pressed:
            kicker.charging(1)
        drawField(window.get_screen())
        ball.update(kicker)
        ball.draw(window.get_screen())
        pygame.display.flip()
        pygame.display.update()
