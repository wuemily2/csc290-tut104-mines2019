import pygame
from typing import List, Dict, Optional
from Board import Board
from TileView import TileView


class MinesweeperGUI:
    """
        MinesweeperGUI class handles the game window and updating it.

        == Attributes ==

    """
    menu_height: int
    board_height: int
    board_width: int
    board_size: int
    bomb_number: int
    _button_board: List[List[TileView]]

    def __int__(self):
        self.menu_height = 50
        self.board_height = 600
        self.board_width = 600
        self._button_board = []
        self.board_size = 9
        self.bomb_number = 10
        width = self.board_width
        height = self.menu_height + self.board_height
        pygame.init()
        screen = pygame.display.set_mode((height, width))
        screen.fill((200, 200, 200))
        pygame.display.set_caption('MineSweeperV2.0')

    def _create_board(self):
        board = Board(self.board_size, self.board_size, self.bomb_number)
        board.create_board()
        for row in range(self.board_size):
            self._button_board += []
            for col in range(self.board_size):
                image = board.get_tile(row, col).get_tile_type()
                size = (self.board_width / self.board_size,
                        self.board_height / self.board_size)
                b = TileView(size, image)
                self._button_board[row] += [b]

    def _board_event_handler(self):

        for row in range(len(self.board())):
            for col in range(len(self.board())):
                if _button[row][col].collidepoint(event.pos):
                    pass

    def start(self):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._board_event_handler()

            pygame.display.update()


if __name__ == '__main__':

    application = MinesweeperGUI()
    print(application.board_size)
# application._create_board()
