import pygame

pygame.init()

surface = pygame.display.set_mode((1024,768))

pygame.display.set_caption('Tims Helicopter Game')

clock = pygame.time.Clock()

game_over = False

while not game_over
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    pygame.display.update()
