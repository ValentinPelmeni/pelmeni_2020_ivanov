import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
color = (255, 244, 38)
screen.fill(pygame.Color('grey'),pygame.Rect(0, 0, 800, 800))
pygame.draw.circle(screen,(0,0,0), (400, 400), 205)
pygame.draw.circle(screen,color, (400, 400), 200)
pygame.Rect(0, 0, 800, 800)
def krug(x):
    pygame.draw.circle(screen, (0,0,0),x , 22)
    pygame.draw.circle(screen, (255, 0, 0),x , 20)
    pygame.draw.circle(screen, (0,0,0),x , 10)
krug((325,325))
krug((475,325))
def brov(x,y):
    pygame.draw.line(screen,(0,0,0), x, y, 10)
brov((420,300),(500,250))
brov((380,300),(300,250))
brov((300,450),(500,450))
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
