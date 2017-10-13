import pygame

import game

SCREEN_W = 1280
SCREEN_H = 720

pygame.init()

a = game.Actor()

current_time = pygame.time.Clock
main_window = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)

pygame.quit()