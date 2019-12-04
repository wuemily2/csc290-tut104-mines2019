from __future__ import annotations
from typing import Tuple, List
from Tile import Tile
from NumberTile import NumberTile


class EmptyTile(Tile):
    """
    The EmptyTile class extends the Tile class. It should have
    all the attributes and methods of the Tile class.
    """

    def __init__(self, board: List[List[Tile]], position: Tuple[int, int]):
        """
        Initialize the EmptyTile class with board and position like the
        Tile class.
        """
        super().__init__(board, position)
        # self._icon
        self._tile_type = "empty"

    def _calculate_click(self):
        """
        Implement the reveal_tile method in the Tile class.
        EmptyTile is initially unrevealed. When it is clicked by the player,
        it reveals itself and all other EmptyTile and Numbered Tiles around it.
        """
        for x_shift in [-1, 0, 1]:
            for y_shift in [-1, 0, 1]:
                if x_shift == y_shift == 0:
                    continue
                try:
                    click_index = (self.get_position()[0] + x_shift,
                                   self.get_position()[1] + y_shift)
                    if click_index[0] < 0 or click_index[1] < 0:
                        continue
                    other_tile = self._board[click_index[0]][click_index[1]]
                    if isinstance(other_tile, EmptyTile) or \
                            isinstance(other_tile, NumberTile):
                        other_tile.reveal_tile()
                except IndexError:  # do nothing
                    pass
        return True

    def get_symbol(self) -> str:
        """
        Return the string representation of an empty tile.
        :return:
        """
        return " "
