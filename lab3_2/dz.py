import pygame  #
from pygame.draw import *  # Подключаем библиотеки
from pygame.transform import *  #

pygame.init()
FPS = 30  # FPS...
screen = pygame.display.set_mode((400, 560))  # Создаем и обызваем экран указывая в скобочках его размеры
ascreen = pygame.Surface((400, 560))  # Дополнительно поле несет лишь вспомогательную функцию


##################################################################
def draw_dom(x, y, k, t):
    '''
    Функия рисует будтку с координатами центра "входа" x,y
    k-определяет размер
    t-если 1 рисует стандартную будку,если 0 то отражает ее
    '''
    if t == 1:
        polygon(screen, (255, 204, 0),
                [(x - int(30 * k), y - int(40 * k)), (x + int(40 * k), y - int(30 * k)),
                 (x + int(40 * k), y + int(40 * k)),
                 (x - int(30 * k), y + int(30 * k))], 0)
        polygon(screen, (0, 0, 0),
                [(x - int(30 * k), y - int(40 * k)), (x + int(40 * k), y - int(30 * k)),
                 (x + int(40 * k), y + int(40 * k)),
                 (x - int(30 * k), y + int(30 * k))], 1)
        polygon(screen, (255, 204, 0),
                [(x + int(40 * k), y - int(30 * k)), (x + int(70 * k), y - int(50 * k)),
                 (x + int(70 * k), y + int(20 * k)),
                 (x + int(40 * k), y + int(40 * k))], 0)
        polygon(screen, (0, 0, 0),
                [(x + int(40 * k), y - int(30 * k)), (x + int(70 * k), y - int(50 * k)),
                 (x + int(70 * k), y + int(20 * k)),
                 (x + int(40 * k), y + int(40 * k))], 1)
        polygon(screen, (255, 153, 0), [(x - int(30 * k), y - int(40 * k)), (x + int(10 * k), y - int(90 * k)),
                                        (x + int(40 * k), y - int(30 * k))], 0)
        polygon(screen, (0, 0, 0), [(x - int(30 * k), y - int(40 * k)), (x + int(10 * k), y - int(90 * k)),
                                    (x + int(40 * k), y - int(30 * k))], 1)
        polygon(screen, (255, 153, 0), [(x + int(10 * k), y - int(90 * k)), (x + int(40 * k), y - int(110 * k)),
                                        (x + int(70 * k), y - int(50 * k)), (x + int(40 * k), y - int(30 * k))], 0)
        polygon(screen, (0, 0, 0), [(x + int(10 * k), y - int(90 * k)), (x + int(40 * k), y - int(110 * k)),
                                    (x + int(70 * k), y - int(50 * k)), (x + int(40 * k), y - int(30 * k))], 1)
        circle(screen, (0, 0, 0), (x, y), int(20 * k), 0)

    if t == 0:
        ascreen.fill((255, 255, 255), rect=None, special_flags=0)
        x = 400 - x
        polygon(ascreen, (255, 204, 0),
                [(x - int(30 * k), y - int(40 * k)), (x + int(40 * k), y - int(30 * k)),
                 (x + int(40 * k), y + int(40 * k)),
                 (x - int(30 * k), y + int(30 * k))], 0)
        polygon(ascreen, (0, 0, 0),
                [(x - int(30 * k), y - int(40 * k)), (x + int(40 * k), y - int(30 * k)),
                 (x + int(40 * k), y + int(40 * k)),
                 (x - int(30 * k), y + int(30 * k))], 1)
        polygon(ascreen, (255, 204, 0),
                [(x + int(40 * k), y - int(30 * k)), (x + int(70 * k), y - int(50 * k)),
                 (x + int(70 * k), y + int(20 * k)),
                 (x + int(40 * k), y + int(40 * k))], 0)
        polygon(ascreen, (0, 0, 0),
                [(x + int(40 * k), y - int(30 * k)), (x + int(70 * k), y - int(50 * k)),
                 (x + int(70 * k), y + int(20 * k)),
                 (x + int(40 * k), y + int(40 * k))], 1)
        polygon(ascreen, (255, 153, 0), [(x - int(30 * k), y - int(40 * k)), (x + int(10 * k), y - int(90 * k)),
                                         (x + int(40 * k), y - int(30 * k))], 0)
        polygon(ascreen, (0, 0, 0), [(x - int(30 * k), y - int(40 * k)), (x + int(10 * k), y - int(90 * k)),
                                     (x + int(40 * k), y - int(30 * k))], 1)
        polygon(ascreen, (255, 153, 0), [(x + int(10 * k), y - int(90 * k)), (x + int(40 * k), y - int(110 * k)),
                                         (x + int(70 * k), y - int(50 * k)), (x + int(40 * k), y - int(30 * k))], 0)
        polygon(ascreen, (0, 0, 0), [(x + int(10 * k), y - int(90 * k)), (x + int(40 * k), y - int(110 * k)),
                                     (x + int(70 * k), y - int(50 * k)), (x + int(40 * k), y - int(30 * k))], 1)
        circle(ascreen, (0, 0, 0), (x, y), int(20 * k), 0)
        pygame.transform.flip(ascreen, True, False)

        ascreen.set_colorkey((255, 255, 255))

        screen.blit(pygame.transform.flip(ascreen, True, False), (0, 0))


