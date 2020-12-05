import pygame
import sys
from pygame.locals import *
from pygame import mixer

clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('FIND PAIR MENU')
mydis = pygame.display.set_mode((1000, 700), 0, 32)
font = pygame.font.SysFont('freesansbold.ttf', 80)
font1 = pygame.font.SysFont('freesansbold.ttf', 40)


def main():
    def credits():
        import credits
        credits.credit()

    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)

    def main_menu():
        click = False

        while True:
            bg = pygame.image.load("blackbg.jpg")
            bg = pygame.transform.scale(bg, (1000, 700))
            mydis.blit(bg, (0, 0))
            draw_text('Main Menu', font, (255, 0, 255), mydis, 370, 300)
            mx, my = pygame.mouse.get_pos()
            button_1 = pygame.Rect(410, 375, 200, 50)
            button_2 = pygame.Rect(410, 450, 200, 50)
            button_3 = pygame.Rect(410, 525, 200, 50)
            button_4 = pygame.Rect(0, 0, 75, 45)
            if button_1.collidepoint((mx, my)):
                if click:
                    button = mixer.Sound("button.wav")
                    button.play()
                    import findpair_levels
                    findpair_levels.levels()
            if button_2.collidepoint((mx, my)):
                if click:
                    button = mixer.Sound("button.wav")
                    button.play()
                    import howto
                    howto.howtopair()
            if button_3.collidepoint((mx, my)):
                if click:
                    button = mixer.Sound("button.wav")
                    button.play()
                    credits()
            if button_4.collidepoint((mx, my)):
                if click:
                    button = mixer.Sound("button.wav")
                    button.play()
                    import frontpage
                    frontpage.mainpage()

            pygame.draw.rect(mydis, (0, 17, 240), button_1)
            draw_text('Start Game', font1, (255, 255, 255), mydis, 440, 385)

            pygame.draw.rect(mydis, (0, 17, 240), button_2)
            draw_text('How to play', font1, (255, 255, 255), mydis, 440, 460)

            pygame.draw.rect(mydis, (0, 17, 240), button_3)
            draw_text('Credits', font1, (255, 255, 255), mydis, 440, 535)

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

    main_menu()


main()
