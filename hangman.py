import pygame
import random
import sys
pygame.init()
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
done = False

alfabet='aąbcćdeęfghijklłmnoópqrsśtuwvzźż'

font = pygame.font.SysFont("comicsansms", 72)
button = pygame.Rect(100, 100, 50, 50)
button.x = 295
button.y = 310

counter = 0

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position

                # checks if mouse position is over the button

                if button.collidepoint(mouse_pos):
                    # prints current location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))

    screen.fill((255, 255, 255))
    text = font.render(alfabet[counter], True, (0, 128, 0))
    screen.blit(text,
        (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.draw.rect(screen, [255, 0, 0], button)

    pygame.display.flip()
    clock.tick(0.75)
    counter=counter+1
    if counter == len(alfabet):
        counter = 0
