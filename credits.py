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


def credit():
    img = pygame.image.load("credits.png")
    back = pygame.transform.scale(img, (1000, 700))
    mydis.blit(back, (0, 0))
    img = pygame.image.load("logo.png")
    logo = pygame.transform.scale(img, (300, 200))
    mydis.blit(logo, (350, 450))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            b_btn = clickable(0, 0, 120, 60)
            pos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b_btn.isover(pos):
                    import frontpage
                    frontpage.mainpage()

        pygame.display.update()


credit()
