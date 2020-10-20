import pygame
from pygame.draw import *
from random import randint
pygame.init()
import math

FPS = 15#FPS....
screen = pygame.display.set_mode((1200, 900))#задаем экран
RED = (255, 0, 0)          #цваета
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN] #массив с цветами

vgrx = 800 #Верхняя граница по x
ngrx = 100 #Нижняя граница по x
vgry = 500 #верхняя граница по y
ngry = 20  #нижняя граница по y

score = 0 #счет
ball = [] #мячик
score = 0 #счет
temp = 0  # временная перемепнная
randomnayachtyka = 0 #другая временная штука


class mball:
    """
    класс масинвых шаров где х у их координаты vx,vy их скорости timer время жизни ,r радиус,color-цвет + они дрожжат для сложночти попадания
    """
    def __init__(self, x, y, vx, vy, r, timer, color):#инциализация
        x = self.x = randint(300, 400)
        y = self.y = randint(300, 400)
        vx = self.vx = randint(-5, 5)
        vy = self.vy = randint(-5, 5)
        r = self.r = randint(20, 50)
        timer = self.timer = randint(100, 500)
        color = self.color = (255, 255, 255)

    def dviz(self):
        #движение шарика
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


class uball:
    #аналогично для mball (только это ultra ball поэтому скорости в 10 раз быстрее(не дрожжит)!!!
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
        #аналогично mball-у
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
            print(999000000000)
        if self.r > 0:
            circle(screen, self.color, (int(self.x), int(self.y)), self.r)


pygame.display.update()      #просто обновление экрана и вспомогательные переменные
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True     #выход из игры
        elif event.type == pygame.MOUSEBUTTONDOWN:   #нажатие и проверка попал ли по шарику если да
                                                     # то шраик исчезает и прибавляетсья очко
            for i in range(0, len(ball)):
                if ((ball[i].x - pygame.mouse.get_pos()[0]) ** 2 + (ball[i].y - pygame.mouse.get_pos()[1]) ** 2) < (
                        (ball[i].r) ** 2):
                    ball[i].r = 0
                    score = score + 1

    for i in range(len(ball)):#проработка столкновения шаров
        for p in range(i, len(ball)):
            if ((((ball[i].r) + (ball[p].r)) ** 2 > (((ball[i].x) - (ball[p].x)) ** 2) + ((ball[i].y) - (ball[p].y)) ** 2)):
                if ball[i].x - ball[p].x != 0:
                    ball[i].vx = ((ball[i].x - ball[p].x) / math.fabs(ball[i].x - ball[p].x)) * ball[i].vx
                    ball[p].vx = ((ball[i].x - ball[p].x) / math.fabs(ball[i].x - ball[p].x)) * ball[p].vx * -1
                if ball[i].y - ball[p].y != 0:
                    ball[i].vy = ((ball[i].y - ball[p].y) / math.fabs(ball[i].y - ball[p].y)) * ball[i].vy
                    ball[i].vy = ((ball[i].y - ball[p].y) / math.fabs(ball[i].y - ball[p].y)) * ball[i].vy * -1
                if ball[i].x - ball[p].x == 0:
                    ball[i].x=ball[p].x+randint(-5,5)
                if ball[i].y - ball[p].y == 0:
                    ball[i].y=ball[p].y+randint(-5,5)

    for i in ball:#удаление мертвых шаров
        if i.r == 0:
            ball.remove(i)

    temp = temp - 1#временная счетчик переменная которая говорит когда добавить шарик
    if temp < 0:
        temp = 50
        randomnayachtyka = randint(0, 3)#нужно чтобы одних шаров было примерно больше чем других (можно было через else
                                        #но мне захотелось так
        if randomnayachtyka == 0:
            ball.append(mball(0, 0, 0, 0, 0, 0, 0, ))
        if randomnayachtyka != 0:
            ball.append(uball(0, 0, 0, 0, 0, 0, 0, ))

    screen.fill(BLACK)     #обновление экрана
    for i in range(len(ball)):#движение шаров и выписывание счета
        ball[i].dviz()
    screen.blit(pygame.font.Font(None, 36).render('Score: '+str(score), 0, (255, 255, 255)), (10, 50))

    pygame.display.update()

pygame.quit()
