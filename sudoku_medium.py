import pygame
import sys
import random
from pygame import mixer

pygame.init()
pygame.font.init()


def sudoku_medium():
    mixer.music.load('Sudoku_Items/Sound/sudoku_background.mp3')
    mixer.music.play(-1)
    pygame.init()
    pygame.font.init()
    mydismed = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("SUDOKU MEDIUM BY BRAIN STEAKS")
    imgmed = pygame.image.load('Sudoku_Items/Images/sudoku.png')
    pygame.display.set_icon(imgmed)

    def create_fontmed(t, s=25, c=(255, 255, 0), b=False, i=False):
        font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
        text = font.render(t, True, c)
        return text

    fontnmed = pygame.font.SysFont("comicsans", 40)
    fontxmed = pygame.font.SysFont("comicsans", 70)

    def bgmed():
        bg = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydismed.blit(bg, (0, 0))
        bg1 = pygame.image.load('Sudoku_Items/Images/sudoku.png')
        bg1 = pygame.transform.scale(bg1, (1000, 700))
        mydismed.blit(bg1, (0, 0))
        pygame.draw.rect(mydismed, (0, 0, 255), (810, 315, 150, 35))
        pygame.draw.rect(mydismed, (0, 0, 255), (810, 370, 150, 35))
        pygame.draw.rect(mydismed, (0, 0, 255), (810, 425, 150, 35))
        text3 = create_fontmed("ANS FOR U")
        mydismed.blit(text3, (820, 320))
        text4 = create_fontmed("     RESET   ")
        mydismed.blit(text4, (820, 375))
        text6 = create_fontmed("CHANCES LEFT :")
        mydismed.blit(text6, (660, 40))
        text7 = create_fontmed("       EXIT   ")
        mydismed.blit(text7, (820, 430))
        # text5 = create_fontmed("     UNDO   ")
        # mydismed.blit(text5, (820, 430))

    runmed = True
    global flag1med
    global flagmed
    global chancesmed
    flag1med = 0
    buttonmed = 1
    valmed = 0
    global xmed
    global ymed
    difmed = 60
    gridq1med = [
        [6, 3, 0, 0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 8, 9, 0, 0],
        [4, 8, 0, 6, 2, 0, 0, 0, 0],
        [2, 6, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 4, 0, 0, 0, 7, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 4, 9],
        [0, 0, 0, 0, 3, 1, 0, 7, 8],
        [0, 0, 1, 7, 0, 0, 0, 3, 0],
        [0, 0, 0, 0, 0, 0, 0, 9, 5]
    ]
    gridq2med = [
        [7, 0, 3, 0, 0, 0, 0, 8, 0],
        [4, 5, 0, 2, 0, 0, 9, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 3, 6, 9, 0, 0, 0, 0, 8],
        [0, 0, 7, 0, 0, 4, 0, 1, 0],
        [9, 0, 0, 0, 3, 0, 0, 0, 0],
        [3, 0, 0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 7, 0, 0, 0, 5],
        [0, 0, 2, 8, 0, 0, 0, 4, 1]
    ]

    gridq3med = [
        [0, 8, 0, 7, 0, 1, 0, 3, 0],
        [4, 0, 9, 0, 0, 0, 0, 0, 0],
        [0, 5, 0, 0, 6, 0, 4, 1, 8],
        [7, 0, 0, 0, 0, 9, 0, 0, 0],
        [8, 0, 0, 6, 1, 0, 5, 0, 0],
        [0, 3, 5, 0, 0, 0, 0, 2, 9],
        [0, 6, 0, 4, 0, 7, 0, 9, 0],
        [1, 0, 0, 0, 0, 8, 0, 0, 4],
        [0, 2, 0, 0, 5, 0, 0, 7, 0]
    ]

    grida1med = [
        [6, 3, 9, 5, 1, 7, 8, 2, 4],
        [1, 2, 7, 3, 4, 8, 9, 5, 6],
        [4, 8, 5, 6, 2, 9, 3, 1, 7],
        [2, 6, 3, 9, 7, 4, 5, 8, 1],
        [9, 1, 4, 8, 5, 2, 7, 6, 3],
        [7, 5, 8, 1, 6, 3, 2, 4, 9],
        [5, 9, 6, 2, 3, 1, 4, 7, 8],
        [8, 4, 1, 7, 9, 5, 6, 3, 2],
        [3, 7, 2, 4, 8, 6, 1, 9, 5]
    ]
    grida2med = [
        [7, 2, 3, 1, 9, 6, 5, 8, 4],
        [4, 5, 1, 2, 8, 7, 9, 6, 3],
        [8, 6, 9, 3, 4, 5, 1, 2, 7],
        [5, 3, 6, 9, 2, 1, 4, 7, 8],
        [2, 8, 7, 5, 6, 4, 3, 1, 9],
        [9, 1, 4, 7, 3, 8, 6, 5, 2],
        [3, 7, 5, 4, 1, 2, 8, 9, 6],
        [1, 4, 8, 6, 7, 9, 2, 3, 5],
        [6, 9, 2, 8, 5, 3, 7, 4, 1]
    ]

    grida3med = [
        [2, 8, 6, 7, 4, 1, 9, 3, 5],
        [4, 1, 9, 3, 8, 5, 7, 6, 2],
        [3, 5, 7, 9, 6, 2, 4, 1, 8],
        [7, 4, 1, 5, 2, 9, 3, 8, 6],
        [8, 9, 2, 6, 1, 3, 5, 4, 7],
        [6, 3, 5, 8, 7, 4, 1, 2, 9],
        [5, 6, 8, 4, 3, 7, 2, 9, 1],
        [1, 7, 3, 2, 9, 8, 6, 5, 4],
        [9, 2, 4, 1, 5, 6, 8, 7, 3]
    ]

    gridmed = [
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
    gridqmed = [gridq1med, gridq2med, gridq3med]
    gridamed = [grida1med, grida2med, grida3med]

    def get_cordmed(pos):
        global xmed
        xmed = (pos[0] - 230) // difmed
        global ymed
        ymed = (pos[1] - 110) // difmed

    def initmed():
        global chancesmed
        chancesmed = 5

        global nmed
        nmed = random.randint(0, 2)
        # print(nmed)
        global quesmed
        quesmed = gridqmed[nmed]
        global solmed
        solmed = gridamed[nmed]

    def init_gridmed():
        for i in range(9):
            for j in range(9):
                if gridmed[i][j] != 0:
                    gridmed[i][j] = 0

    def draw_gridmed():

        for i in range(9):
            for j in range(9):
                if quesmed[i][j] == 0:
                    if gridmed[i][j] != 0:
                        text1 = fontnmed.render(str(gridmed[i][j]), 1, (38, 0, 80, 1))
                        mydismed.blit(text1, (i * difmed + 15 + 230, j * difmed + 15 + 110))

    def draw_boxmed():
        for i in range(2):
            pygame.draw.line(mydismed, (255, 255, 255), (xmed * difmed - 2 + 230, (ymed + i) * difmed + 110),
                             (xmed * difmed + difmed + 2 + 230, (ymed + i) * difmed + 110), 7)
            pygame.draw.line(mydismed, (255, 255, 255), ((xmed + i) * difmed + 230, ymed * difmed + 110),
                             ((xmed + i) * difmed + 230, ymed * difmed + difmed + 110), 7)

    def draw_valmed(valmed):
        text1 = fontnmed.render(str(valmed), 1, (38, 231, 80, 1))
        mydismed.blit(text1, (xmed * difmed + 15 + 230, ymed * difmed + 15 + 110))

    def draw_solmed():
        for i in range(9):
            for j in range(9):
                text1 = fontnmed.render(str(solmed[i][j]), 1, (38, 0, 80, 1))
                mydismed.blit(text1, (i * difmed + 15 + 230, j * difmed + 15 + 110))

    def draw_quesmed():

        for i in range(9):
            for j in range(9):
                if quesmed[i][j] != 0:
                    text1 = fontnmed.render(str(quesmed[i][j]), 1, (38, 0, 80, 1))
                    mydismed.blit(text1, (i * difmed + 15 + 230, j * difmed + 15 + 110))

    def error1med():
        button = mixer.Sound("Sudoku_Items/Sound/sudoku_error.wav")
        button.play()
        text1 = fontnmed.render("NOT A VALID KEY", 1, (117, 255, 255, 1))
        mydismed.blit(text1, (250, 45))

        text7 = fontnmed.render(str(chancesmed), 1, (38, 0, 80, 1))
        mydismed.blit(text7, (850, 40))

    def lostmed():
        bg = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydismed.blit(bg, (0, 0))
        mixer.music.stop()
        button = mixer.Sound("Sudoku_Items/Sound/sudoku_loosing.wav")
        button.play()
        text9 = fontxmed.render("--GAME__OVER--", 1, (255, 255, 255))
        mydismed.blit(text9, (300, 330))
        pygame.display.update()

    def winmed():
        amed = [
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
                amed[i][j] = int(quesmed[i][j]) + int(gridmed[i][j])

        if amed == solmed:
            bg = pygame.image.load("blackbg.jpg")
            bg = pygame.transform.scale(bg, (1000, 700))
            mydismed.blit(bg, (0, 0))
            mixer.music.stop()
            button = mixer.Sound("Sudoku_Items/Sound/pair_winning.wav")
            button.play()
            pygame.draw.rect(mydismed, (0, 0, 0), (10, 10, 1000, 700))
            text11 = fontxmed.render("--WINNER--", 1, (255, 255, 255))
            mydismed.blit(text11, (350, 330))
            pygame.display.update()
            pygame.time.wait(3000)
            bgmed()
            initmed()
            chancesmed = 5
            chancesmed += 0
            draw_quesmed()
            init_gridmed()
            mixer.music.load('Sudoku_Items/Sound/sudoku_background.mp3')
            mixer.music.play(-1)

    bgmed()
    initmed()
    draw_quesmed()
    init_gridmed()
    draw_gridmed()

    while runmed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runmed = False
            valmed = 0

            bgmed()
            draw_quesmed()
            draw_gridmed()

            if event.type == pygame.MOUSEBUTTONDOWN:
                button = mixer.Sound("Sudoku_Items/Sound/sudoku_button.wav")
                button.play()
                pos = pygame.mouse.get_pos()

                if pos[0] >= 810 and pos[0] <= 960:
                    if pos[1] >= 315 and pos[1] <= 350:
                        flagmed = 0
                        buttonmed = 0
                        bgmed()
                        pygame.display.update()
                        draw_solmed()
                        pygame.display.update()
                        pygame.time.wait(3000)
                        init_gridmed()
                        initmed()
                        draw_quesmed()
                        draw_gridmed()
                        chancesmed = 5

                if pos[0] >= 810 and pos[0] <= 960:
                    if pos[1] >= 370 and pos[1] <= 405:
                        init_gridmed()
                        bgmed()
                        initmed()
                        init_gridmed()
                        draw_quesmed()
                        draw_gridmed()

                        flag1med = 0
                        chancesmed = 5

                if pos[0] >= 230 and pos[1] >= 110:
                    if pos[0] <= 770 and pos[1] <= 650:
                        flag1med = 1
                        buttonmed = 1
                        get_cordmed(pos)

                if pos[0] >= 810 and pos[1] >= 425:
                    if pos[0] <= 960 and pos[1] <= 460:
                        button = mixer.Sound("Sudoku_Items/Sound/sudoku_button.wav")
                        button.play()
                        import sudoku_levels
                        sudoku_levels.levels()

            if buttonmed == 1:
                if event.type == pygame.KEYDOWN:
                    pygame.draw.rect(mydismed, (0, 0, 0), (10, 10, 600, 100))
                    if event.key == pygame.K_LEFT:
                        if xmed > 0:
                            xmed -= 1

                        flag1med = 1
                    if event.key == pygame.K_RIGHT:
                        if xmed < 8:
                            xmed += 1
                        flag1med = 1
                    if event.key == pygame.K_UP:
                        if ymed > 0:
                            ymed -= 1
                        flag1med = 1
                    if event.key == pygame.K_DOWN:
                        if ymed < 8:
                            ymed += 1
                        flag1med = 1
                    if event.key == pygame.K_1:
                        valmed = 1
                    if event.key == pygame.K_2:
                        valmed = 2
                    if event.key == pygame.K_3:
                        valmed = 3
                    if event.key == pygame.K_4:
                        valmed = 4
                    if event.key == pygame.K_5:
                        valmed = 5
                    if event.key == pygame.K_6:
                        valmed = 6
                    if event.key == pygame.K_7:
                        valmed = 7
                    if event.key == pygame.K_8:
                        valmed = 8
                    if event.key == pygame.K_9:
                        valmed = 9

            if flag1med == 1:
                draw_boxmed()
                text7 = fontnmed.render(str(chancesmed), 1, (255, 255, 255, 1))
                mydismed.blit(text7, (850, 40))

            if valmed != 0:

                if valmed == solmed[int(xmed)][int(ymed)]:
                    gridmed[int(xmed)][int(ymed)] = solmed[int(xmed)][int(ymed)]
                    # draw_val(valmed)
                    draw_gridmed()

                if valmed != solmed[int(xmed)][int(ymed)]:
                    draw_valmed(valmed)
                    error1med()
                    chancesmed -= 1
                    text7 = fontnmed.render(str(chancesmed), 1, (38, 0, 80, 1))
                    mydismed.blit(text7, (850, 40))

            if chancesmed < 1:
                pygame.draw.rect(mydismed, (0, 0, 0), (10, 10, 1000, 700))
                pygame.display.update
                lostmed()

                pygame.time.wait(3000)
                chancesmed = 5
                init_gridmed()
                initmed()
                bgmed()
                mixer.music.load('Sudoku_Items/Sound/sudoku_background.mp3')
                mixer.music.play(-1)
                draw_quesmed()
            winmed()
        pygame.display.update()
    pygame.quit()
    sys.exit()


sudoku_medium()
pygame.quit()
sys.exit()
