import pygame                       #загружаем библиотеки
import math
from pygame.draw import *
from random import randint

##############################################
pygame.init()
timer = 1000                                             #параментр от которого зависит через какое время
                                                         # будут появлятсья новые шарики чем больше тем дольше
FPS = 10                                                 #FPS...
screen = pygame.display.set_mode((900, 700))             #Экран
score = 0                                                #счетчик очков
RED = (255, 0, 0)                                        #Цвета
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (30, 30, 30)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]      #набор цветов
chislo = 10                                             #число шаров(максимальное)
##############################################
x = []                                        #Это списки переменных для каждого шарика x-координата шарка x
y = []                                        #y-координата шарика y,
vx = []                                       #vx,vy- скорость по соответсвующим осям
vy = []                                       #
r = []                                        #r-радиус шарика
color = []                                    #color-цвет шарика
cychect = []                                  #cychect-отвеает за то сущесвует ли шарик в
                                              # принципе(если True то он отображаеться и дает очки,False - наоборот
time = []                                     #time-время через которое ичезает шарик
##############################################
for i in range(chislo):                       #Дали пустые ячейки для шариков(по каждой переменной)
    cychect.append(False)
    x.append(0)
    y.append(0)
    vx.append(0)
    vy.append(0)
    r.append(0)
    color.append(0)
    time.append(0)


##############################################
def dobavki():
    '''
    Функция добавляет шарик если есть для него места проверяя на параметр False все места масива
    (если False то добавит шарик с произвольными параметрами)
    '''
    if cychect.count(False) > 0:
        nomer_pystogo = cychect.index(False, 0, chislo)
        x[nomer_pystogo] = randint(300, 600)
        y[nomer_pystogo] = randint(200, 500)
        vx[nomer_pystogo] = ((-1) ** randint(1, 2)) * 5
        vy[nomer_pystogo] = ((-1) ** randint(1, 2)) * 5
        color[nomer_pystogo] = COLORS[randint(0, 5)]
        time[nomer_pystogo] = randint(200, 1000)
        r[nomer_pystogo] = randint(10, 35)
        cychect[nomer_pystogo] = True


##############################################
for i in range(chislo - 1):                  #заполняет масив шариков и показывает красоту функций
    dobavki()


##############################################
def dvizh():
    """
    Функция отвечает за перемещение шариков на расстояние
    также отвечает за их исчезновение со временем и ограниением их движения "стенками" размеры
    которых вписываються ниже в условия
    """
    screen.fill((0, 0, 0))
    for i in range(chislo - 1):
        if cychect[i]:
            x[i] = vx[i] + x[i]
            y[i] = vy[i] + y[i]
            if x[i] - r[i] > 500:
                vx[i] = int(-1 * math.fabs(vx[i]))
                vy[i] = ((-1) ** randint(1, 2)) * 5
            if x[i] + r[i] < 100:
                vx[i] = int(math.fabs(vx[i]))
                vx[i] = ((-1) ** randint(1, 2)) * 5
            if y[i] - r[i] > 500:
                vy[i] = int(-1 * math.fabs(vy[i]))
                vy[i] = ((-1) ** randint(1, 2)) * 5
            if y[i] - r[i] < 100:
                vy[i] = int(math.fabs(vy[i]))
                vy[i] = ((-1) ** randint(1, 2)) * 5
            circle(screen, color[i], (x[i], y[i]), r[i])
            time[i] = time[i] - 1
            if time[i] <= 0:
                x[i] = 0
                y[i] = 0
                vx[i] = 0
                vy[i] = 0
                r[i] = 0
                cychect[i] = False
                time[i] = 1


##############################################
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:                             #
    clock.tick(FPS)                             #Пропускаем время и перемещаем шарики
    dvizh()                                     #
    timer = timer - 20                          #
    if timer <= 0:                              # проверка на условие добавления шариков
        dobavki()
        timer = 1000
    for event in pygame.event.get():
        pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:#Проверяет расстояние от щелчка до всех шариков,если попадает в
                                                  #радиус то шарик"исчезает" и начисляеться очко которое пишеться ниже
            for i in range(chislo):
                if r[i] ** 2 >= (((x[i] - pygame.mouse.get_pos()[0]) ** 2) + ((y[i] - pygame.mouse.get_pos()[1]) ** 2)):
                    score = score + 1
                    print(score)
                    cychect[i] = False
    pygame.display.update()
pygame.quit()
