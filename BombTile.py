from __future__ import annotations
from typing import Tuple, List
from Tile import Tile


class BombTile(Tile):
    """
    The BombTile class extends the Tile class. It should has all attributes
    and methods of the Tile class.
    The reveal_tile is implemented based on the behavior of
    BombTile.
    """

    def __init__(self, board: List[List[Tile]], position: Tuple[int, int]):
        """
        Initialize the BombTile class with board and position like the
        Tile class.
        """
        super().__init__(board, position)
        # self._icon
        self._tile_type = "bomb"

    def _calculate_click(self) -> bool:
        return False

    def get_symbol(self) -> str:
        return " * "
