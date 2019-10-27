from __future__ import annotations
from Board import Board
from typing import Tuple


class Tile:
    # This class may extend a PyGame Button class in the future, depending on
    # the implementation
    """ A Tile class. This is used to represent a tile inside the grid
        in a Minesweeper game.

        This is an abstract class that should not be instantiated directly.
        This class is extended by BombTile, EmptyTile and NumberTile classes.

        #TODO Reorganize attributes, functions, and documentation as needed

        === Public Attributes ===

        === Private Attributes ===
        _board:
            Stores the board that the Tile is in.
        _icon:
            Stores the appearance of any icon on the tile. Stores None if empty.
        _pos:
            Stores the position of the Tile in (x, y) format.
        _flagged:
            Stores a boolean indicating whether the Tile is flagged.
        _revealed:
            Stores whether the Tile's contents are revealed on the board.
            For example, the tile may be clicked to reveal a number,
            bomb, or empty space.

        === Representation Invariants ===
            -_flagged and _revealed cannot store the same boolean value
            -_pos must contain values only within the game grid's range
        """
    _board: Board
    # _icon: #TODO decide the type of _icon
    _pos: Tuple[int, int]
    _flagged: bool
    _revealed: bool

    def __init__(self, board: Board, position: Tuple[int, int]):
        """
        Initialize the tile with <board> and <position>. Initially, _flagged
        and _revealed are set to False, as the player has not clicked or flagged
        any of the Tiles.
        Precondition: The constructor is called only when #TODO complete doc
        :param: board - the Board that this Tile is stored in.
        :param: position - the location of the Tile in the Board
        """
        self._board = board
        self._icon = None
        self._pos = position
        self._flagged = self._revealed = False
        # TODO: Modify if necessary

    def process_left_click_tile(self) -> None:
        """
        Update the Board state based on the type of tile clicked.
        This is an abstract method.
        Precondition:
           Method is called only when the player
           left-clicks the tile at _pos in the game grid.
           The tile cannot be flagged.
        """
        raise NotImplementedError

    def flag_tile(self) -> None:
        """
        Update the Tile _icon to a flag icon, as well as the game board's view.
        Preconditions:
        _revealed must be False
        Called only by a right-click.
        """
        self._flag()
        # self._icon = #TODO set the correct icon
        # TODO: implement game board's view updating.

    def _flag(self) -> None:
        """
        Changes the boolean value stored in _flagged.
        Precondition: _revealed is False
        """
        self._flagged = not self._flagged

    def get_position(self) -> Tuple[int, int]:
        """
        :return: The position of the Tile
        """
        return self._pos
