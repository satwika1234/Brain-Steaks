import pygame
import sys
import random
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()

mydis = pygame.display.set_mode((1000, 700))
black = (0, 0, 0)
white = (255, 255, 255)
erase = (200, 0, 255)
fontObj1 = pygame.font.Font('freesansbold.ttf', 70)
fontObj2 = pygame.font.Font('freesansbold.ttf', 50)
fontObj3 = pygame.font.Font('freesansbold.ttf', 40)
pygame.display.set_caption("FIND PAIR EASY BY BRAIN STEAKS")


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


def pair_easy():
    mixer.music.load('FindPair_Items/Sound/pair_background.mp3')
    mixer.music.play(-1)

    img = pygame.image.load("blackbg.jpg")
    bgo = pygame.transform.scale(img, (1000, 700))
    mydis.blit(bgo, (0, 0))
    img = pygame.image.load("FindPair_Items/Images/pairbg.png")
    bg = pygame.transform.scale(img, (1000, 700))
    mydis.blit(bg, (0, 0))

    cback = pygame.image.load("FindPair_Items/Images/cardback.png")
    cback = pygame.transform.scale(cback, (135, 170))

    img = pygame.image.load("FindPair_Items/Images/paircut.png")
    cut = pygame.transform.scale(img, (1000, 700))

    img = pygame.image.load("FindPair_Items/Images/dim.png")
    dim = pygame.transform.scale(img, (1000, 700))

    img = pygame.image.load("FindPair_Items/Images/dialog.png")
    dial = pygame.transform.scale(img, (1000, 700))

    textSurfaceObj = fontObj2.render("LIVES", True, black)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (835, 130)
    mydis.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj2.render("12", True, black)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (835, 245)
    mydis.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj1.render("BACK", True, black)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (835, 470)
    mydis.blit(textSurfaceObj, textRectObj)

    textSurfaceObj = fontObj1.render("RESET", True, black)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (835, 610)
    mydis.blit(textSurfaceObj, textRectObj)

    back_b = clickable(705, 420, 260, 100, 50)
    reset_b = clickable(705, 560, 260, 100, 50)
    rest_b = clickable(280, 420, 190, 50, 20)
    bck_b = clickable(530, 420, 190, 50, 20)

    active = 0
    c_left = 12
    diag = 0

    cards = []
    selected = []

    for i in range(3):
        for j in range(4):
            x = 45 + j * 155
            y = 105 + i * 190
            mydis.blit(cback, (x, y))
            c = clickable(x, y, 135, 170, 4 * i + j)
            cards.append(c)

    randlist = []

    def randomise():
        nonlocal randlist
        k = random.randint(1, 11)
        l = random.randint(3, 5)
        l = l * 2 + 1

        randlist = []
        for i in range(12):
            k = k + l
            if k > 12:
                k = k - 12
            while k in randlist:
                k += 5
                if k > 12:
                    k = k - 12
            randlist.append(k)

    randomise()

    curr_img = None
    curr_num = None

    img = pygame.image.load("FindPair_Items/Images/pair1.png")
    img1 = pygame.transform.scale(img, (135, 170))

    img = pygame.image.load("FindPair_Items/Images/pair2.png")
    img2 = pygame.transform.scale(img, (135, 170))

    img = pygame.image.load("FindPair_Items/Images/pair3.jpg")
    img3 = pygame.transform.scale(img, (135, 170))

    img = pygame.image.load("FindPair_Items/Images/pair4.jpg")
    img4 = pygame.transform.scale(img, (135, 170))

    img = pygame.image.load("FindPair_Items/Images/pair5.png")
    img5 = pygame.transform.scale(img, (135, 170))

    img = pygame.image.load("FindPair_Items/Images/pair6.jpg")
    img6 = pygame.transform.scale(img, (135, 170))

    def flip(n):
        nonlocal active
        nonlocal img1
        nonlocal img2
        nonlocal img3
        nonlocal img4
        nonlocal img5
        nonlocal img6
        nonlocal curr_img
        nonlocal curr_num
        x = n % 4
        y = n // 4
        x = 45 + x * 155
        y = 105 + y * 190
        img_id = (randlist[n] + 1) // 2
        im = "img" + str(img_id)
        im = eval(im)
        mydis.blit(im, (x, y))
        if active == 1:
            pygame.display.update()
            pygame.time.wait(500)
            check(im, n)
        else:
            curr_img = im
            curr_num = n
            selected.append(n)
            active = 1

    def reset():
        mixer.music.load('FindPair_Items/Sound/pair_background.mp3')
        mixer.music.play()
        nonlocal c_left
        nonlocal selected
        nonlocal active
        mydis.blit(bgo, (0, 0))
        mydis.blit(bg, (0, 0))
        c_left = 12
        selected = []
        randomise()
        for i in range(3):
            for j in range(4):
                x = 45 + j * 155
                y = 105 + i * 190
                mydis.blit(cback, (x, y))

        textSurfaceObj = fontObj2.render("LIVES", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (835, 130)
        mydis.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj2.render("12", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (835, 245)
        mydis.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj1.render("BACK", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (835, 470)
        mydis.blit(textSurfaceObj, textRectObj)

        textSurfaceObj = fontObj1.render("RESET", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (835, 610)
        mydis.blit(textSurfaceObj, textRectObj)
        active = 0

    def show_win():
        mixer.music.stop()
        button = mixer.Sound("FindPair_Items/Sound/pair_winning.wav")
        button.play()
        nonlocal diag
        mydis.blit(dim, (0, 0))
        mydis.blit(dial, (0, 0))
        textSurfaceObj = fontObj2.render("LEVEL COMPLETE", True, black)
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

    def show_loss():
        mixer.music.stop()
        mixer.music.load('FindPair_Items/Sound/pair_loosing.mp3')
        mixer.music.play()

        nonlocal diag
        mydis.blit(dim, (0, 0))
        mydis.blit(dial, (0, 0))
        textSurfaceObj = fontObj2.render("GAME OVER", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (500, 300)
        mydis.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj3.render("RETRY", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (375, 445)
        mydis.blit(textSurfaceObj, textRectObj)
        textSurfaceObj = fontObj3.render("BACK", True, black)
        textRectObj = textSurfaceObj.get_rect()
        textRectObj.center = (625, 445)
        mydis.blit(textSurfaceObj, textRectObj)
        pygame.display.update()
        diag = 1

    def check(ob, m):
        nonlocal curr_img
        nonlocal curr_num
        nonlocal cback
        nonlocal active
        nonlocal c_left
        if ob == curr_img:
            selected.append(m)
            if len(selected) == 12:
                show_win()
        else:
            x = m % 4
            y = m // 4
            x = 45 + x * 155
            y = 105 + y * 190
            mydis.blit(cback, (x, y))
            x = curr_num % 4
            y = curr_num // 4
            x = 45 + x * 155
            y = 105 + y * 190
            mydis.blit(cback, (x, y))
            selected.pop()

            c_left -= 1
            mydis.blit(cut, (0, 0))

            textSurfaceObj = fontObj2.render(str(c_left), True, black)
            textRectObj = textSurfaceObj.get_rect()
            textRectObj.center = (835, 245)
            mydis.blit(textSurfaceObj, textRectObj)

            if c_left == 0:
                show_loss()

        active = 0

    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if diag == 0:
                    for i in cards:
                        button = mixer.Sound("FindPair_Items/Sound/button.wav")
                        button.play()
                        if i.isover(pos) and i.uid not in selected:
                            flip(i.uid)

                    if back_b.isover(pos):
                        button = mixer.Sound("FindPair_Items/Sound/button.wav")
                        button.play()
                        import findpair_levels
                        findpair_levels.levels()
                    if reset_b.isover(pos):
                        button = mixer.Sound("FindPair_Items/Sound/button.wav")
                        button.play()
                        reset()

                if diag == 1:
                    if rest_b.isover(pos):
                        button = mixer.Sound("FindPair_Items/Sound/button.wav")
                        button.play()
                        reset()
                        diag = 0
                    if bck_b.isover(pos):
                        button = mixer.Sound("FindPair_Items/Sound/button.wav")
                        button.play()
                        import findpair_levels
                        findpair_levels.levels()
                        diag = 0

        pygame.display.update()
        clock.tick(60)


pair_easy()
