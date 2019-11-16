from __future__ import annotations
from typing import Tuple, List
from Tile import Tile


class EmptyTile(Tile):
    """
    The EmptyTile class extends the Tile class. It should has all attributes
    and methods of the Tile class.
    The process_left_click_tile is implemented based on the behavior of
    EmptyTile.
    """

    def __init__(self, board: List[List[Tile]], position: Tuple[int, int]):
        """
        Initialize the EmptyTile class with board and position like the
        Tile class.
        """
        super().__init__(self, board, position)
        # self._icon

    def process_left_click_tile(self) -> None:
        """
        Implement the process_left_click_tile method in the Tile class.
        EmptyTile is initially unrevealed. When it is clicked by the player,
        it reveals itself and all other EmptyTile around it unitile reaches
        NumberTile.

        """
        pass
