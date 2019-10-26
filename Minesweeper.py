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
        update the PyGame display given the events.
        """
        #TODO
        pass

    def report_game_won(self) -> bool:
        """
        return true iff game has been won.
        """
        #TODO
        pass

    def restart(self) -> None:
        """
        restart teh Minesweeper game.
        """
        #TODO
        pass

    def game_loop(self) -> None:
        """
        continue the game loop.
        """
        #TODO
        pass





