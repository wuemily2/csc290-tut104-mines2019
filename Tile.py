from __future__ import annotations
from typing import Tuple, List


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
        _pos:
            Stores the position of the Tile in (x, y) format.
        _flagged:
            Stores a boolean indicating whether the Tile is flagged.
        _revealed:
            Stores whether the Tile's contents are revealed on the board.
            For example, the tile may be clicked to reveal a number,
            bomb, or empty space.
        _tile_type:
            Stores the string representation of this type of tile

        === Representation Invariants ===
            -_flagged and _revealed cannot store the same boolean value
            -_pos must contain values only within the game grid's range
        """
    _board: List[List[Tile]]
    # _icon: #TODO decide the type of _icon
    _pos: Tuple[int, int]
    _flagged: bool
    _revealed: bool
    _tile_type: str

    def __init__(self, board: List[List[Tile]], position: Tuple[int, int]):
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
        self._tile_type = "Tile"
        # TODO: Modify if necessary

    def reveal_tile(self) -> bool:
        """
        Update the Board state based on the type of tile clicked.
        This is an abstract method.
        Precondition:
           Method is called only when the player
           left-clicks the tile at _pos in the game grid.
           The tile cannot be flagged.
        Post condition:
            return true if the game doesn't end after this click
            otherwise, return false
        """
        if self._revealed is True or self._flagged is True:
            # Do nothing if revealed or flagged
            return True
        else:
            self._reveal()
        return self._calculate_click()

    def _calculate_click(self) -> bool:
        """
        This method is only called by reveal_tile.
        This defines the behaviour of a tile
        when the tile is clicked and revealed.
        Different tiles have different behaviour.
        For example, empty tiles reveal the surrounding
        empty and numbered tiles.

        returns false if it is a bomb tile. returns true otherwise
        """
        raise NotImplementedError

    def flag_tile(self) -> bool:
        """
        If the tile is not revealed, then change the flagged state of this tile.
        Preconditions:
            _revealed must be False, and the function is
            called only by a right-click.
        Post conditions:
            return whether flagging action is successful
        """
        if self._revealed is False:
            self._flag()
            return True
        return False

    def _flag(self) -> None:
        """
        Changes the boolean value stored in _flagged.

        """
        self._flagged = not self._flagged

    def is_flagged(self):
        """
        Return whether the tile is flagged.
        :return: The value stored in _flagged.
        """
        return self._flagged

    def get_position(self) -> Tuple[int, int]:
        """
        Gets the position of the tile.
        :return: The position of the Tile in the form of (row, col)
        """
        return self._pos

    def get_tile_type(self) -> str:
        """
        Return "flag" if the tile is flagged. Otherwise, return "closed" if the
        tile has not been clicked. If it has been clicked, return the type of
        this tile.
        :return: A string representation of the tile's state. This is either
        "flag", "closed", or the stored _tile_type.
        """
        if self.is_flagged():
            return "flag"
        elif not (self.is_revealed()):
            return "closed"
        else:
            return self._tile_type

    def is_same_type(self, other: Tile) -> bool:
        """
        :param other: A Tile object
        :return: Whether both this object and the
        other tile object are the same.
        """
        return self.get_tile_type() == other.get_tile_type()

    def _reveal(self) -> None:
        """
        Reveals the tile.
        """
        self._revealed = True

    def is_revealed(self) -> bool:
        """
        :return: A boolean. True if this tile is revealed, otherwise false.
        """
        return self._revealed

    def to_string(self) -> str:
        """
        :return: A String representation of this Tile.
        """
        if not self.is_revealed():
            if self.is_flagged():
                return "[F]"
            else:
                return "[|]"
        return "[" + self.get_symbol() + "]"

    def get_symbol(self) -> str:
        """
        :return: A String representation of the contents of this tile.
        """
        raise NotImplementedError
