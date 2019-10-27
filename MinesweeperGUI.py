import pygame
import TileView

pygame.init()
clock = pygame.time.Clock()

crashed = False
menu_height = 50
board_height = 600
board_width = 600
width = board_width
height = menu_height + board_height

screen = pygame.display.set_mode((height, width))
screen.fill((200, 200, 200))
pygame.display.set_caption('MineSweeperV2.0')

# Initial board creation, using tiles from board and Button class


while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)


    pygame.display.update()

