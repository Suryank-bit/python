import pygame
pygame.init()
res = (800, 600)
screen = pygame.display.set_mode(res)
gray = (200, 200, 200)
# credits
bigfont2 = pygame.font.SysFont('8-BIT WONDER.TTF', 30)
bigfont3 = pygame.font.SysFont('8-BIT WONDER.TTF', 50)
n1 = bigfont2.render('IN THIS GAME TO SCORE POINTS ', True, gray)
n2 = bigfont2.render('YOU HAVE TO MAKE THE BALL STRIKE THE OPPOSITE THE SIDE OF ', True, gray)
n3 = bigfont2.render('AND THE OTHER PLAYER HAVE TO SAVE THE BALL FROM STRIKING THE SIDE ', True, gray)
n4 = bigfont2.render('IF YOU SUCCEED IN STRIKING THE OPPOSITE SIDE YOU SCORE A POINT ', True, gray)
n5 = bigfont2.render('THE GAMES GOES ON FOR 60 SECONDS ', True, gray)
n6 = bigfont2.render('NOW THE CONTROLLES THE BLUE PADDLE ', True, gray)
n7 = bigfont2.render('MOVES UP AND DOWN USING W-KEY AND S-KEY, RESPECTIVELY ', True, gray)
n8 = bigfont2.render('THE RED PADDLE MOVES WITH THE ARROW KEYS ',True,gray)
n9 = bigfont2.render('UP-KEY TO ASCEND AND DOWN KEY TO DESCEND.', True, gray)
n10 = bigfont3.render('HAVE FUN PLAYING!!!' , True, gray)
pygame.display.set_caption("PING PONG")
icon = pygame.image.load("ping-pong.png")
r = 1
while r == 1:
    screen.blit(n1, (190, 10))
    screen.blit(n2, (50, 50))
    screen.blit(n3, (20, 100))
    screen.blit(n4, (30, 150))
    screen.blit(n5, (150, 200))
    screen.blit(n6, (140, 250))
    screen.blit(n7, (60, 300))
    screen.blit(n8, (100, 350))
    screen.blit(n9, (100, 400))
    screen.blit(n10,(190, 450))

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
           r = 0