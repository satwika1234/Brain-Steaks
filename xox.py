import pygame
import sys
from pygame import mixer

pygame.init()
mydis = pygame.display.set_mode((1000, 700))
black = (0, 0, 0)
white = (255, 255, 255)
erase = (200, 0, 255)
fontObj = pygame.font.Font('freesansbold.ttf', 90)
fontObj2 = pygame.font.Font('freesansbold.ttf', 50)
fontObj3 = pygame.font.Font('freesansbold.ttf', 40)
pygame.display.set_caption("XOX BY BRAIN STEAKS")
xscore = 0
oscore = 0
fc = "X"


class clickable:
    def __init__(self, startx, starty, w, h, uid):
        self.startx = startx
        self.starty = starty
        self.w = w
        self.h = h
        self.uid = uid

    def isover(self, pos):
        if pos[0] > self.startx and pos[0] < self.startx + self.w:
            if pos[1] > self.starty and pos[1] < self.starty + self.h:
                return True
            else:
                return False
        else:
            return False


def xox():
    mixer.music.load('xox_background.mp3')
    mixer.music.play(-1)

    diag = 0

    def strter():
        mixer.music.load('xox_background.mp3')
        mixer.music.play(-1)
        global oscore
        global xscore
        oscore = 0
        xscore = 0

    strter()

    def initpage():
        nonlocal chance
        img = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(img, (1000, 700))
        mydis.blit(bg, (0, 0))
        img = pygame.image.load("xox.png")
        bg = pygame.transform.scale(img, (1000, 700))
        mydis.blit(bg, (0, 0))
        img = pygame.image.load("xoxglow.png")
        glw = pygame.transform.scale(img, (300, 100))

        textSurfaceObj = fontObj2.render("Player X:", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (755, 150)
        mydis.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj2.render("Player O:", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (755, 290)
        mydis.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj2.render("RESET", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (810, 470)
        mydis.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj2.render("BACK", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (810, 610)
        mydis.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj2.render(str(xscore), True, black)
        textRectObjx = textSurfaceObj.get_rect()
        textRectObjx.center = (910, 150)
        mydis.blit(textSurfaceObj, textRectObjx)

        textSurfaceObj = fontObj2.render(str(oscore), True, black)
        textRectObjx = textSurfaceObj.get_rect()
        textRectObjx.center = (910, 290)
        mydis.blit(textSurfaceObj, textRectObjx)

        chance = fc

    reset_b = clickable(660, 420, 300, 100, 10)
    back_b = clickable(660, 560, 300, 100, 10)
    rest_b = clickable(280, 420, 190, 50, 20)
    bck_b = clickable(530, 420, 190, 50, 20)

    initpage()
    boxes = [[0 for i in range(3)] for i in range(3)]
    taken = [] * 9

    for i in range(3):
        for j in range(3):
            boxes[i][j] = clickable(20 + i * 200, 80 + j * 200, 200, 200, 3 * i + j)
    filled = [[0 for i in range(3)] for i in range(3)]

    def xwin():
        button = mixer.Sound("xox_winning.wav")
        button.play()
        global xscore
        nonlocal filled
        nonlocal taken
        global fc
        img = pygame.image.load("xoxglow.png")
        glw = pygame.transform.scale(img, (340, 140))
        mydis.blit(glw, (640, 80))
        pygame.display.update()
        pygame.time.wait(1000)
        xscore = xscore + 1
        if xscore == 5:
            mixer.music.stop()
            button = mixer.Sound("pair_winning.wav")
            button.play()
            img = pygame.image.load("dim.png")
            dim = pygame.transform.scale(img, (1000, 700))
            img = pygame.image.load("dialog.png")
            dial = pygame.transform.scale(img, (1000, 700))
            nonlocal diag
            mydis.blit(dim, (0, 0))
            mydis.blit(dial, (0, 0))
            textSurfaceObj = fontObj2.render("X won", True, black)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (500, 300)
            mydis.blit(textSurfaceObj, textRectObj)
            textSurfaceObj = fontObj3.render("RESTART", True, black)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (375, 445)
            mydis.blit(textSurfaceObj, textRectObj)
            textSurfaceObj = fontObj3.render("BACK", True, black)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (625, 445)
            mydis.blit(textSurfaceObj, textRectObj)
            pygame.display.update()
            diag = 1

        else:

            textSurfaceObj = fontObj2.render(str(xscore), True, black)
            textRectObjx = textSurfaceObj.get_rect()
            textRectObjx.center = (910, 150)
            mydis.blit(textSurfaceObj, textRectObjx)

            initpage()

            taken = []
            filled = [[0 for i in range(3)] for i in range(3)]

            if fc == "X":
                fc = "O"
            else:
                fc = "X"

    def owin():
        button = mixer.Sound("xox_winning.wav")
        button.play()
        global oscore
        nonlocal taken
        nonlocal filled
        global fc
        img = pygame.image.load("xoxglow.png")
        glw = pygame.transform.scale(img, (340, 140))
        mydis.blit(glw, (640, 220))
        pygame.display.update()
        pygame.time.wait(1000)

        oscore = oscore + 1

        if oscore == 5:
            mixer.music.stop()
            button = mixer.Sound("pair_winning.wav")
            button.play()
            img = pygame.image.load("dim.png")
            dim = pygame.transform.scale(img, (1000, 700))
            img = pygame.image.load("dialog.png")
            dial = pygame.transform.scale(img, (1000, 700))
            nonlocal diag
            mydis.blit(dim, (0, 0))
            mydis.blit(dial, (0, 0))
            textSurfaceObj = fontObj2.render("O won", True, black)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (500, 300)
            mydis.blit(textSurfaceObj, textRectObj)
            textSurfaceObj = fontObj3.render("RESTART", True, black)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (375, 445)
            mydis.blit(textSurfaceObj, textRectObj)
            textSurfaceObj = fontObj3.render("BACK", True, black)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (625, 445)
            mydis.blit(textSurfaceObj, textRectObj)
            pygame.display.update()
            diag = 1

        else:

            textSurfaceObj = fontObj2.render(str(oscore), True, black)
            textRectObjx = textSurfaceObj.get_rect()
            textRectObjx.center = (910, 290)
            mydis.blit(textSurfaceObj, textRectObjx)

            initpage()

            taken = []
            filled = [[0 for i in range(3)] for i in range(3)]

            if fc == "X":
                fc = "O"
            else:
                fc = "X"

    def draw():
        nonlocal taken
        nonlocal filled
        global fc
        pygame.time.wait(1000)
        initpage()
        # init("drw")
        taken = []
        filled = [[0 for i in range(3)] for i in range(3)]

        if fc == "X":
            fc = "O"
        else:
            fc = "X"

    def reset_game():
        nonlocal taken
        nonlocal filled
        global oscore
        global xscore
        taken = []
        filled = [[0 for i in range(3)] for i in range(3)]
        oscore = 0
        xscore = 0
        initpage()
        strter()

    def check():
        for i in range(3):
            if filled[i][0] == filled[i][1] and filled[i][2] == filled[i][1]:
                if filled[i][0] == "X":
                    xwin()
                elif filled[i][0] == "O":
                    owin()
            elif filled[0][i] == filled[1][i] and filled[2][i] == filled[1][i]:
                if filled[0][i] == "X":
                    xwin()
                    # print("x win row")
                elif filled[1][i] == "O":
                    owin()
        if filled[0][0] == filled[1][1] and filled[1][1] == filled[2][2]:
            if filled[0][0] == "X":
                xwin()
                # print("x win lead")
            elif filled[0][0] == "O":
                owin()
        elif filled[0][2] == filled[1][1] and filled[1][1] == filled[2][0]:
            if filled[0][2] == "X":
                xwin()
                # print("x win dig")
            elif filled[2][0] == "O":
                owin()
        if len(taken) == 9:
            draw()

    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if diag == 0:
                    for i in range(3):
                        for j in range(3):
                            if boxes[i][j].isover(pos) and boxes[i][j] not in taken:
                                textSurfaceObj = fontObj.render(chance, True, black)
                                textRectObj = textSurfaceObj.get_rect()
                                textRectObj.center = (120 + 200 * i, 180 + 200 * j)
                                mydis.blit(textSurfaceObj, textRectObj)
                                filled[i][j] = chance
                                taken.append(boxes[i][j])
                                pygame.display.update()
                                check()

                                if chance == "X":
                                    button = mixer.Sound("button.wav")
                                    button.play()
                                    chance = "O"
                                else:
                                    button = mixer.Sound("button.wav")
                                    button.play()
                                    chance = "X"
                    if reset_b.isover(pos):
                        button = mixer.Sound("button.wav")
                        button.play()
                        reset_game()
                    if back_b.isover(pos):
                        button = mixer.Sound("button.wav")
                        button.play()
                        import xox_menupage
                        xox_menupage.main()
                else:
                    if rest_b.isover(pos):
                        button = mixer.Sound("button.wav")
                        button.play()
                        diag = 0
                        reset_game()
                    if bck_b.isover(pos):
                        button = mixer.Sound("button.wav")
                        button.play()
                        diag = 0
                        import frontpage
                        frontpage.mainpage()

        pygame.display.update()


xox()
