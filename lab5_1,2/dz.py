import pygame
from pygame.draw import *
from random import randint

pygame.init()
import math

FPS = 15  # FPS....
screen = pygame.display.set_mode((1200, 900))  # задаем экран
RED = (255, 0, 0)  # цваета
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]  # массив с цветами

exitrimer = 200  # число указывающее время выход при 200 = 15 секунд
yes = False  # переменная отвечающая за согласие продолжения игры
countvis = 0

vgrx = 800  # Верхняя граница по x
ngrx = 100  # Нижняя граница по x
vgry = 500  # верхняя граница по y
ngry = 20  # нижняя граница по y

score = 0  # счет
ball = []  # мячик
cnar = []  # массив снарядов
score = 0  # счет
temp = 0  # временная перемепнная
randomnayachtyka = 0  # другая временная штука


class bullet:
    """
    Класс снаярдов которыми плюеться пушка x,y-координаты ,vx,vx-скорости по ним
    """

    def __init__(self, x, y, vx, vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy

    def dviz(self):
        """
        Функция движения снарядов с учетом гравитации и трения ,также прорисовывает шары
        """
        self.x = int(self.x + self.vx)
        self.y = int(self.y + self.vy)
        if self.x - 10 < ngrx:
            self.vx = (self.vx * self.vx) ** 0.5
        if self.x + 10 > vgrx:
            self.vx = -1 * (self.vx * self.vx) ** 0.5
        if self.y - 10 < ngry:
            self.vy = (self.vy * self.vy) ** 0.5
        if self.y + 10 > vgry:
            self.vy = (-1 * (self.vy * self.vy) ** 0.5) * 0.5
        if self.y + 10 < vgry:
            self.vy = self.vy + 0.5
            self.vx = self.vx * 0.98
        else:
            if self.vy ** 2 < 4:
                self.vy = 0
                self.vx = self.vx * 0.98
                if self.vx ** 2 < 1:
                    self.vx = 0
        if (self.vx ** 2 + self.vy ** 2) > 0:
            circle(screen, (255, randint(120, 255), 0), (int(self.x), int(self.y)), 10)


class mball:
    """
    класс масинвых шаров где х у их координаты vx,vy их скорости timer время жизни ,r радиус,color-цвет + они дрожжат для сложночти попадания
    """

    def __init__(self, x, y, vx, vy, r, timer, color):  # инциализация
        x = self.x = randint(300, 400)
        y = self.y = randint(300, 400)
        vx = self.vx = randint(-5, 5)
        vy = self.vy = randint(-5, 5)
        r = self.r = randint(20, 50)
        timer = self.timer = randint(100, 500)
        color = self.color = (255, 255, 255)

    def dviz(self):
        # движение шарика
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.timer = self.timer - 1
        if self.x - self.r < ngrx:
            self.vx = (self.vx * self.vx) ** 0.5
        if self.x + self.r > vgrx:
            self.vx = -1 * (self.vx * self.vx) ** 0.5
        if self.y - self.r < ngry:
            self.vy = (self.vy * self.vy) ** 0.5
        if self.y + self.r > vgry:
            self.vy = -1 * (self.vy * self.vy) ** 0.5
        if self.timer == 0:
            self.r = 0
        if self.r > 0:
            circle(screen, self.color, (int(self.x), int(self.y)), self.r)


def pychka():
    """
    функция отвечающая за поворот пушки(lx,ly-координаты конца пушки в случае выхода за длинну ,k коофициент показывает насколько близка длинна пушки к максимальной длинне
    (надо было чтобы пушка красиво меняла цвет)
    """
    if ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5 > 100:
        lx = 100 * (pygame.mouse.get_pos()[0] - 400) / (
                ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5)
        ly = 100 * (pygame.mouse.get_pos()[1] - 600) / (
                ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5)
        lx = int(lx)
        ly = int(ly)
        pygame.draw.line(screen, (200, randint(0, 100), randint(1, 100)), (400, 600), (400 + lx, 600 + ly), 10)
    else:
        k = ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5
        pygame.draw.line(screen, (int(k * 2.55), 25, 25), (400, 600), pygame.mouse.get_pos(), 10)


def vistrel():
    """
    функция отвечает за проработку выстрела(добавоения снаряда,увелечения скорости пропорцианально длинне пушки(скорость направлена вдоль пушки),lx,ly координаты конца пушки
    (использовались те же обозначение что и в другой функции тк начальная координата шарика это координата конца пушки)))
    powerx,powery-отвечает за скорость по соответсвующим осям
    """
    if ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5 > 100:
        lx = 100 * (pygame.mouse.get_pos()[0] - 400) / (
                ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5)
        ly = 100 * (pygame.mouse.get_pos()[1] - 600) / (
                ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5)
        lx = int(lx) + 400
        ly = int(ly) + 600
    else:
        lx = pygame.mouse.get_pos()[0]
        ly = pygame.mouse.get_pos()[1]

    if ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5 > 100:
        powerx = 33 * (pygame.mouse.get_pos()[0] - 400) / (
                ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5)
        powery = 33 * (pygame.mouse.get_pos()[1] - 600) / (
                ((pygame.mouse.get_pos()[0] - 400) ** 2 + (pygame.mouse.get_pos()[1] - 600) ** 2) ** 0.5)
        powerx = int(powerx)
        powery = int(powery)
        cnar.append(bullet(lx, ly, powerx, powery))
    else:
        cnar.append(
            bullet(lx, ly, int((pygame.mouse.get_pos()[0] - 400) / 3), int((pygame.mouse.get_pos()[1] - 600) / 3)))


class uball:
    # аналогично для mball (только это ultra ball поэтому скорости в 10 раз быстрее(не дрожжит)!!!
    def __init__(self, x, y, vx, vy, r, timer, color):
        x = self.x = randint(300, 400)
        y = self.y = randint(300, 400)
        vx = self.vx = randint(-5, 5) * 10
        vy = self.vy = randint(-5, 5) * 10
        time = self.time = 0
        r = self.r = randint(20, 50)
        timer = self.timer = randint(20, 50)
        color = self.color = COLORS[randint(0, 5)]

    def dviz(self):
        # аналогично mball-у
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.timer = self.timer - 1
        if self.x - self.r < ngrx:
            self.vx = (self.vx * self.vx) ** 0.5
        if self.x + self.r > vgrx:
            self.vx = -1 * (self.vx * self.vx) ** 0.5
        if self.y - self.r < ngry:
            self.vy = (self.vy * self.vy) ** 0.5
        if self.y + self.r > vgry:
            self.vy = -1 * (self.vy * self.vy) ** 0.5
        if self.timer == 0:
            self.r = 0
        if self.r > 0:
            circle(screen, self.color, (int(self.x), int(self.y)), self.r)


pygame.display.update()  # просто обновление экрана и вспомогательные переменные
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True  # выход из игры
        elif event.type == pygame.MOUSEBUTTONDOWN:  # нажатие и проверка попал ли по шарику если да
            vistrel()  # выстрел...
            countvis += 1
            if exitrimer < 0 and yes != True:  # отвечает за то,что после шелчка игра перезапустить (подтверждение шелчка)
                yes = True

    for i in range(len(ball)):  # проработка столкновения шаров
        for p in range(i, len(ball)):
            if (
                    (((ball[i].r) + (ball[p].r)) ** 2 > (((ball[i].x) - (ball[p].x)) ** 2) + (
                            (ball[i].y) - (ball[p].y)) ** 2)):
                if ball[i].x - ball[p].x != 0:
                    ball[i].vx = ((ball[i].x - ball[p].x) / math.fabs(ball[i].x - ball[p].x)) * ball[i].vx
                    ball[p].vx = ((ball[i].x - ball[p].x) / math.fabs(ball[i].x - ball[p].x)) * ball[p].vx * -1
                if ball[i].y - ball[p].y != 0:
                    ball[i].vy = ((ball[i].y - ball[p].y) / math.fabs(ball[i].y - ball[p].y)) * ball[i].vy
                    ball[i].vy = ((ball[i].y - ball[p].y) / math.fabs(ball[i].y - ball[p].y)) * ball[i].vy * -1
                if ball[i].x - ball[p].x == 0:
                    ball[i].x = ball[p].x + randint(-5, 5)
                if ball[i].y - ball[p].y == 0:
                    ball[i].y = ball[p].y + randint(-5, 5)

    for i in ball:  # удаление мертвых шаров
        if i.r == 0:
            ball.remove(i)

    temp = temp - 1  # временная счетчик переменная которая говорит когда добавить шарик
    if temp < 0:
        temp = 50
        randomnayachtyka = randint(0,
                                   3)  # нужно чтобы одних шаров было примерно больше чем других (можно было через else
        # но мне захотелось так)
        if randomnayachtyka == 0:
            ball.append(mball(0, 0, 0, 0, 0, 0, 0, ))
        if randomnayachtyka != 0:
            ball.append(uball(0, 0, 0, 0, 0, 0, 0, ))

    screen.fill(BLACK)  # обновление экрана
    for i in range(len(ball)):  # движение шаров и выписывание счета
        ball[i].dviz()
    for i in range(len(cnar)):  # движение
        cnar[i].dviz()
    screen.blit(pygame.font.Font(None, 36).render('Score: ' + str(score), 0, (255, 255, 255)),
                (10, 50))  # пишет счет во время игры
    pychka()
    for i in range(0, len(
            ball)):  # условие пересечение снарядом шариков (с блокиратором счетчика после того как выйден время)
        for p in range(0, len(cnar)):
            if (cnar[p].vx ** 2 + cnar[p].vy ** 2) > 0:
                if (
                        (((ball[i].r) + (10)) ** 2 > (((ball[i].x) - (cnar[p].x)) ** 2) + (
                                (ball[i].y) - (cnar[p].y)) ** 2)):
                    ball[i].r = 0
                    if exitrimer > 0:
                        score = score + 1
    exitrimer = exitrimer - 1
    if exitrimer > 0:  # рисует время которое осталось до окончания игры (рисует полоску,посторался сделать чтобы мигала)
        pygame.draw.line(screen, (randint(30, 255 - exitrimer), randint(1, 30), randint(1, 30)), (1100 - exitrimer, 70),
                         (1100, 70), 10)
    if exitrimer < 0:  # условие заканчивания времени,в случае подтверждения перезапуска обнулит масивы шаров и снарядов ,а также счетчик
        screen.fill(BLACK)
        screen.blit(pygame.font.Font(None, 36).render(
            'Время вышло,ваш счет : ' + str(score) + ' количесвто выстрелов : ' + str(
                countvis) + ' чтобы продолжить нажмите ПКМ', 0, (255, 255, 255)),
            (50, 400))
        if yes == True:
            for i in range(len(ball)):  # движение шаров и выписывание счета
                ball.pop()
            for i in range(len(cnar)):  # движение
                cnar.pop()
            score = 0
            yes = False
            exitrimer = 200

    pygame.display.update()

pygame.quit()
