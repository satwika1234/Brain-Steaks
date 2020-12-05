import pygame
import sys
import random
from pygame import mixer

pygame.init()
pygame.font.init()


def sudoku_hard():
    mixer.music.load('sudoku_background.mp3')
    mixer.music.play(-1)
    pygame.init()
    pygame.font.init()
    mydishard = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("SUDOKU HARD BY BRAIN STEAKS")
    imghard = pygame.image.load('sudoku.png')
    pygame.display.set_icon(imghard)

    def create_fonthard(t, s=25, c=(255, 255, 0), b=False, i=False):
        font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
        text = font.render(t, True, c)
        return text

    fotnhard = pygame.font.SysFont("comicsans", 40)
    fontxhard = pygame.font.SysFont("comicsans", 70)

    def bghard():
        bg = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydishard.blit(bg, (0, 0))
        bg1 = pygame.image.load('sudoku.png')
        bg1 = pygame.transform.scale(bg1, (1000, 700))
        mydishard.blit(bg1, (0, 0))
        pygame.draw.rect(mydishard, (0, 0, 255), (810, 315, 150, 35))
        pygame.draw.rect(mydishard, (0, 0, 255), (810, 370, 150, 35))
        pygame.draw.rect(mydishard, (0, 0, 255), (810, 425, 150, 35))
        text3 = create_fonthard("ANS FOR U")
        mydishard.blit(text3, (820, 320))
        text4 = create_fonthard("     RESET   ")
        mydishard.blit(text4, (820, 375))
        text6 = create_fonthard("CHANCES LEFT :")
        mydishard.blit(text6, (660, 40))
        text7 = create_fonthard("       EXIT   ")
        mydishard.blit(text7, (820, 430))
        # text5 = create_font("     UNDO   ")
        # mydishard.blit(text5, (820, 430))

    runhard = True
    global flag1hard
    global flaghard
    global chanceshard
    flag1hard = 0
    buttonhard = 1
    valhard = 0
    global xhard
    global yhard
    difhard = 60
    gridhardq1 = [
        [0, 0, 7, 1, 0, 0, 0, 5, 0],
        [0, 6, 0, 0, 0, 0, 0, 7, 0],
        [0, 0, 0, 7, 0, 0, 3, 0, 4],
        [3, 0, 0, 4, 0, 0, 5, 2, 0],
        [0, 2, 0, 8, 0, 5, 0, 4, 0],
        [0, 8, 4, 0, 0, 3, 0, 0, 6],
        [1, 0, 5, 0, 0, 2, 0, 0, 0],
        [0, 7, 0, 0, 0, 0, 0, 6, 0],
        [0, 4, 0, 0, 0, 9, 1, 0, 0]

    ]
    gridhardq2 = [
        [9, 0, 0, 0, 0, 8, 0, 0, 0],
        [0, 2, 7, 0, 6, 0, 0, 0, 0],
        [0, 0, 6, 1, 0, 0, 0, 0, 0],
        [0, 0, 3, 0, 0, 0, 0, 0, 7],
        [0, 1, 0, 9, 0, 0, 0, 3, 0],
        [2, 0, 0, 0, 8, 0, 0, 0, 0],
        [0, 6, 0, 0, 9, 0, 0, 0, 0],
        [0, 0, 1, 7, 0, 0, 0, 4, 0],
        [8, 4, 0, 0, 2, 0, 0, 0, 6]
    ]
    gridhardq3 = [
        [0, 9, 0, 0, 0, 6, 0, 4, 0],
        [0, 0, 5, 3, 0, 0, 0, 0, 8],
        [0, 0, 0, 0, 7, 0, 2, 0, 0],
        [0, 0, 1, 0, 5, 0, 0, 0, 3],
        [0, 6, 0, 0, 0, 9, 0, 7, 0],
        [2, 0, 0, 0, 8, 4, 1, 0, 0],
        [0, 0, 3, 0, 1, 0, 0, 0, 0],
        [8, 0, 0, 0, 0, 2, 5, 0, 0],
        [0, 5, 0, 4, 0, 0, 0, 8, 0]
    ]

    gridharda1 = [
        [4, 9, 7, 1, 3, 8, 6, 5, 2],
        [2, 6, 3, 9, 5, 4, 8, 7, 1],
        [8, 5, 1, 7, 2, 6, 3, 9, 4],
        [3, 1, 9, 4, 6, 7, 5, 2, 8],
        [7, 2, 6, 8, 1, 5, 9, 4, 3],
        [5, 8, 4, 2, 9, 3, 7, 1, 6],
        [1, 3, 5, 6, 7, 2, 4, 8, 9],
        [9, 7, 8, 3, 4, 1, 2, 6, 5],
        [6, 4, 2, 5, 8, 9, 1, 3, 7]
    ]
    gridharda2 = [
        [9, 3, 4, 2, 7, 8, 6, 1, 5],
        [1, 2, 7, 4, 6, 5, 3, 8, 9],
        [5, 8, 6, 1, 3, 9, 7, 2, 4],
        [4, 5, 3, 6, 1, 2, 8, 9, 7],
        [6, 1, 8, 9, 4, 7, 5, 3, 2],
        [2, 7, 9, 5, 8, 3, 4, 6, 1],
        [7, 6, 2, 8, 9, 4, 1, 5, 3],
        [3, 9, 1, 7, 5, 6, 2, 4, 8],
        [8, 4, 5, 3, 2, 1, 9, 7, 6]
    ]
    gridharda3 = [
        [1, 9, 8, 5, 2, 6, 3, 4, 7],
        [7, 2, 5, 3, 4, 1, 6, 9, 8],
        [3, 4, 6, 9, 7, 8, 2, 1, 5],
        [9, 8, 1, 2, 5, 7, 4, 6, 3],
        [5, 6, 4, 1, 3, 9, 8, 7, 2],
        [2, 3, 7, 6, 8, 4, 1, 5, 9],
        [4, 7, 3, 8, 1, 5, 9, 2, 6],
        [8, 1, 9, 7, 6, 2, 5, 3, 4],
        [6, 5, 2, 4, 9, 3, 7, 8, 1]
    ]

    gridhard = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    gridqhard = [gridhardq1, gridhardq2, gridhardq3]
    gridahard = [gridharda1, gridharda2, gridharda3]

    def get_cordhard(poshard):
        global xhard
        xhard = (poshard[0] - 230) // difhard
        global yhard
        yhard = (poshard[1] - 110) // difhard

    def inithard():
        global chanceshard
        chanceshard = 5

        global nhard
        nhard = random.randint(0, 2)
        global queshard
        queshard = gridqhard[nhard]
        global solhard
        solhard = gridahard[nhard]

    def init_gridhard():
        for i in range(9):
            for j in range(9):
                if gridhard[i][j] != 0:
                    gridhard[i][j] = 0

    def draw_gridhard():

        for i in range(9):
            for j in range(9):
                if queshard[i][j] == 0:
                    if gridhard[i][j] != 0:
                        text1 = fotnhard.render(str(gridhard[i][j]), 1, (38, 0, 80, 1))
                        mydishard.blit(text1, (i * difhard + 15 + 230, j * difhard + 15 + 110))

    def draw_boxhard():
        for i in range(2):
            pygame.draw.line(mydishard, (255, 255, 255), (xhard * difhard - 2 + 230, (yhard + i) * difhard + 110),
                             (xhard * difhard + difhard + 2 + 230, (yhard + i) * difhard + 110), 7)
            pygame.draw.line(mydishard, (255, 255, 255), ((xhard + i) * difhard + 230, yhard * difhard + 110),
                             ((xhard + i) * difhard + 230, yhard * difhard + difhard + 110), 7)

    def draw_valhard(valhard):
        text1 = fotnhard.render(str(valhard), 1, (38, 231, 80, 1))
        mydishard.blit(text1, (xhard * difhard + 15 + 230, yhard * difhard + 15 + 110))

    def draw_solhard():
        for i in range(9):
            for j in range(9):
                text1 = fotnhard.render(str(solhard[i][j]), 1, (38, 0, 80, 1))
                mydishard.blit(text1, (i * difhard + 15 + 230, j * difhard + 15 + 110))

    def draw_queshard():

        for i in range(9):
            for j in range(9):
                if queshard[i][j] != 0:
                    text1 = fotnhard.render(str(queshard[i][j]), 1, (38, 0, 80, 1))
                    mydishard.blit(text1, (i * difhard + 15 + 230, j * difhard + 15 + 110))

    def error1hard():
        button = mixer.Sound("sudoku_error.wav")
        button.play()
        text1 = fotnhard.render("NOT A valhardID KEY", 1, (117, 255, 255, 1))
        mydishard.blit(text1, (250, 45))

        text7 = fotnhard.render(str(chanceshard), 1, (38, 0, 80, 1))
        mydishard.blit(text7, (850, 40))

    def losthard():
        bg = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydishard.blit(bg, (0, 0))
        mixer.music.stop()
        button = mixer.Sound("sudoku_loosing.wav")
        button.play()
        text9 = fontxhard.render("--GAME__OVER--", 1, (255, 255, 255))
        mydishard.blit(text9, (300, 330))
        pygame.display.update()

    def winhard():
        ahard = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        for i in range(9):
            for j in range(9):
                ahard[i][j] = int(queshard[i][j]) + int(gridhard[i][j])

        if ahard == solhard:
            bg = pygame.image.load("blackbg.jpg")
            bg = pygame.transform.scale(bg, (1000, 700))
            mydishard.blit(bg, (0, 0))
            mixer.music.stop()
            button = mixer.Sound("pair_winning.wav")
            button.play()
            pygame.draw.rect(mydishard, (0, 0, 0), (10, 10, 1000, 700))
            text11 = fontxhard.render("--WINNER--", 1, (255, 255, 255))
            mydishard.blit(text11, (350, 330))
            pygame.display.update()
            pygame.time.wait(3000)
            bghard()
            inithard()
            chanceshard = 5
            chanceshard += 0
            draw_queshard()
            init_gridhard()
            mixer.music.load('sudoku_background.mp3')
            mixer.music.play(-1)

    bghard()
    inithard()
    draw_queshard()
    init_gridhard()
    draw_gridhard()

    while runhard:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runhard = False
            valhard = 0

            bghard()
            draw_queshard()
            draw_gridhard()

            if event.type == pygame.MOUSEBUTTONDOWN:
                button = mixer.Sound("button.wav")
                button.play()

                poshard = pygame.mouse.get_pos()

                if poshard[0] >= 810 and poshard[0] <= 960:
                    if poshard[1] >= 315 and poshard[1] <= 350:
                        flaghard = 0
                        buttonhard = 0
                        bghard()
                        pygame.display.update()
                        draw_solhard()
                        pygame.display.update()
                        pygame.time.wait(3000)
                        init_gridhard()
                        inithard()
                        draw_queshard()
                        draw_gridhard()
                        chanceshard = 5

                if poshard[0] >= 810 and poshard[0] <= 960:
                    if poshard[1] >= 370 and poshard[1] <= 405:
                        init_gridhard()
                        bghard()
                        inithard()
                        init_gridhard()
                        draw_queshard()
                        draw_gridhard()
                        flag1hard = 0
                        chanceshard = 5

                if poshard[0] >= 230 and poshard[1] >= 110:
                    if poshard[0] <= 770 and poshard[1] <= 650:
                        flag1hard = 1
                        buttonhard = 1
                        get_cordhard(poshard)
                        # print(xhard,yhard)

                if poshard[0] >= 810 and poshard[1] >= 425:
                    if poshard[0] <= 960 and poshard[1] <= 460:
                        button = mixer.Sound("button.wav")
                        button.play()
                        import sudoku_levels
                        sudoku_levels.levels()
            if buttonhard == 1:
                if event.type == pygame.KEYDOWN:
                    pygame.draw.rect(mydishard, (0, 0, 0), (10, 10, 600, 100))
                    if event.key == pygame.K_LEFT:
                        if xhard > 0:
                            xhard -= 1

                        flag1hard = 1
                    if event.key == pygame.K_RIGHT:
                        if xhard < 8:
                            xhard += 1
                        flag1hard = 1
                    if event.key == pygame.K_UP:
                        if yhard > 0:
                            yhard -= 1
                        flag1hard = 1
                    if event.key == pygame.K_DOWN:
                        if yhard < 8:
                            yhard += 1
                        flag1hard = 1
                    if event.key == pygame.K_1:
                        valhard = 1
                    if event.key == pygame.K_2:
                        valhard = 2
                    if event.key == pygame.K_3:
                        valhard = 3
                    if event.key == pygame.K_4:
                        valhard = 4
                    if event.key == pygame.K_5:
                        valhard = 5
                    if event.key == pygame.K_6:
                        valhard = 6
                    if event.key == pygame.K_7:
                        valhard = 7
                    if event.key == pygame.K_8:
                        valhard = 8
                    if event.key == pygame.K_9:
                        valhard = 9

            if flag1hard == 1:
                draw_boxhard()
                text7 = fotnhard.render(str(chanceshard), 1, (255, 255, 255, 1))
                mydishard.blit(text7, (850, 40))

            if valhard != 0:

                if valhard == solhard[int(xhard)][int(yhard)]:
                    gridhard[int(xhard)][int(yhard)] = solhard[int(xhard)][int(yhard)]
                    # draw_valhard(valhard)
                    draw_gridhard()

                if valhard != solhard[int(xhard)][int(yhard)]:
                    draw_valhard(valhard)
                    error1hard()
                    chanceshard -= 1
                    text7 = fotnhard.render(str(chanceshard), 1, (38, 0, 80, 1))
                    mydishard.blit(text7, (850, 40))

            if chanceshard < 1:
                pygame.draw.rect(mydishard, (0, 0, 0), (10, 10, 1000, 700))
                pygame.display.update
                losthard()

                pygame.time.wait(3000)
                chanceshard = 5
                init_gridhard()
                inithard()
                bghard()
                draw_queshard()
                mixer.music.load('sudoku_background.mp3')
                mixer.music.play(-1)
            winhard()
        pygame.display.update()
    pygame.quit()
    sys.exit()


sudoku_hard()
pygame.quit()
sys.exit()
