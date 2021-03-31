import random

# initializing the constructor
import pygame as pygame

pygame.init()

# screen resolution
res = (800, 600)

# opens up a window
screen = pygame.display.set_mode(res)

# white color
color = (255, 255, 255)

# light shade of the button
color_light = (247, 220, 111)

# dark shade of the button
color_dark = (100, 100, 100)

# stores the width of the
# screen into a variable
width = screen.get_width()

# stores the height of the
# screen into a variable
#
# # rendering a text written in
# # this font
height = screen.get_height()

# defining a font
smallfont = pygame.font.SysFont('8-BIT WONDER.TTF', 35)
smallfont1 = pygame.font.SysFont('8-BIT WONDER.TTF', 30)
bigfont = pygame.font.SysFont('8-BIT WONDER.TTF', 100)
play = smallfont.render('PLAY', True, color)
htp = smallfont1.render('HOW TO PLAY', True, color)
cre = smallfont.render('CREDITS', True, color)
quit = smallfont.render('QUIT', True, color)
title = bigfont.render('PING - PONG', True, color)

# fills the screen with a color
screen.fill((0, 0, 0))

# stores the (x,y) coordinates into
# the variable as a tuple
mouse = pygame.mouse.get_pos()

# if mouse is hovered on a button it
# changes to lighter shade

# superimposing the text onto our button
screen.blit(play, (width / 2 - 35, height / 2 - 35))
screen.blit(htp, (width / 2 - 70, height / 2 + 15))
screen.blit(cre, (width / 2 - 55, height / 2 + 55))
screen.blit(quit, (width / 2 - 30, height / 2 + 95))
screen.blit(title, (200, 100))

# updates the frames of the game
pygame.display.update()

clock = pygame.time.Clock()
start = 6000
begin = 500

print("hello")
# bkg-screen
screen = pygame.display.set_mode((800, 600))
bg_color = (168, 156, 156)

# title &icon
pygame.display.set_caption("PING PONG")
icon = pygame.image.load("ping-pong.png")
pygame.display.set_icon(icon)

gray = (200, 200, 200)
red = (146, 43, 33)
blue = (31, 97, 141)
# paddle_A
player1 = pygame.Rect(780, 230, 10, 140)

player1_speed = 0

# paddle_B
player2 = pygame.Rect(10, 230, 10, 140)
player2_speed = 0
# score
player1_score = 0
player2_score = 0
score_card = pygame.font.Font("8-BIT WONDER.TTF", 34)
player1v = "PLAYER 1 WINS!!!!"
player2v = "PLAYER 2 WINS!!!!"
# time
tick = pygame.font.Font("8-BIT WONDER.TTF", 34)

# ball
ball = pygame.Rect(385, 285, 30, 30)
ball_speed_x: int = 7 * random.choice((-1, 1))
ball_speed_y: int = 7 * random.choice((-1, 1))

# sound
pong = pygame.mixer.Sound("Ping_Pong.wav")
point = pygame.mixer.Sound("coin.wav")


def ball_col():
    global ball_speed_x
    global ball_speed_y
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= 600:
        pygame.mixer.Sound.play(pong)
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= 800:
        pygame.mixer.Sound.play(pong)
        ball_speed_x *= -1

    if ball.colliderect(player1) or ball.colliderect(player2):
        pygame.mixer.Sound.play(pong)
        ball_speed_x *= -1
        ball_speed_y *= -1


def player_move():
    player1.y += player1_speed
    player2.y += player2_speed
    if player1.top <= 0:
        player1.top = 0
    if player1.bottom >= 600:
        player1.bottom = 600
    if player2.top <= 0:
        player2.top = 0
    if player2.bottom >= 600:
        player2.bottom = 600


def score():
    global player1_score
    global player2_score
    if ball.left <= 0:
        pygame.mixer.Sound.play(point)
        player2_score += 1
        stime = pygame.time.get_ticks()
    if ball.right >= 800:
        pygame.mixer.Sound.play(point)
        player1_score += 1
        stime = pygame.time.get_ticks()


# menu

while True:

    for ev in pygame.event.get():

        if ev.type == pygame.QUIT:
            pygame.quit()
            # checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # if the mouse is clicked on the
            # button the game is terminated

            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 45 <= mouse[1] <= height / 2:
                pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 2 - 45, 140, 40])
                running = True
            else:
                pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 - 45, 140, 40])
                # if the mouse is clicked on the
                # button the game is terminated
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 <= mouse[1] <= height / 2 + 45:
                pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 2, 140, 40])

            else:
                pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 2, 140, 40])
                # if the mouse is clicked on the
                # button the game is terminated
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 45 <= mouse[1] <= height / 2 + 90:
                pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 2 + 45, 140, 40])

            else:
                pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 45, 140, 40])
                # if the mouse is clicked on the
                # button the game is terminated
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 90 <= mouse[1] <= height / 2 + 135:
                pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 2 + 90, 140, 40])
                pygame.quit()
            else:
                pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 90, 140, 40])

stime = None
pygame.time.delay(2000)
while running:

    screen.fill(bg_color)  # screen color(R, G, B)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player1_speed += 7
            if event.key == pygame.K_UP:
                player1_speed -= 7
            if event.key == pygame.K_w:
                player2_speed -= 7
            if event.key == pygame.K_s:
                player2_speed += 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player1_speed -= 7
            if event.key == pygame.K_UP:
                player1_speed += 7
            if event.key == pygame.K_w:
                player2_speed += 7
            if event.key == pygame.K_s:
                player2_speed -= 7

    pygame.draw.rect(screen, red, player1)
    ball_col()
    player_move()
    score()

    pygame.draw.rect(screen, blue, player2)
    pygame.draw.ellipse(screen, gray, ball)
    pygame.draw.aaline(screen, gray, (400, 0), (400, 600))
    player1_text = score_card.render(f"{player1_score}", False, gray)
    screen.blit(player1_text, (350, 300))
    player2_text = score_card.render(f"{player2_score}", False, gray)
    screen.blit(player2_text, (430, 300))
    time_text = tick.render(f"{int(start / 100)}", False, gray)
    screen.blit(time_text, (400, 0))
    start -= 1
    if start <= 0:
        running = False

    pygame.display.update()
    clock.tick(70)