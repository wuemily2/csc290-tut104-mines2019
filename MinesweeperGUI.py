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
    board: Board
    _button_board: List[List[TileView]]
    screen: pygame.display

    def __init__(self):
        self.menu_height = 50
        self.board_height = 600
        self.board_width = 600
        self._button_board = []
        self.board_size = 9
        self.bomb_number = 10
        width = self.board_width
        height = self.menu_height + self.board_height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((200, 200, 200))
        pygame.display.set_caption('MineSweeperV2.0')

    def _create_board(self):
        position = [0, 0]
        self.board = Board(self.board_size, self.board_size, self.bomb_number)
        self.board.create_board()
        for row in range(self.board_size):
            self._button_board += [[]]
            for col in range(self.board_size):
                image = self.board.get_tile(row, col).get_tile_type()
                size = (int(self.board_width / self.board_size),
                        int(self.board_height / self.board_size))
                b = TileView(size, image)
                b.set_tile_id((row, col))
                b.draw(self.screen, position)
                position[0] += int(self.board_width / self.board_size)
                self._button_board[row] += [b]
            position[0] = 0
            position[1] += int(self.board_height / self.board_size)

    def _board_event_handler(self, event):
        for row in range(self.board_size):
            for col in range(self.board_size):
                if self._button_board[row][col].get_rect().collidepoint(event.pos):
                    self.screen.fill((200, 200, 200))
                    input = self._button_board[row][col].id
                    print("row:" + str(input[0]))
                    print("col:" + str(input[1]))
                    self.board.reveal(input[1], input[0])
                    self.update()

    def update(self):
        for row in range(self.board_size):
            for col in range(self.board_size):
                image = self.board.get_tile(row, col).get_tile_type()
                self._button_board[row][col].update(self.screen, image)

    def start(self):
        crashed = False
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self._board_event_handler(event)
                    right = 2

            pygame.display.update()


if __name__ == '__main__':

    application = MinesweeperGUI()
    application._create_board()
    application.start()
