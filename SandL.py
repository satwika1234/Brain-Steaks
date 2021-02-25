# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 21:02:11 2020

@author: Hisana
"""
import pygame
from random import randint
from pygame import mixer

pygame.init()
GD = pygame.display.set_mode((1000, 700))
w = 1000
h = 700

pygame.display.set_caption("S & L BY BRAIN STEAKS")

# change color if u want
headcolor = (255, 0, 50)
black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
b_red = (240, 0, 0)
bg = pygame.image.load("blackbg.jpg")
GD.blit(bg, (0, 0))
board = pygame.image.load("SandL_Items/Images/Snakes-and-Ladders-Bigger.jpg")
GD.blit(board, (w / 2 - 250, h / 2 - 250))
dice1 = pygame.image.load("SandL_Items/Images/dice1.png")
dice2 = pygame.image.load("SandL_Items/Images/dice2.gif")
dice3 = pygame.image.load("SandL_Items/Images/dice3.gif")
dice4 = pygame.image.load("SandL_Items/Images/dice4.gif")
dice5 = pygame.image.load("SandL_Items/Images/dice5.gif")
dice6 = pygame.image.load("SandL_Items/Images/dice6.gif")
redgoti = pygame.image.load("SandL_Items/Images/redgoti.png")

yellowgoti = pygame.image.load("SandL_Items/Images/yellowgoti.png")

greengoti = pygame.image.load("SandL_Items/Images/greengoti.png")
green = (0, 200, 0)
b_green = (0, 230, 0)


def button1(text, xmouse, ymouse, x, y, w, h, i, a, fs):
    # mouse pos

    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            return True

    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


def message_display(text, x, y, fs):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    GD.blit(TextSurf, TextRect)


def text_objects(text, font):
    textSurface = font.render(text, True, (255, 255, 255))
    return textSurface, textSurface.get_rect()


def message_display1(text, x, y, fs, c):
    largeText = pygame.font.Font('freesansbold.ttf', fs)
    TextSurf, TextRect = text_objects1(text, largeText)
    TextRect.center = (x, y)
    GD.blit(TextSurf, TextRect)


def text_objects1(text, font):
    textSurface = font.render(text, True, white)
    return textSurface, textSurface.get_rect()


def button(text, xmouse, ymouse, x, y, w, h, i, a, fs, b):
    if x + w > xmouse > x and y + h > ymouse > y:
        pygame.draw.rect(GD, a, [x - 2.5, y - 2.5, w + 5, h + 5])
        if pygame.mouse.get_pressed() == (1, 0, 0):
            if b == 1:
                options()
            elif b == 5:
                import frontpage
                frontpage.mainpage()
            elif b == 0:
                Quit()
            elif b == 21:
                but = mixer.Sound("SandL_Items/Sound/SandL_button.wav")
                but.play()
                play(21)
            elif b == 13:
                but = mixer.Sound("SandL_Items/Sound/SandL_button.wav")
                but.play()
                play(2)
            elif b == "s" or b == 2:
                but = mixer.Sound("SandL_Items/Sound/SandL_button.wav")
                but.play()
                return b
            elif b == 7:
                options()
            else:
                return True






    else:
        pygame.draw.rect(GD, i, [x, y, w, h])
    message_display(text, (x + w + x) / 2, (y + h + y) / 2, fs)


def dice(a):
    if a == 1:
        a = dice1
    elif a == 2:
        a = dice2
    elif a == 3:
        a = dice3
    elif a == 4:
        a = dice4
    elif a == 5:
        a = dice5
    elif a == 6:
        a = dice6

    time = pygame.time.get_ticks()
    while pygame.time.get_ticks() - time < 500:
        GD.blit(a, (800, 450))
        pygame.display.update()


def goti(a):
    l1 = [[195, 550], [250, 550], [300, 550], [350, 550], [400, 550], [450, 550], [500, 550], [550, 550], [600, 550],
          [650, 550], [700, 550],
          [700, 500], [650, 500], [600, 500], [550, 500], [500, 500], [450, 500], [400, 500], [350, 500], [300, 500],
          [250, 500],
          [250, 450], [300, 450], [350, 450], [400, 450], [450, 450], [500, 450], [550, 450], [600, 450], [650, 450],
          [700, 450],
          [700, 400], [650, 400], [600, 400], [550, 400], [500, 400], [450, 400], [400, 400], [350, 400], [300, 400],
          [250, 400],
          [250, 350], [300, 350], [350, 350], [400, 350], [450, 350], [500, 350], [550, 350], [600, 350], [650, 350],
          [700, 350],
          [700, 300], [650, 300], [600, 300], [550, 300], [500, 300], [450, 300], [400, 300], [350, 300], [300, 300],
          [250, 300],
          [250, 250], [300, 250], [350, 250], [400, 250], [450, 250], [500, 250], [550, 250], [600, 250], [650, 250],
          [700, 250],
          [700, 200], [650, 200], [600, 200], [550, 200], [500, 200], [450, 200], [400, 200], [350, 200], [300, 200],
          [250, 200],
          [250, 150], [300, 150], [350, 150], [400, 150], [450, 150], [500, 150], [550, 150], [600, 150], [650, 150],
          [700, 150],
          [700, 100], [650, 100], [600, 100], [550, 100], [500, 100], [450, 100], [400, 100], [350, 100], [300, 100],
          [250, 100]]
    l2 = l1[a]
    x = l2[0]
    y = l2[1]
    return x, y


def ladders(x):
    if x == 1:
        return 38
    elif x == 4:
        return 14
    elif x == 9:
        return 31
    elif x == 28:
        return 84
    elif x == 21:
        return 42
    elif x == 51:
        return 67
    elif x == 80:
        return 99
    elif x == 72:
        return 91
    else:
        return x


def snakes(x):
    if x == 17:
        return 7
    elif x == 54:
        return 34
    elif x == 62:
        return 19
    elif x == 64:
        return 60
    elif x == 87:
        return 36
    elif x == 93:
        return 73
    elif x == 95:
        return 75
    elif x == 98:
        return 79
    else:
        return x


def Quit():
    pygame.quit()


def turn(score, six):
    a = randint(1, 6)  # player dice roll
    if a == 6:
        six = True
    else:
        six = False
    dice(a)
    score += a
    if score <= 100:
        lad = ladders(score)  # use snk and lad if you wanna use sound
        score = lad
        snk = snakes(score)
        score = snk
    else:  # checks if player score is not grater than 100
        score -= a
        time = pygame.time.get_ticks()
        while pygame.time.get_ticks() - time < 1500:
            message_display1("Can't move!", w / 2, 50, 35, white)
            pygame.display.update()

    return score, six


def options():
    flag = True
    while flag == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()

        # mouse pos
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        b1 = b2 = b3 = b4 = b5 = -1
        GD.blit(bg, (0, 0))
        # Single player button
        b1 = button("Single Player", mouse[0], mouse[1], (w / 2 - 150), 250, 300, 50, (0, 17, 240), (0, 13, 210), 30,
                    "s")
        # 2 player button
        b2 = button("2 Players", mouse[0], mouse[1], (w / 2) - 150, 350, 300, 50, (0, 17, 240), (0, 13, 210), 30, 2)

        # Back button
        b5 = button("Back", mouse[0], mouse[1], 0, 0, 200, 50, (0, 17, 240), b_red, 30, 5)
        if b5 == 5:
            but = mixer.Sound(".SandL_Items/Sound/SandL_button.wav")
            but.play()

        if b1 == "s":
            but = mixer.Sound("SandL_Items/Sound/SandL_button.wav")
            but.play()
            play(21)
        if b2 == 2:
            but = mixer.Sound("SandL_Items/Sound/SandL_button.wav")
            but.play()
            play(2)

        pygame.display.update()


def play(b):
    mixer.music.load('SandL_Items/Sound/SandL_background.mp3')
    mixer.music.play(-1)
    p1score = 0

    p2score = 0
    time = 3000
    t = 1
    p1score = 0
    p2score = 0
    xcr = xcy = 195
    ycr = ycy = 550
    GD.blit(bg, (0, 0))
    GD.blit(board, (w / 2 - 250, h / 2 - 250))
    GD.blit(redgoti, (195, 550))

    while True:
        GD.blit(bg, (0, 0))
        GD.blit(board, (w / 2 - 250, h / 2 - 250))
        mouse = pygame.mouse.get_pos()
        t = 1
        s = False
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                Quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    Quit()
        if (b == 21):
            if (button1("Player ", mouse[0], mouse[1], 90, 400, 100, 30, red, (50, 50, 50), 20)):
                if t == 1:
                    but = mixer.Sound("SandL_Items/Sound/SandL_button.wav")
                    but.play()

                    p1score, s = turn(p1score, s)
                    if not s:
                        t = 2
                    xcr, ycr = goti(p1score)

                    pygame.display.update()
                    if p1score == 100:
                        mixer.music.stop()
                        but = mixer.Sound("SandL_Items/Sound/SandL_winning.wav")
                        but.play(0)
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            message_display1("Player wins", w / 2, 50, 35, white)

                            pygame.display.update()
                        break

            GD.blit(redgoti, (xcr, ycr))
            pygame.time.wait(80)

            button("Reset", mouse[0], mouse[1], 900, 0, 100, 50, (0, 17, 240), (50, 50, 50), 19, 21)

            mouse = pygame.mouse.get_pos()
            (button1("Computer", mouse[0], mouse[1], 90, 450, 100, 30, (225, 155, 10), (50, 50, 50), 19))
            if True:
                if t == 2:

                    p2score, s = turn(p2score, s)
                    if not s:
                        t = 1
                    xcy, ycy = goti(p2score)

                    pygame.display.update()
                    if p2score == 100:
                        but = mixer.Sound("SandL_Items/Sound/SandL_winning.wav")
                        but.play(0)
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            message_display1("Computer wins", w / 2, 50, 35, white)

                            pygame.display.update()
                        break

                GD.blit(yellowgoti, (xcy, ycy))

        else:
            if (button1("Player 1", mouse[0], mouse[1], 90, 400, 100, 30, red, (50, 50, 50), 20)):
                if t == 1:
                    but = mixer.Sound("SandL_Items/Sound/SandL_button.wav")
                    but.play()
                    p1score, s = turn(p1score, s)
                    if not s:
                        t = 2
                    xcr, ycr = goti(p1score)

                    pygame.display.update()
                    if p1score == 100:
                        but = mixer.Sound("SandL_Items/Sound/SandL_winning.wav")
                        but.play(0)
                        time = pygame.time.get_ticks()
                        while pygame.time.get_ticks() - time < 2000:
                            message_display1("Player 1 wins", w / 2, 50, 35, white)

                            pygame.display.update()
                        break

            GD.blit(redgoti, (xcr, ycr))
            pygame.time.wait(80)

            mouse = pygame.mouse.get_pos()
            if (button1("Player 2", mouse[0], mouse[1], 90, 450, 100, 30, (255, 155, 10), (50, 50, 50), 19)):

                p2score, s = turn(p2score, s)
                but = mixer.Sound("SandL_Items/Sound/SandL_button.wav")
                but.play()
                if not s:
                    t = 1
                xcy, ycy = goti(p2score)

                pygame.display.update()
                if p2score == 100:
                    but = mixer.Sound("SandL_Items/Sound/SandL_winning.wav")
                    but.play(0)
                    time = pygame.time.get_ticks()
                    while pygame.time.get_ticks() - time < 2000:
                        message_display1("Player 2 wins", w / 2, 50, 35, white)

                        pygame.display.update()
                    break

            GD.blit(yellowgoti, (xcy, ycy))
            button("Reset", mouse[0], mouse[1], 900, 0, 100, 50, (0, 17, 240), (50, 50, 50), 19, 13)

        button("Back", mouse[0], mouse[1], 0, 0, 100, 50, red, b_red, 19, 7)

        pygame.display.update()


options()

# call this function for snake game to start