##################################################################
def draw_zabor(x, y, k):
    '''
    Функция рисует забор с координатами x,y левого верхнего края забора
    k-определяет его размер
    '''

    for i in range(20):
        rect(screen, (255, 204, 102), (x + int(i * 20 * k), y, int(20 * k), int(240 * k)), 0)
        rect(screen, (0, 0, 0), (x + int(i * 20 * k), y, int(20 * k), int(240 * k)), 1)


##################################################################
def draw_sobaka(x, y, k, orientacia):
    '''
    Функия рисует собаку с координатами x,y соеденения ее передней лапки с телом
    k-определяет размер
    orientacia - если True то не поворачивает собаку,если False то поворачивает
    '''

    if orientacia == True:
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y - int(40 * k), int(120 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(100 * k), y - int(50 * k), int(60 * k), int(40 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(110 * k), y - int(30 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y - int(50 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(110 * k), y - int(10 * k), int(10 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y - int(30 * k), int(10 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(110 * k), y + int(30 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y + int(10 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(30 * k), y - int(30 * k), int(30 * k), int(60 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(10 * k), y - int(10 * k), int(30 * k), int(60 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y + int(20 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x, y + int(40 * k), int(30 * k), int(10 * k)), 0)
        rect(screen, (128, 128, 128), (x, y - int(60 * k), int(50 * k), int(50 * k)), 0)
        rect(screen, (0, 0, 0), (x, y - int(60 * k), int(50 * k), int(50 * k)), 1)
        ellipse(screen, (255, 0, 0), (x + int(20 * k), y - int(30 * k), int(10 * k), int(17 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(10 * k), y - int(50 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(10 * k), y - int(50 * k), int(30 * k), int(30 * k)), 1)
        rect(screen, (128, 128, 128), (x + int(10 * k), y - int(50 * k), int(30 * k), int(20 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y - int(60 * k), int(20 * k), int(20 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(40 * k), y - int(60 * k), int(20 * k), int(20 * k)), 1)
        ellipse(screen, (128, 128, 128), (x - int(10 * k), y - int(60 * k), int(20 * k), int(20 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(10 * k), y - int(60 * k), int(20 * k), int(20 * k)), 1)
        ellipse(screen, (255, 255, 255), (x + int(30 * k), y - int(50 * k), int(10 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(30 * k), y - int(50 * k), int(10 * k), int(6 * k)), 1)
        ellipse(screen, (255, 255, 255), (x + int(10 * k), y - int(50 * k), int(10 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(10 * k), y - int(50 * k), int(10 * k), int(6 * k)), 1)
        ellipse(screen, (0, 0, 0), (x + int(13 * k), y - int(50 * k), int(4 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x + int(33 * k), y - int(50 * k), int(4 * k), int(6 * k)), 0)

    elif orientacia == False:
        ellipse(screen, (128, 128, 128), (x - int(50 * k), y - int(40 * k), int(120 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y - int(50 * k), int(60 * k), int(40 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(80 * k), y - int(30 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y - int(50 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(100 * k), y - int(10 * k), int(10 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(60 * k), y - int(30 * k), int(10 * k), int(50 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(80 * k), y + int(30 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x + int(40 * k), y + int(10 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(60 * k), y - int(30 * k), int(30 * k), int(60 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(20 * k), y - int(10 * k), int(30 * k), int(60 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(70 * k), y + int(20 * k), int(30 * k), int(10 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(30 * k), y + int(40 * k), int(30 * k), int(10 * k)), 0)
        rect(screen, (128, 128, 128), (x - int(50 * k), y - int(60 * k), int(50 * k), int(50 * k)), 0)
        rect(screen, (0, 0, 0), (x - int(50 * k), y - int(60 * k), int(50 * k), int(50 * k)), 1)
        ellipse(screen, (255, 0, 0), (x - int(30 * k), y - int(30 * k), int(10 * k), int(17 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(40 * k), y - int(50 * k), int(30 * k), int(30 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(40 * k), y - int(50 * k), int(30 * k), int(30 * k)), 1)
        rect(screen, (128, 128, 128), (x - int(40 * k), y - int(50 * k), int(30 * k), int(20 * k)), 0)
        ellipse(screen, (128, 128, 128), (x - int(60 * k), y - int(60 * k), int(20 * k), int(20 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(60 * k), y - int(60 * k), int(20 * k), int(20 * k)), 1)
        ellipse(screen, (128, 128, 128), (x - int(10 * k), y - int(60 * k), int(20 * k), int(20 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(10 * k), y - int(60 * k), int(20 * k), int(20 * k)), 1)
        ellipse(screen, (255, 255, 255), (x - int(40 * k), y - int(50 * k), int(10 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(40 * k), y - int(50 * k), int(10 * k), int(6 * k)), 1)
        ellipse(screen, (255, 255, 255), (x - int(20 * k), y - int(50 * k), int(10 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(20 * k), y - int(50 * k), int(10 * k), int(6 * k)), 1)
        ellipse(screen, (0, 0, 0), (x - int(37 * k), y - int(50 * k), int(4 * k), int(6 * k)), 0)
        ellipse(screen, (0, 0, 0), (x - int(17 * k), y - int(50 * k), int(4 * k), int(6 * k)), 0)


##################################################################
rect(screen, (51, 255, 255), (0, 0, 400, 280), 0)  # Рисует небо

rect(screen, (102, 255, 51), (0, 280, 400, 280), 0)  # Рисует травку

draw_zabor(80, 8, 1.3)  # делаем забор

draw_zabor(0, 130, 0.8)  # делаем еще забор

draw_zabor(0, 220, 0.6)  # нам нужно больше заборов

draw_zabor(260, 180, 0.8)  # нам нуден забор

draw_sobaka(360, 340, 0.7, True)  # рисуем собаку ,тут важно учесть когда рисуеться собака ,
# если сделать ее после дома то она перкоет его собой

draw_dom(280, 390, 1.5, 1)  # Делаем дом собаки

draw_sobaka(70, 350, 1, False)  # 2 собаки

draw_sobaka(130, 500, 1, True)  # 3 собаки

draw_sobaka(380, 560, 3, False)  # 4 собаки...
##################################################################

pygame.display.update()  # Это обновит дисплей после рисования
clock = pygame.time.Clock()  # Дальше делаеться для того чтобы экран не обновлялся слишком часто и
finished = False  # бесполезно не нагружал пк
while not finished:  # Остальное отвечает за закрытие программы
    clock.tick(FPS)  #
    for event in pygame.event.get():  #
        if event.type == pygame.QUIT:  #
            finished = True  #
pygame.quit()  #
