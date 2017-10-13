import pygame

from game import Actor

SCREEN_W = 1280
SCREEN_H = 720
MAX_FPS = 120

C_BLACK = (0, 0, 0)

pygame.init()

Player = Actor.Actor(0, 0)

game_clock = pygame.time.Clock()
main_window = pygame.display.set_mode((SCREEN_W, SCREEN_H), pygame.DOUBLEBUF | pygame.RESIZABLE)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;

    main_window.fill(C_BLACK)

    # RENDER

    pygame.display.flip()
    game_clock.tick(MAX_FPS)


pygame.quit()