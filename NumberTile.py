from __future__ import annotations
from typing import Tuple
import Board
from Tile import Tile

class NumberTile(Tile):
    """
    The NumberTile class extends the Tile class. It should has all attributes
    and methods of the Tile class.
    Each NumberTile has an attribute number which presents the number of
    bombs around it. The range of the number is 1 to 8.
    The process_left_click_tile is implemented based on the behavior of
    NumberTile.
    """
    _number: int
    def __init__(self, board: Board, position: Tuple[int, int], number: int):
        """
        Initialize the NumberTile class with board and position like the
        Tile class.
        Precondition: 1 <= number <= 8
        """
        super().__init__(self, board, position)
        self._number = number

    def process_left_click_tile(self) -> None:
        """
        Implement the process_left_click_tile method in the Tile class.
        NumberTile is initially unrevealed. When it is clicked by the player,
        it reveals itself, showing the number of BombTile around it self.

        """
        pass
