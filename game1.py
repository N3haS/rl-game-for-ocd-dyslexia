import pygame
import sys
from makeitrain import rain_dys
from breakout2 import brek
from fifteen import fif

pygame.init()

window_w = 800
window_h = 600
bagcol = (255, 255, 255)
clcpos = [(100, 100), 
		  (250, 350), 
		  (460, 262)]
gamewin_si = (400, 300)
gamewin_clr = (200, 200, 200)

def display_initial_window(screen):
    screen.fill(bagcol)
    background_img = pygame.transform.scale(pygame.image.load('C:\\Users\\DELL\\PycharmProjects\\synapse\\livingggr.jpg').convert_alpha(), (800,600))

    screen.blit(background_img, (0, 0))
    for pos in clcpos:
        pygame.draw.circle(screen, (0, 0, 0), pos, 5)
    pygame.display.update()

def main():
    screen = pygame.display.set_mode((window_w, window_h))
    pygame.display.set_caption('Game Selector')

    display_initial_window(screen)

    game_functions = {
        (100, 100): rain_dys,
        (250, 350): fif,
        (400, 200): brek
    }

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for pos, func in game_functions.items():
                        if pygame.Rect(pos[0] - 5, pos[1] - 5, 10, 10).collidepoint(event.pos):
                            func()

    pygame.quit()
    sys.exit()

if _name_ == '_main_':
    main()
