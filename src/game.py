from module.window import Window
from module.ball import Ball
from module.kicker import Kicker
from module.colors import *
from module.image import *
import pygame


gameRunning = True
ball = Ball([1600 / 2, 900 / 2], (10, 10), Image("./assets/images/ball.jpeg").get())
kicker = Kicker(1200, 600, Image("./assets/images/KICKer.jpg").get(), Image("./assets/images/player.png").get())
z_pressed = False
s_pressed = False
up_pressed = False
down_pressed = False
e_pressed = False
ZERO_pressed = False
scoreL = 0
scoreR = 0


def event_game_handler(event, window):
    global gameRunning, z_pressed, s_pressed, up_pressed, down_pressed, kicker, ball, e_pressed, ZERO_pressed

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
    ball.set_spawn([1600 / 2, 300])


def setBallSpawnUp():
    global ball
    ball.set_speed(0)
    ball.set_spawn([1600 / 2, 600])


def draw_donut_circle(window):
    circle_radius = 150
    circle_thickness = 10
    circle_x = 1600 / 2
    circle_y = 900 / 2

    pygame.draw.circle(window, WHITE, (circle_x, circle_y), circle_radius)
    pygame.draw.circle(window, GREEN,(circle_x, circle_y), circle_radius-circle_thickness)


def drawField(window):
    line = pygame.Surface((10, kicker.size_y))
    line.fill(WHITE)
    vertical_line = pygame.transform.rotate(line, 180)
    rect = vertical_line.get_rect()

    #draw_donut_circle(window)

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


def get_score(window):
    global scoreL, scoreR

    if ball.get_pos()[0] < 220 and ball.get_pos()[1] >= 450 and ball.get_pos()[1] <= 550:
        scoreR += 1
        setBallSpawnDown()
        ball.set_direction([-1, -1])
    elif ball.get_pos()[0] > 1300 and ball.get_pos()[1] >= 450 and ball.get_pos()[1] <= 550:
        scoreL += 1
        setBallSpawnUp()
        ball.set_direction([1, 1])


def gameLoop(window, running):
    global gameRunning, scoreR, scoreL
    font = pygame.font.Font(None, 36)
    pygame.font.init()

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
        get_score(window)
        kicker.draw_background(window.get_screen())
        drawField(window.get_screen())
        ball.update(kicker)
        ball.draw(window.get_screen())
        score_text = font.render("Score Player1: " + str(scoreL), True, (120, 120, 255))
        window.get_screen().blit(score_text, (30, 10))
        score_text2 = font.render("Score Player2: " + str(scoreR), True, (120, 120, 255))
        window.get_screen().blit(score_text2, (1200, 10))
        pygame.display.flip()
        pygame.display.update()
