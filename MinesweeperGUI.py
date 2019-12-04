import pygame
from typing import List
from Board import Board
from TileView import TileView
from BombTile import BombTile
import sys


class MinesweeperGUI:
    """
    MinesweeperGUI is the main class of the minesweeper project which handles
    the view and user inputs. The class also updates the view accordingly after
    each user input.

    == Attributes ==
    menu_height: The height of the menu bar for all the menu buttons
    board_height: The height of the game board
    board_width: The width of the window and game board
    row_size: The number of rows for the minesweeper game board
    col_size: The number of columns for the minesweeper game board
    bomb_number: The number of bombs on the board
    board: The minesweeper that handles game logic
    _button_board: The tile board the user sees on the board
    screen: The screen to draw and collect inputs from
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

    def __init__(self) -> None:
        self.menu_height = 50
        self.board_height = 600
        self.board_width = 600
        self._button_board = []
        self.col_size = 15
        self.row_size = 15
        self.bomb_number = 15
        width = self.board_width
        height = self.menu_height + self.board_height
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((200, 200, 200))
        pygame.display.set_caption('MineSweeperV2.0')

    def _create_board(self) -> None:
        """
        Creates the TileView and assembles them on the board according to the
        row and column size. The method also sets the position for the tile
        so it can be reused to update the board after every move.
        """
        size = self._get_tile_size()
        starting_x = int((self.board_width - (size[0]*self.col_size))/2)
        starting_y = int((self.board_height - (size[1]*self.row_size))/2) + self.menu_height
        position = [starting_x, starting_y]
        self.board = Board(self.row_size, self.col_size, self.bomb_number)
        self.board.create_board()
        # Makes each view tile and draws them on screen
        for row in range(self.row_size):
            self._button_board += [[]]
            for col in range(self.col_size):
                image = self.board.get_tile(row, col).get_tile_type()
                # Creating the tiles
                b = TileView(size, image, (row, col))
                b.draw(self.screen, position)
                position[0] += size[0]
                self._button_board[row] += [b]
            position[0] = starting_x
            position[1] += size[1]

    def _get_tile_size(self) -> tuple:
        """
        Calculates the size of the tiles based on the view width, height and
        row, column size.
        :return: The size of the tile in a tuple
        """
        row_length = int(self.board_width / self.row_size)
        col_length = int(self.board_height / self.col_size)
        size = (min(row_length, col_length), min(row_length, col_length))
        return size

    def _board_event_handler(self, event: pygame.event) -> None:
        """
        Takes the event input and performs the task for different types of
        events. It also updates the board right after.
        Also checks each button/tile and checks the position of the click with
        the button or tile.
        Left click: reveal tile, or perform button click event
        Right click: flag a tile or do nothing if its not a tile.
        :param event: Mouse click event.
        """
        for row in range(self.row_size):
            for col in range(self.col_size):
                if self._button_board[row][col].get_rect().collidepoint(
                        event.pos[0], event.pos[1]):
                    input = self._button_board[row][col].id
                    if event.button == 1:  # Left click
                        self.board.reveal(input[0], input[1])
                    elif event.button == 3:  # Right click
                        self.board.flag(input[0], input[1])
                    self.update()

    def update(self) -> None:
        """
        Clears and updates the screen with new tile updates and info.
        """
        self.screen.fill((200, 200, 200))
        # Goes through each tile and update them accordingly
        for row in range(self.row_size):
            for col in range(self.col_size):
                image = self.board.board[row][col].get_tile_type()
                self._button_board[row][col].update(self.screen, image)
                # Reveals the tiles that are left when the game is over
                # Only executes at the end of the game
                if self.board.is_game_over():
                    self.board.get_tile(row, col).reveal_tile()
                    if self.board.get_tile(row, col).is_flagged() and \
                            not (isinstance(self.board.get_tile(row, col), BombTile)):
                        self._button_board[row][col].update(self.screen, "wrongflag")
                    else:
                        image = self.board.board[row][col].get_tile_type()
                        self._button_board[row][col].update(self.screen, image)

    def start(self) -> None:
        """
        Starts the game loop that tracks the user input
         and updates board constantly.
        """
        crashed = False
        self._create_board()
        while not crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crashed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self._board_event_handler(event)

            pygame.display.update()


if __name__ == '__main__':
    """
    Handles the start of the game.
    """
    sys.setrecursionlimit(2000)
    application = MinesweeperGUI()
    application.start()
