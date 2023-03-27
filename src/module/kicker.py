import pygame
from module.colors import BLACK

class Fooser:
    def __init__(self, x, y):
        self._x = x
        self._y = y
        self._chargingPower = 0

    def move(self, x, y):
        self._x = x
        self._y = y

    def add_force(self, ball, direction, power):
        force_x = ball._rect.x - self._x
        force_y = ball._rect.y - self._y
        force_x *= 10
        force_y *= 10
        force_x += direction * 500 + power
        ball.add_force(force_x, force_y)
        ball.set_speed(ball._speed + 20 + power/20)

    def charging(self):
        self._chargingPower += 1
        if self._chargingPower > 400:
            self._chargingPower = 400

    def kick(self, ball, player):
        if ball._rect.right < self._x + 50 and ball._rect.left > self._x - 50:
            if ball._rect.top < self._y + 30 and ball._rect.bottom > self._y - 30:
                if player == 0:
                    if ball._direction[0] < 0:
                        ball._direction[0] *= -1
                    self.add_force(ball, 1, self._chargingPower)
                if player == 1:
                    if ball._direction[0] > 0:
                        ball._direction[0] *= -1
                    self.add_force(ball, -1, self._chargingPower)
        self._chargingPower = 0


class Bar:
    def __init__(self, nb, team, size, x):
        self._number = nb
        self._team = team
        self._x = x
        self._y = (900/2)
        self._speed = 20
        self.size = size
        self._foosers = list()
        if self._number == 1:
            self._foosers.append(Fooser(self._x, self._y))
        else:
            for i in range(0, self._number):
                self._foosers.append(Fooser(self._x, self._y - ((self.size - 60)/(self._number - 1)) * i + (self.size - 60)/2))


    def move(self, kicker, direction):
        self._y += 10 * direction
        if self._y > (900 / 2) + (kicker.size_y/2) - self.size/2:
            self._y = (900 / 2) + (kicker.size_y/2) - self.size/2
        if self._y < (900 / 2) - (kicker.size_y/2) + self.size/2:
            self._y = (900 / 2) - (kicker.size_y/2) + self.size/2
        if self._number == 1:
            self._foosers[0].move(self._x, self._y)
        else:
            for i in range(0, self._number):
                self._foosers[i].move(self._x, self._y - ((self.size - 60)/(self._number - 1)) * i + (self.size - 60)/2)

    def draw(self, window):
        color = (0, 0, 255)
        if self._team == 1:
            color = (255, 0, 0)
        for fooser in self._foosers:
            player_line = pygame.Surface((40, 40))
            player_line.fill(color)
            rect = player_line.get_rect()
            rect.center = (fooser._x, fooser._y)
            window.blit(player_line, rect)
        line = pygame.Surface((10, self.size))
        line.fill(color)
        rect = line.get_rect()
        rect.center = (self._x, self._y)
        window.blit(line, rect)

    def kick(self, ball):
        for fooser in self._foosers:
            fooser.kick(ball, self._team)

    def charging(self):
        for fooser in self._foosers:
            fooser.charging()




class Kicker:
    def __init__(self, size_x, size_y, background):
        self.size_x = size_x
        self.size_y = size_y
        self.bars = list()
        self.bars.append(Bar(1, 0, (self.size_y - 200), (1600/2) - (self.size_x/2) + ((size_x) / 7) * 1 - 100))
        self.bars.append(Bar(2, 0, (self.size_y - 300), (1600/2) - (self.size_x/2) + ((size_x) / 7) * 2 - 60))
        self.bars.append(Bar(3, 1, (self.size_y - 200), (1600/2) - (self.size_x/2) + ((size_x) / 7) * 3 - 30))
        self.bars.append(Bar(3, 0, (self.size_y - 200), (1600/2) - (self.size_x/2) + ((size_x) / 7) * 4 + 30))
        self.bars.append(Bar(2, 1, (self.size_y - 300), (1600/2) - (self.size_x/2) + ((size_x) / 7) * 5 + 60))
        self.bars.append(Bar(1, 1, (self.size_y - 200), (1600/2) - (self.size_x/2) + ((size_x) / 7) * 6 + 100))
        self._background = background
        self._background_rect = self._background.get_rect()

    def playerMovement(self, player, direction):
        for bar in self.bars:
            if bar._team == player:
                bar.move(self, direction)

    def draw(self, window):
        for bar in self.bars:
            bar.draw(window)

    def charging(self, player):
        for bar in self.bars:
            if bar._team == player:
                bar.charging()

    def kick(self, player, ball):
        for bar in self.bars:
            if bar._team == player:
                bar.kick(ball)

    def draw_background(self, window):
        window.fill(BLACK)
        window.blit(self._background, (0, 0))

    def draw(self, window, outline=None):
        self.draw_background(window)
