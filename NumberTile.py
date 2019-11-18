from __future__ import annotations
from typing import Tuple, List
from Tile import Tile


class NumberTile(Tile):
    """
    The NumberTile class extends the Tile class. It should has all attributes
    and methods of the Tile class.
    Each NumberTile has an attribute number which presents the number of
    bombs around it. The range of the number is 1 to 8.
    The reveal_tile is implemented based on the behavior of
    NumberTile.
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
        # self._icon
        self._number = number
        self._tile_type = f"{number}"

    def get_tile_type(self) -> str:
        if not (self.is_revealed()):
            return "closed"
        elif self.is_flagged():
            return "flag"
        else:
            return self._tile_type

    def _calculate_click(self) -> bool:
        return True

    def get_symbol(self) -> str:
        return self.get_tile_type()
