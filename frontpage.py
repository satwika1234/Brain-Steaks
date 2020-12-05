import pygame
import sys
from pygame import mixer

pygame.init()
clock = pygame.time.Clock()

mydis = pygame.display.set_mode((1000, 700), 0, 32)
headcolor = (255, 0, 50)
txtcolor = (255, 13, 0)
btncolor = (240, 240, 240)
black = (0, 0, 0)
pygame.display.set_caption('Brain Steaks')


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


def mainpage():
    mixer.music.load('main_background.mp3')
    mixer.music.play(-1)
    bg = pygame.image.load("mainbg.png")
    bg = pygame.transform.scale(bg, (1000, 700))
    mydis.blit(bg, (0, 0))
    sudoku_b = clickable(430, 240, 140, 120, 0)
    xox_b = clickable(430, 520, 140, 120, 0)
    shuffle_b = clickable(590, 240, 140, 120, 0)
    chess_b = clickable(590, 380, 140, 120, 0)
    pair_b = clickable(270, 380, 140, 120, 0)
    snake_b = clickable(270, 520, 140, 120, 0)
    about_b = clickable(750, 600, 200, 70, 0)

    font1 = pygame.font.Font("freesansbold.ttf", 50)
    paper = font1.render("Brain Steaks", True, headcolor)
    textrect = paper.get_rect()
    textrect.center = (500, 140)
    mydis.blit(paper, textrect)

    font2 = pygame.font.Font("freesansbold.ttf", 30)
    gtext1 = font2.render("sudoku", True, txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (500, 300)
    mydis.blit(gtext1, textrect)

    gtext1 = font2.render("Shuffle", True, txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (660, 300)
    mydis.blit(gtext1, textrect)

    gtext1 = font2.render("Pair", True, txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (340, 440)
    mydis.blit(gtext1, textrect)

    gtext1 = font2.render("Chess", True, txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (660, 440)
    mydis.blit(gtext1, textrect)

    gtext1 = font2.render("S & L", True, txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (340, 580)
    mydis.blit(gtext1, textrect)

    gtext1 = font2.render("XOX", True, txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (500, 580)
    mydis.blit(gtext1, textrect)

    gtext1 = font2.render("About", True, txtcolor)
    textrect = gtext1.get_rect()
    textrect.center = (850, 635)
    mydis.blit(gtext1, textrect)

    while True:
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                button = mixer.Sound("button.wav")
                button.play()

                if sudoku_b.isover(pos):
                    import sudoku_menupage
                    sudoku_menupage.main()

                if xox_b.isover(pos):
                    import xox_menupage
                    xox_menupage.main()

                if shuffle_b.isover(pos):
                    import shuffle_menupage
                    shuffle_menupage.main()

                if chess_b.isover(pos):
                    import chess_menupage
                    chess_menupage.main()

                if pair_b.isover(pos):
                    import findpair_menupage
                    findpair_menupage.main()

                if snake_b.isover(pos):
                    import SandL_menupage
                    SandL_menupage.main()

                if about_b.isover(pos):
                    about()

        pygame.display.update()
        clock.tick(60)


def about():
    import credits
    credits.credit()


mainpage()
