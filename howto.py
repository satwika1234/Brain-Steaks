import pygame
import sys

pygame.init()
mydis = pygame.display.set_mode((1000, 700))


class clickable:
    def __init__(self, startx, starty, w, h):
        self.startx = startx
        self.starty = starty
        self.w = w
        self.h = h

    def isover(self, pos):
        if pos[0] > self.startx and pos[0] < self.startx + self.w:
            if pos[1] > self.starty and pos[1] < self.starty + self.h:
                return True
            else:
                return False
        else:
            return False


def howtopair():
    img = pygame.image.load("howtoboxpair.png")
    back = pygame.transform.scale(img, (1000, 700))
    mydis.blit(back, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            b_btn = clickable(0, 0, 120, 60)
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_btn.isover(pos):
                    import findpair_menupage
                    findpair_menupage.main()

        pygame.display.update()


def howtoshuffle():
    img = pygame.image.load("howtoboxshuffle.png")
    back = pygame.transform.scale(img, (1000, 700))
    mydis.blit(back, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            b_btn = clickable(0, 0, 120, 60)
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_btn.isover(pos):
                    import shuffle_menupage
                    shuffle_menupage.main()

        pygame.display.update()


def howtosandl():
    img = pygame.image.load("howtoboxsl.png")
    back = pygame.transform.scale(img, (1000, 700))
    mydis.blit(back, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            b_btn = clickable(0, 0, 120, 60)
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_btn.isover(pos):
                    import SandL_menupage
                    SandL_menupage.main()

        pygame.display.update()


def howtosudoku():
    img = pygame.image.load("howtoboxsudoku.png")
    back = pygame.transform.scale(img, (1000, 700))
    mydis.blit(back, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            b_btn = clickable(0, 0, 120, 60)
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_btn.isover(pos):
                    import sudoku_menupage
                    sudoku_menupage.main()

        pygame.display.update()


def howtoxox():
    img = pygame.image.load("howtoboxxox.png")
    back = pygame.transform.scale(img, (1000, 700))
    mydis.blit(back, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            b_btn = clickable(0, 0, 120, 60)
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_btn.isover(pos):
                    import xox_menupage
                    xox_menupage.main()

        pygame.display.update()


def howtochess():
    img = pygame.image.load("howtochess.png")
    back = pygame.transform.scale(img, (1000, 700))
    mydis.blit(back, (0, 0))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            b_btn = clickable(0, 0, 120, 60)
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_btn.isover(pos):
                    import chess_menupage
                    chess_menupage.main()

        pygame.display.update()
