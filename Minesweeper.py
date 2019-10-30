import pygame
import Board
import Tile


class Minesweeper:
    """
    A Minesweeper Game.

    === Instance Attributes ===

    === Private Attributes ===

    === Representation Invariants ===
    """
    def __init__(self, board: Board):
        """
        Initialize this Minesweeper game.

        Preconditions:
        """
        self.board = board
        self.window = None
        self.buttons = []
        #TODO
        pass

    def update_display(self) -> None:
        """
        update the PyGame display given the events of Tiles.
        """
        #TODO
        pass

    def report_game_won(self) -> bool:
        """
        return true iff game has been won.
        """
        #Return true if all flag coordinates and bomb coordinates are equal
        #Certain variable names have artitrary name until further development of game
        count = num_bombs
        for row in range(len(board)):
            for col in range(len(row)):
                if board[row][col] == BombTile and board[row][col]._flagged:
                    count += 1
        return count == num_bombs


    def restart(self) -> None:
        """
        restart the Minesweeper game.
        """
        #TODO
        pass

    def game_loop(self) -> None:
        """
        checks board for an event, sends and receives data from board and
        is used to update the board
        """
        #TODO
        pass





