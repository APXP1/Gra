import pygame
import random

pygame.init()
win = pygame.display.set_mode((1280, 720))
x = 550
y = 550

px = random.choice([0, 426])
py = 0
px1 = random.choice([426, 853])
py1 = 0
px2 = random.choice([853, 1280])
py2 = 0
# poniżej przedstawiono zmnienne, które odpowiadają za położenie asteroid
p = 0
pp = 200

p1 = 200
pp1 = -200

p2 = 400
pp2= -200

p3 = 600
pp3 = -200

p4 = 800
pp4 = -200

p5 = 1000
pp5 = -200

szer = 0
wys = 0
asteroida = pygame.image.load('asteroida.png')
postac = pygame.image.load("postać.png")
tlo = pygame.image.load('tło.webp')
predkosc = 10
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Ruszanie postyacią
    pygame.time.delay(25)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= predkosc
    if keys[pygame.K_d]:
        x += predkosc
    if keys[pygame.K_LEFT]:
        x -= predkosc
    if keys[pygame.K_RIGHT]:
        x += predkosc
    #zapętlony wyświetlany pixel przemieszczający się w dół
    while py == 700:
        #ustawienie nowego położenia y
        py = 0
        py1=0
        py2=0
        #losowanie położenia x
        px = random.choice([0, 550])
    #zmenianie poziomu y różnych rzeczy (py to pixele, pp asteroidy)
    py += 4
    py1 += 8
    py2 += 16

    pp += 6
    pp1 += 9
    pp2 += 5
    pp3 += 7
    pp4 += 10
    pp5 += 5
    #resetowanie położenia y asteroidy
    while pp>720:
        pp =-200
    while pp1>720:
        pp1=-200
    while pp2>720:
        pp2=-200
    while pp3>720:
        pp3=-200
    while pp4>720:
        pp4=-200
    #koniec gry (w przypadku kolizji)
    while (p+130>x and p+130<x+140 and pp+102==y) or (p+30>x and p+30<x+140 and pp+102==y) or (p+210>x and p+210<x+140 and pp+102==y):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Game Over ', 1, (255, 255, 255))
        win.blit(label, (100, 425))
        pygame.display.update()
    while (p1+130>x and p1+130<x+140 and pp1+102==y) or (p1+30>x and p1+30<x+140 and pp1+102==y) or (p1+210>x and p1+210<x+140 and pp1+102==y):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Game Over ', 1, (255, 255, 255))
        win.blit(label, (300, 425))
        pygame.display.update()
    while (p2+130>x and p2+130<x+140 and pp2+100==y) or (p2+30>x and p2+30<x+140 and pp2+100==y) or (p2+210>x and p2+210<x+140 and pp2+100==y):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Game Over ', 1, (255, 255, 255))
        win.blit(label, (500, 425))
        pygame.display.update()
    while (p3+130>x and p3+130<x+140 and pp3+141==y) or (p3+30>x and p3+30<x+140 and pp3+141==y) or (p3+210>x and p3+210<x+140 and pp3+141==y):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Game Over ', 1, (255, 255, 255))
        win.blit(label, (700, 425))
        pygame.display.update()
    while (p4+130>x and p4+130<x+140 and pp4+120==y) or (p4+30>x and p4+30<x+140 and pp4+120==y) or (p4+210>x and p4+210<x+140 and pp4+120==y):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Game Over ', 1, (255, 255, 255))
        win.blit(label, (900, 425))
        pygame.display.update()
    while (p5+130>x and p5+130<x+140 and pp5+110==y) or (p5+30>x and p5+30<x+140 and pp5+110==y) or (p5+210>x and p5+210<x+140 and pp5+110==y):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Game Over ', 1, (255, 255, 255))
        win.blit(label, (1100, 425))
        pygame.display.update()
    #bariera
    while x<0:
        x=0
    while x>1150:
        x=1150


    #wyświetlanie
    win.blit(tlo, (0, 0))
    win.blit(postac, (x, y))
    win.blit(asteroida, (p,pp))
    win.blit(asteroida,(p1,pp1))
    win.blit(asteroida, (p2, pp2))
    win.blit(asteroida, (p3, pp3))
    win.blit(asteroida, (p4, pp4))
    win.blit(asteroida, (p5, pp5))
    pygame.draw.rect(win, (255, 255, 255), (px, py, 5, 15))
    pygame.draw.rect(win, (255, 255, 255), (px1, py1, 5, 15))
    pygame.draw.rect(win, (255, 255, 255), (px2, py2, 5, 15))
    pygame.display.update()
