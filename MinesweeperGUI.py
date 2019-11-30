import pygame
from typing import List, Dict, Optional
from Board import Board
from TileView import TileView
from BombTile import BombTile
import sys


class MinesweeperGUI:
    """
        MinesweeperGUI class handles the game window and updating it.

        == Attributes ==

    """
    menu_height: int
    board_height: int
    board_width: int
    row_size: int
    col_size: int
    bomb_number: int
    board: Board
    _button_board: List[List[TileView]]
    screen: pygame.display

    def __init__(self):
        self.menu_height = 50
        self.board_height = 600
        self.board_width = 600
        self._button_board = []
        self.col_size = 40
        self.row_size = 40
        self.bomb_number = 84
        width = self.board_width
        height = self.menu_height + self.board_height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((200, 200, 200))
        pygame.display.set_caption('MineSweeperV2.0')

    def _create_board(self):
        size = self._get_tile_size()
        starting_x = int((self.board_width - (size[0]*self.col_size))/2)
        starting_y = int((self.board_height - (size[1]*self.row_size))/2) + self.menu_height
        position = [starting_x, starting_y]
        print(position)
        self.board = Board(self.row_size, self.col_size, self.bomb_number)
        self.board.create_board()
        for row in range(self.row_size):
            self._button_board += [[]]
            for col in range(self.col_size):
                # self.board.get_tile(row, col)._revealed = True
                image = self.board.get_tile(row, col).get_tile_type()
                # Creating the tiles
                b = TileView(size, image)
                b.set_tile_id((row, col))
                b.draw(self.screen, position)
                position[0] += size[0]
                self._button_board[row] += [b]
            position[0] = starting_x
            position[1] += size[1]

    def _get_tile_size(self):
        row_length = int(self.board_width / self.row_size)
        col_length = int(self.board_height / self.col_size)
        size = (min(row_length, col_length), min(row_length, col_length))
        return size

    def set_board_property(self):


    def _board_event_handler(self, event):
        for row in range(self.row_size):
            for col in range(self.col_size):
                if self._button_board[row][col].get_rect().collidepoint(
                        event.pos[0], event.pos[1]):
                    input = self._button_board[row][col].id
                    if event.button == 1:
                        self.board.reveal(input[0], input[1])
                    elif event.button == 3:
                        self.board.flag(input[0], input[1])
                    self.update()

    def update(self):
        self.screen.fill((200, 200, 200))
        for row in range(self.row_size):
            for col in range(self.col_size):
                image = self.board.board[row][col].get_tile_type()
                self._button_board[row][col].update(self.screen, image)
                if self.board.is_game_over():
                    self.board.get_tile(row, col).reveal_tile()
                    if self.board.get_tile(row, col).is_flagged() and \
                            not (isinstance(self.board.get_tile(row, col), BombTile)):
                        self._button_board[row][col].update(self.screen, "wrongflag")
                    else:
                        image = self.board.board[row][col].get_tile_type()
                        self._button_board[row][col].update(self.screen, image)

    def start(self):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._board_event_handler(event)
                    right = 2

            pygame.display.update()


if __name__ == '__main__':
    sys.setrecursionlimit(2000)
    application = MinesweeperGUI()
    application._create_board()
    application.start()
