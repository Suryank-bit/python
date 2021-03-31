
import pingpong1
import os

# initializing the constructor
pingpong1.pygame.init()

# screen resolution
res = (800, 600)

# opens up a window
screen = pingpong1.pygame.display.set_mode(res)

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
smallfont = pingpong1.pygame.font.SysFont('8-BIT WONDER.TTF', 35)
smallfont1 = pingpong1.pygame.font.SysFont('8-BIT WONDER.TTF', 30)
bigfont = pingpong1.pygame.font.SysFont('8-BIT WONDER.TTF', 100)
play = smallfont.render('PLAY', True, color)
htp = smallfont1.render('HOW TO PLAY', True, color)
cre = smallfont.render('CREDITS', True, color)
quit = smallfont.render('QUIT', True, color)
title = bigfont.render('PING - PONG', True, color)

while True:
    for ev in pingpong1.pygame.event.get():
        if ev.type == pingpong1.pygame.QUIT:
            pingpong1.pygame.quit()
            # checks if a mouse is clicked
        if ev.type == pingpong1.pygame.MOUSEBUTTONDOWN:
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 45 <= mouse[1] <= height / 2:
                os.system('pingpong1.py')
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 <= mouse[1] <= height / 2 + 45:
                os.system('HTP.py')
            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 45 <= mouse[1] <= height / 2 + 90:
                os.system('credits.py')

            if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 90 <= mouse[1] <= height / 2 + 135:
                pingpong1.pygame.quit()

    # stores the (x,y) coordinates into
    # the variable as a tuple
    mouse = pingpong1.pygame.mouse.get_pos()

    # if mouse is hovered on a button it
    # changes to lighter shade
    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 - 45 <= mouse[1] <= height / 2:
        pingpong1.pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 2 - 45, 140, 40])

    else:
        pingpong1.pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 - 45, 140, 40])

    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 <= mouse[1] <= height / 2 + 45:
        pingpong1.pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 2, 140, 40])

    else:
        pingpong1.pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 2, 140, 40])

    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 45 <= mouse[1] <= height / 2 + 90:
        pingpong1.pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 2 + 45, 140, 40])

    else:
        pingpong1.pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 45, 140, 40])

    if width / 2 - 70 <= mouse[0] <= width / 2 + 70 and height / 2 + 90 <= mouse[1] <= height / 2 + 135:
        pingpong1.pygame.draw.rect(screen, color_light, [width / 2 - 70, height / 2 + 90, 140, 40])

    else:
        pingpong1.pygame.draw.rect(screen, color_dark, [width / 2 - 70, height / 2 + 90, 140, 40])

        # superimposing the text onto our button
    screen.blit(play, (width / 2 - 35, height / 2 - 35))
    screen.blit(htp, (width / 2 - 70, height / 2 + 15))
    screen.blit(cre, (width / 2 - 55, height / 2 + 55))
    screen.blit(quit, (width / 2 - 30, height / 2 + 95))
    screen.blit(title, (200, 100))

    # updates the frames of the game
    pingpong1.pygame.display.update()
