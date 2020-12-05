import pygame
import sys
import random
from pygame import mixer

pygame.init()
pygame.font.init()


def sudoku_easy():
    mixer.music.load('sudoku_background.mp3')
    mixer.music.play(-1)
    pygame.init()
    pygame.font.init()
    mydis = pygame.display.set_mode((1000, 700))
    pygame.display.set_caption("SUDOKU EASY BY BRAIN STEAKS")
    img = pygame.image.load('sudoku.png')
    pygame.display.set_icon(img)

    def create_font(t, s=25, c=(255, 255, 0), b=False, i=False):
        font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
        text = font.render(t, True, c)
        return text

    fontn = pygame.font.SysFont("comicsans", 40)
    fontx = pygame.font.SysFont("comicsans", 70)

    def bg():
        bg = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydis.blit(bg, (0, 0))

        bg1 = pygame.image.load('sudoku.png')
        bg1 = pygame.transform.scale(bg1, (1000, 700))
        mydis.blit(bg1, (0, 0))
        pygame.draw.rect(mydis, (0, 0, 255), (810, 315, 150, 35))
        pygame.draw.rect(mydis, (0, 0, 255), (810, 370, 150, 35))
        pygame.draw.rect(mydis, (0, 0, 255), (810, 425, 150, 35))
        text3 = create_font("ANS FOR U")
        mydis.blit(text3, (820, 320))
        text4 = create_font("     RESET   ")
        mydis.blit(text4, (820, 375))
        text6 = create_font("CHANCES LEFT :")
        mydis.blit(text6, (660, 40))
        text7 = create_font("       EXIT   ")
        mydis.blit(text7, (820, 430))
        # text5 = create_font("     UNDO   ")
        # mydis.blit(text5, (820, 430))

    run = True
    global flag1
    global flag
    global chances
    flag1 = 0
    button = 1
    val = 0
    global x
    global y
    dif = 60
    gridq1 = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
    gridq2 = [
        [5, 6, 0, 8, 4, 7, 0, 0, 0],
        [3, 0, 9, 0, 0, 0, 6, 0, 0],
        [0, 0, 8, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 8, 0, 0, 4, 0],
        [7, 9, 0, 6, 0, 2, 0, 1, 8],
        [0, 5, 0, 0, 3, 0, 0, 9, 0],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [0, 0, 6, 0, 0, 0, 8, 0, 7],
        [0, 0, 0, 3, 1, 6, 0, 5, 9]
    ]

    grida1 = [
        [7, 8, 5, 4, 3, 9, 1, 2, 6],
        [6, 1, 2, 8, 7, 5, 3, 4, 9],
        [4, 9, 3, 6, 2, 1, 5, 7, 8],
        [8, 5, 7, 9, 4, 3, 2, 6, 1],
        [2, 6, 1, 7, 5, 8, 9, 3, 4],
        [9, 3, 4, 1, 6, 2, 7, 8, 5],
        [5, 7, 8, 3, 9, 4, 6, 1, 2],
        [1, 2, 6, 5, 8, 7, 4, 9, 3],
        [3, 4, 9, 2, 1, 6, 8, 5, 7]
    ]
    grida2 = [
        [5, 6, 1, 8, 4, 7, 9, 2, 3],
        [3, 7, 9, 5, 2, 1, 6, 8, 4],
        [4, 2, 8, 9, 6, 3, 1, 7, 5],
        [6, 1, 3, 7, 8, 9, 5, 4, 2],
        [7, 9, 4, 6, 5, 2, 3, 1, 8],
        [8, 5, 2, 1, 3, 4, 7, 9, 6],
        [9, 3, 5, 4, 7, 8, 2, 6, 1],
        [1, 4, 6, 2, 9, 5, 8, 3, 7],
        [2, 8, 7, 3, 1, 6, 4, 5, 9]
    ]

    grid = [
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
    gridq = [gridq1, gridq2]
    grida = [grida1, grida2]

    def get_cord(pos):
        global x
        x = (pos[0] - 230) // dif
        global y
        y = (pos[1] - 110) // dif

    def init():
        global chances
        chances = 5

        global n
        n = random.randint(0, 1)
        #print(n)
        global ques
        ques = gridq[n]
        global sol
        sol = grida[n]

    def init_grid():
        for i in range(9):
            for j in range(9):
                if grid[i][j] != 0:
                    grid[i][j] = 0

    def draw_grid():

        for i in range(9):
            for j in range(9):
                if ques[i][j] == 0:
                    if grid[i][j] != 0:
                        text1 = fontn.render(str(grid[i][j]), 1, (38, 0, 80, 1))
                        mydis.blit(text1, (i * dif + 15 + 230, j * dif + 15 + 110))

    def draw_box():
        for i in range(2):
            pygame.draw.line(mydis, (255, 255, 255), (x * dif - 2 + 230, (y + i) * dif + 110),
                             (x * dif + dif + 2 + 230, (y + i) * dif + 110), 7)
            pygame.draw.line(mydis, (255, 255, 255), ((x + i) * dif + 230, y * dif + 110),
                             ((x + i) * dif + 230, y * dif + dif + 110), 7)

    def draw_val(val):
        text1 = fontn.render(str(val), 1, (38, 231, 80, 1))
        mydis.blit(text1, (x * dif + 15 + 230, y * dif + 15 + 110))

    def draw_sol():
        for i in range(9):
            for j in range(9):
                text1 = fontn.render(str(sol[i][j]), 1, (38, 0, 80, 1))
                mydis.blit(text1, (i * dif + 15 + 230, j * dif + 15 + 110))

    def draw_ques():

        for i in range(9):
            for j in range(9):
                if ques[i][j] != 0:
                    text1 = fontn.render(str(ques[i][j]), 1, (38, 0, 80, 1))
                    mydis.blit(text1, (i * dif + 15 + 230, j * dif + 15 + 110))

    def error1():
        button = mixer.Sound("sudoku_error.wav")
        button.play()
        text1 = fontn.render("NOT A VALID KEY", 1, (117, 255, 255, 1))
        mydis.blit(text1, (250, 45))

        text7 = fontn.render(str(chances), 1, (38, 0, 80, 1))
        mydis.blit(text7, (850, 40))

    def lost():
        mixer.music.stop()
        button = mixer.Sound("sudoku_loosing.wav")
        button.play()
        bg = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydis.blit(bg, (0, 0))
        text9 = fontx.render("--GAME__OVER--", 1, (255, 255, 255))
        mydis.blit(text9, (300, 330))
        pygame.display.update()

    def win():

        a = [
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
                a[i][j] = int(ques[i][j]) + int(grid[i][j])

        if a == sol:
            bg = pygame.image.load("blackbg.jpg")
            bg = pygame.transform.scale(bg, (1000, 700))
            mydis.blit(bg, (0, 0))
            mixer.music.stop()
            #button = mixer.Sound("pair_winning.wav")
            #button.play()
            pygame.draw.rect(mydis, (0, 0, 0), (10, 10, 1000, 700))
            text11 = fontx.render("--WINNER--", 1, (255, 255, 255))
            mydis.blit(text11, (350, 330))
            pygame.display.update()
            pygame.time.wait(3000)
            bg()
            init()
            mixer.music.load('sudoku_background.mp3')
            mixer.music.play(-1)
            chances = 5
            chances += 0
            draw_ques()
            init_grid()

    bg()
    init()
    draw_ques()
    init_grid()
    draw_grid()

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            val = 0

            bg()
            draw_ques()
            draw_grid()

            if event.type == pygame.MOUSEBUTTONDOWN:
                button = mixer.Sound("button.wav")
                button.play()
                pos = pygame.mouse.get_pos()

                if pos[0] >= 810 and pos[0] <= 960:
                    if pos[1] >= 315 and pos[1] <= 350:
                        flag = 0
                        button = 0
                        bg()
                        pygame.display.update()
                        draw_sol()
                        pygame.display.update()
                        pygame.time.wait(2000)
                        init_grid()
                        init()
                        draw_ques()
                        draw_grid()
                        chances = 5

                if pos[0] >= 810 and pos[0] <= 960:
                    if pos[1] >= 370 and pos[1] <= 405:
                        init_grid()
                        bg()
                        init()
                        init_grid()
                        draw_ques()
                        draw_grid()
                        flag1 = 0
                        chances = 5

                if pos[0] >= 230 and pos[1] >= 110:
                    if pos[0] <= 770 and pos[1] <= 650:
                        flag1 = 1
                        button = 1
                        get_cord(pos)
                        #print(x, y)

                if pos[0] >= 810 and pos[1] >= 425:
                    if pos[0] <= 960 and pos[1] <= 460:
                        button = mixer.Sound("button.wav")
                        button.play()
                        import sudoku_levels
                        sudoku_levels.levels()


                        

            if button == 1:
                if event.type == pygame.KEYDOWN:
                    pygame.draw.rect(mydis, (0, 0, 0), (10, 10, 600, 100))
                    if event.key == pygame.K_LEFT:
                        if x > 0:
                            x -= 1

                        flag1 = 1
                    if event.key == pygame.K_RIGHT:
                        if x < 8:
                            x += 1
                        flag1 = 1
                    if event.key == pygame.K_UP:
                        if y > 0:
                            y -= 1
                        flag1 = 1
                    if event.key == pygame.K_DOWN:
                        if y < 8:
                            y += 1
                        flag1 = 1
                    if event.key == pygame.K_1:
                        val = 1
                    if event.key == pygame.K_2:
                        val = 2
                    if event.key == pygame.K_3:
                        val = 3
                    if event.key == pygame.K_4:
                        val = 4
                    if event.key == pygame.K_5:
                        val = 5
                    if event.key == pygame.K_6:
                        val = 6
                    if event.key == pygame.K_7:
                        val = 7
                    if event.key == pygame.K_8:
                        val = 8
                    if event.key == pygame.K_9:
                        val = 9

            if flag1 == 1:
                draw_box()
                text7 = fontn.render(str(chances), 1, (255, 255, 255, 1))
                mydis.blit(text7, (850, 40))

            if val != 0:

                if val == sol[int(x)][int(y)]:
                    grid[int(x)][int(y)] = sol[int(x)][int(y)]
                    # draw_val(val)
                    draw_grid()

                if val != sol[int(x)][int(y)]:
                    draw_val(val)
                    error1()
                    chances -= 1
                    text7 = fontn.render(str(chances), 1, (38, 0, 80, 1))
                    mydis.blit(text7, (850, 40))

            if chances < 1:
                pygame.draw.rect(mydis, (0, 0, 0), (10, 10, 1000, 700))
                pygame.display.update
                lost()

                pygame.time.wait(3000)
                chances = 5
                mixer.music.load('sudoku_background.mp3')
                mixer.music.play(-1)
                init_grid()
                init()
                bg()
                draw_ques()
            win()
        pygame.display.update()
    pygame.quit()
    sys.exit()


sudoku_easy()
pygame.quit()
sys.exit()
