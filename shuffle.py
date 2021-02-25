import pygame
import sys
import random
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()

mydis = pygame.display.set_mode((1000, 700), pygame.RESIZABLE)
white = (255, 250, 250)
txtcolor = (255, 13, 0)
btncolor = (240, 240, 240)
black = (0, 0, 0)
pygame.display.set_caption("SHUFFLE BY BRAIN STEAKS")
fontObj1 = pygame.font.Font('freesansbold.ttf', 70)
fontObj2 = pygame.font.Font('freesansbold.ttf', 50)
fontObj3 = pygame.font.Font('freesansbold.ttf', 40)


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


def shuffle():
    mixer.music.load('Shuffle_Items/Sound/shuffle_background.mp3')
    mixer.music.play(-1)

    back_b = clickable(30, 260, 200, 80, 50)
    reset_b = clickable(30, 360, 200, 80, 50)
    rest_b = clickable(280, 420, 190, 50, 20)
    bck_b = clickable(530, 420, 190, 50, 20)
    clicklist = []
    randlist = []
    diag = 0
    moves = 0
    imglist = [0] * 16

    img = pygame.image.load("Shuffle_Items/Images/dim.png")
    dim = pygame.transform.scale(img, (1000, 700))

    img = pygame.image.load("Shuffle_Items/Images/dialog.png")
    dial = pygame.transform.scale(img, (1000, 700))
    img = [0] * 16

    def reset():

        nonlocal imglist
        nonlocal back_b
        nonlocal reset_b
        nonlocal bck_b
        nonlocal rest_b
        nonlocal clicklist
        nonlocal moves
        nonlocal diag
        imglist = [0] * 16
        bg = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydis.blit(bg, (0, 0))

        addmoves()
        im1 = pygame.image.load("Shuffle_Items/Images/image_part_001.png")
        im2 = pygame.image.load("Shuffle_Items/Images/image_part_002.png")
        im3 = pygame.image.load("Shuffle_Items/Images/image_part_003.png")
        im4 = pygame.image.load("Shuffle_Items/Images/image_part_004.png")
        im5 = pygame.image.load("Shuffle_Items/Images/image_part_005.png")
        im6 = pygame.image.load("Shuffle_Items/Images/image_part_006.png")
        im7 = pygame.image.load("Shuffle_Items/Images/image_part_007.png")
        im8 = pygame.image.load("Shuffle_Items/Images/image_part_008.png")
        im9 = pygame.image.load("Shuffle_Items/Images/image_part_009.png")
        im10 = pygame.image.load("Shuffle_Items/Images/image_part_010.png")
        im11 = pygame.image.load("Shuffle_Items/Images/image_part_011.png")
        im12 = pygame.image.load("Shuffle_Items/Images/image_part_012.png")
        im13 = pygame.image.load("Shuffle_Items/Images/image_part_013.png")
        im14 = pygame.image.load("Shuffle_Items/Images/image_part_014.png")
        im15 = pygame.image.load("Shuffle_Items/Images/image_part_015.png")
        im16 = pygame.image.load("Shuffle_Items/Images/image_part_016.png")
        for i in range(1, 17):
            im_str = "im" + str(i)
            img[i - 1] = pygame.transform.scale(eval(im_str), (120, 120))
        randomise()

        initpage()

        clicklist = []
        imgpos1 = clickable(260, 170, 120, 120, 1)
        imgpos2 = clickable(380, 170, 120, 120, 2)
        imgpos3 = clickable(500, 170, 120, 120, 3)
        imgpos4 = clickable(620, 170, 120, 120, 4)
        imgpos5 = clickable(260, 290, 120, 120, 5)
        imgpos6 = clickable(380, 290, 120, 120, 6)
        imgpos7 = clickable(500, 290, 120, 120, 7)
        imgpos8 = clickable(620, 290, 120, 120, 8)
        imgpos9 = clickable(260, 410, 120, 120, 9)
        imgpos10 = clickable(380, 410, 120, 120, 10)
        imgpos11 = clickable(500, 410, 120, 120, 11)
        imgpos12 = clickable(620, 410, 120, 120, 12)
        imgpos13 = clickable(260, 530, 120, 120, 13)
        imgpos14 = clickable(380, 530, 120, 120, 14)
        imgpos15 = clickable(500, 530, 120, 120, 15)
        imgpos16 = clickable(620, 530, 120, 120, 16)

        moves = 0

        for i in range(16):
            name = "imgpos" + str(i + 1)
            ob = eval(name)
            clicklist.append(ob)

    def addmoves():
        bg = pygame.image.load("Shuffle_Items/Images/sh_top.png")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydis.blit(bg, (0, 0))
        textSurfaceObj = fontObj2.render("MOVES : " + str(moves), True, white)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 70)
        mydis.blit(textSurfaceObj, textRectObj)

    def randomise():
        nonlocal randlist
        k = random.randint(3, 10)
        l = random.randint(3, 5)
        l = l * 2 + 1

        randlist = []
        for i in range(16):
            k = k + l
            if k > 16:
                k = k - 16
            while k in randlist:
                k += 1
                if k > 16:
                    k = k - 16
            randlist.append(k)

    def initpage():
        nonlocal img
        bg = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydis.blit(bg, (0, 0))
        bg = pygame.image.load("Shuffle_Items/Images/sh_button.png")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydis.blit(bg, (0, 0))
        textSurfaceObj = fontObj2.render("EXIT", True, white)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (130, 300)
        mydis.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj2.render("RESET", True, white)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (130, 400)
        mydis.blit(textSurfaceObj, textRectObj)

        pygame.draw.rect(mydis, black, (620, 530, 120, 120))
        org = pygame.image.load("Shuffle_Items/Images/shuffle.jpg")
        org = pygame.transform.scale(org, (200, 200))
        mydis.blit(org, (770, 100))

        addmoves()
        cnt = 0
        for i in range(4):
            for j in range(4):
                x = 260 + 120 * j
                y = 170 + 120 * i
                mydis.blit(img[randlist[cnt] - 1], (x, y))
                cnt = cnt + 1
        for i in range(15):
            imglist[i] = img[randlist[i] - 1]
        pygame.draw.rect(mydis, black, (620, 530, 120, 120))

    def winner(a):
        but = mixer.Sound("Shuffle_Items/Sound/shuffle_winning.wav")
        but.play(0)
        nonlocal diag
        nonlocal dim
        nonlocal dial
        pygame.display.update()
        pygame.time.wait(2000)
        mydis.blit(dim, (0, 0))
        mydis.blit(dial, (0, 0))
        str1 = ''''You solved the puzzle...'''
        str2 = str(a + 1) + "moves"

        textSurfaceObj = fontObj3.render(str1, True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 300)
        mydis.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj2.render(str2, True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 360)
        mydis.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj3.render("RESTART", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (375, 445)
        mydis.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj3.render("Exit", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (625, 445)
        mydis.blit(textSurfaceObj, textRectObj)
        pygame.display.update()
        diag = 1

    def check():
        nonlocal moves
        nonlocal imglist
        nonlocal img
        flag = 0
        for i in range(15):
            if imglist[i] != 0 and imglist[i] != img[i]:
                flag = 1
                break
        if flag == 0:
            winner(moves)

    reset()
    while True:
        for event in pygame.event.get():
            mpos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if diag == 0:
                    if back_b.isover(mpos):
                        button = mixer.Sound("Shuffle_Items/Sound/shuffle_button.wav")
                        button.play()
                        import shuffle_menupage
                        shuffle_menupage.main()
                    if reset_b.isover(mpos):
                        button = mixer.Sound("Shuffle_Items/Sound/shuffle_button.wav")
                        button.play()
                        moves = 0
                        reset()

                    for i in clicklist:
                        if i.isover(mpos):
                            button = mixer.Sound("Shuffle_Items/Sound/shuffle_button.wav")
                            button.play()
                            pos = i.uid
                            if imglist[pos - 1] != 0:
                                top = pos - 4
                                bottom = pos + 4
                                if pos % 4 != 0:
                                    right = pos + 1
                                else:
                                    right = 18
                                if pos % 4 != 1:
                                    left = pos - 1
                                else:
                                    left = -1
                                if top > 0:
                                    if imglist[top - 1] == 0:
                                        mydis.blit(imglist[pos - 1],
                                                   (260 + (120 * ((top - 1) % 4)), 170 + (120 * ((top - 1) // 4))))
                                        imglist[top - 1] = imglist[pos - 1]
                                        imglist[pos - 1] = 0
                                        moves += 1
                                        addmoves()
                                        pygame.draw.rect(mydis, black, (
                                            260 + (120 * ((pos - 1) % 4)), 170 + (120 * ((pos - 1) // 4)), 120, 120))

                                if bottom < 17:
                                    if imglist[bottom - 1] == 0:
                                        mydis.blit(imglist[pos - 1], (
                                            260 + (120 * ((bottom - 1) % 4)), 170 + (120 * ((bottom - 1) // 4))))
                                        imglist[bottom - 1] = imglist[pos - 1]
                                        imglist[pos - 1] = 0
                                        moves += 1
                                        addmoves()
                                        pygame.draw.rect(mydis, black, (
                                            260 + (120 * ((pos - 1) % 4)), 170 + (120 * ((pos - 1) // 4)), 120, 120))
                                if left > 0:
                                    if imglist[left - 1] == 0:
                                        mydis.blit(imglist[pos - 1],
                                                   (260 + (120 * ((left - 1) % 4)), 170 + (120 * ((left - 1) // 4))))
                                        imglist[left - 1] = imglist[pos - 1]
                                        imglist[pos - 1] = 0
                                        moves += 1
                                        addmoves()
                                        pygame.draw.rect(mydis, black, (
                                            260 + (120 * ((pos - 1) % 4)), 170 + (120 * ((pos - 1) // 4)), 120, 120))
                                if right < 17:
                                    if imglist[right - 1] == 0:
                                        mydis.blit(imglist[pos - 1],
                                                   (260 + (120 * ((right - 1) % 4)), 170 + (120 * ((right - 1) // 4))))
                                        imglist[right - 1] = imglist[pos - 1]
                                        imglist[pos - 1] = 0
                                        moves += 1
                                        addmoves()
                                        pygame.draw.rect(mydis, black, (
                                            260 + (120 * ((pos - 1) % 4)), 170 + (120 * ((pos - 1) // 4)), 120, 120))
                            check()
                else:
                    if rest_b.isover(mpos):
                        button = mixer.Sound("Shuffle_Items/Sound/shuffle_button.wav")
                        button.play()
                        moves = 0
                        reset()
                    if bck_b.isover(mpos):
                        button = mixer.Sound("Shuffle_Items/Sound/shuffle_button.wav")
                        button.play()
                        import shuffle_menupage
                        shuffle_menupage.main()
                        diag = 0

        pygame.display.update()
        clock.tick(60)


shuffle()
