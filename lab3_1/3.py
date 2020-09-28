import pygame

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 700))
color = (255, 244, 38)
screen.fill(pygame.Color('grey'),pygame.Rect(0, 0, 1200, 700))
def car(x,y,r):
    pygame.draw.ellipse(screen, (0, 0, 0), (x - 20 * r, y + 30 * r, r * 30, r * 10))
    pygame.draw.rect(screen, (100, 255, 255), (x, y, 150*r,50*r))
    pygame.draw.rect(screen, (100, 255, 255), (x+50*r, y-20*r, 75*r, 50 * r))
    pygame.draw.rect(screen, (255, 255, 255), (x + 60 * r, y - 15 * r, 30 * r, 15 * r))
    pygame.draw.rect(screen, (255, 255, 255), (x + 100 * r, y - 15 * r, 20 * r, 15 * r))
    pygame.draw.ellipse(screen, (0, 0, 0), (x+ 20 * r, y + 40 * r, r * 30, r * 30))
    pygame.draw.ellipse(screen, (0, 0, 0), (x + 100 * r, y + 40 * r, r * 30, r * 30))


pygame.draw.rect(screen, (100, 110, 100), (0, 500, 1200, 200))
pygame.draw.ellipse(screen, (150, 150, 150), (400, 500, 2000, 600))
pygame.draw.rect(screen, (150, 70, 0), (20, 50, 100, 500))
pygame.draw.rect(screen, (0, 150, 90), (300, 70, 120, 480))
pygame.draw.rect(screen, (150, 90, 0), (800, 50, 100, 450))
pygame.draw.rect(screen, (90, 70, 39), (1000, 50, 80, 520))
pygame.draw.rect(screen, (190, 70, 39), (400, 50, 150, 550))
pygame.draw.rect(screen, (190, 160, 190), (600, 50, 150, 460))

car(100,600,1.5)
car(400,650,1)
car(600,600,1)
car(900,600,1.5)

pygame.draw.ellipse(screen,(200,200,200), (10, 500, 100, 80))
pygame.draw.ellipse(screen,(200,200,200), (30, 300, 120, 90))
pygame.draw.ellipse(screen,(200,200,200), (350, 500, 80, 50))
pygame.draw.ellipse(screen,(200,200,200), (400, 300, 120, 90))
pygame.draw.ellipse(screen,(200,200,200), (550, 500, 90, 80))
pygame.draw.ellipse(screen,(200,200,200), (700, 300, 120, 90))
pygame.draw.ellipse(screen,(200,200,200), (800, 500, 90, 80))
pygame.draw.ellipse(screen,(200,200,200), (900, 300, 120, 90))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()
