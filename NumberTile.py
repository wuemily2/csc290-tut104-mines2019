from __future__ import annotations
from typing import Tuple, List
from Tile import Tile


class NumberTile(Tile):
    """
    The NumberTile class extends the Tile class. It should have all attributes
    and methods of the Tile class.
    Each NumberTile has an attribute number which presents the number of
    bombs around it. The range of the number is 1 to 8.
    The symbol representation of this tile is a number from 1 to 8.
    """
    _number: int

    def __init__(self, board: List[List[Tile]], position: Tuple[int, int],
                 number: int):
        """
        Initialize the NumberTile class with board and position like the
        Tile class.
        Precondition: 1 <= number <= 8
        """
        super().__init__(board, position)
        self._number = number
        self._tile_type = f"{number}"

    def _calculate_click(self) -> bool:
        """
        Defines the behaviour of a NumberTile when it is clicked.
        This function simply returns True, and otherwise does nothing.
        :return: True
        """
        return True

    def get_symbol(self) -> str:
        return self.get_tile_type()
