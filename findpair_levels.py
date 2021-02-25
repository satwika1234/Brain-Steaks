import pygame
import sys
from pygame.locals import *
from pygame import mixer

clock = pygame.time.Clock()

pygame.init()
mydis = pygame.display.set_mode((1000, 700), 0, 32)

pygame.display.set_caption('FIND PAIR LEVELS')
font = pygame.font.SysFont('freesansbold.ttf', 80)
font1 = pygame.font.SysFont('freesansbold.ttf', 40)


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def levels():
    click = False

    while True:
        bg = pygame.image.load("blackbg.jpg")
        bg = pygame.transform.scale(bg, (1000, 700))
        mydis.blit(bg, (0, 0))
        draw_text('Levels', font, (255, 0, 255), mydis, 415, 300)
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(410, 375, 200, 50)
        button_2 = pygame.Rect(410, 450, 200, 50)
        button_3 = pygame.Rect(410, 525, 200, 50)
        button_4 = pygame.Rect(0, 0, 75, 45)

        if button_1.collidepoint((mx, my)):
            if click:
                button = mixer.Sound("FindPair_Items/Sound/button.wav")
                button.play()
                import findpair_easy
                findpair_easy.pair_easy()

        if button_2.collidepoint((mx, my)):
            if click:
                button = mixer.Sound("FindPair_Items/Sound/button.wav")
                button.play()
                import findpair_medium
                findpair_medium.pair_medium()

        if button_3.collidepoint((mx, my)):
            if click:
                button = mixer.Sound("FindPair_Items/Sound/button.wav")
                button.play()
                import findpair_hard
                findpair_hard.pair_hard()

        if button_4.collidepoint((mx, my)):
            if click:
                button = mixer.Sound("FindPair_Items/Sound/button.wav")
                button.play()
                import findpair_menupage
                findpair_menupage.main()

        pygame.draw.rect(mydis, (0, 17, 240), button_1)
        draw_text('Easy', font1, (255, 255, 255), mydis, 480, 385)

        pygame.draw.rect(mydis, (0, 17, 240), button_2)
        draw_text('Medium', font1, (255, 255, 255), mydis, 460, 460)

        pygame.draw.rect(mydis, (0, 17, 240), button_3)
        draw_text('Hard', font1, (255, 255, 255), mydis, 480, 535)

        pygame.draw.rect(mydis, (0, 17, 240), button_4)
        draw_text('Back', font1, (255, 255, 255), mydis, 5, 10)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            pygame.display.update()
            clock.tick(60)


levels()
