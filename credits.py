import pygame
pygame.init()
res = (800, 600)
screen = pygame.display.set_mode(res)
gray = (200, 200, 200)
# credits
bigfont = pygame.font.SysFont('8-BIT WONDER.TTF', 70)
name1 = bigfont.render('name 1', True, gray)
name2 = bigfont.render('name 2', True, gray)
name3 = bigfont.render('name 3', True, gray)
pygame.display.set_caption("PING PONG")
icon = pygame.image.load("ping-pong.png")
r = 1
while r == 1:
    screen.blit(name1, (200, 100))
    screen.blit(name2, (200, 150))
    screen.blit(name3, (200, 200))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
           r = 0
