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
        super().__init__(board, position)
        # self._icon
        self._tile_type = "EmptyTile"

    def _calculate_click(self):
        """
        Implement the process_left_click_tile method in the Tile class.
        EmptyTile is initially unrevealed. When it is clicked by the player,
        it reveals itself and all other EmptyTile and Numbered Tiles around it.
        """
        # print(self._tile_type + str(self.get_position()))
        for x_shift in [-1, 0, 1]:
            for y_shift in [-1, 0, 1]:
                # print("x: " + str(x_shift) + " y: " + str(y_shift))
                if x_shift == y_shift == 0:
                    continue  # Skip this loop iteration
                try:
                    click_index = (self.get_position()[0] + x_shift,
                                   self.get_position()[1] + y_shift)
                    if click_index[0] < 0 or click_index[1] < 0:
                        # Account for annoying negative indexing
                        continue  # skip loop
                    other_tile = self._board[click_index[0]][click_index[1]]
                    other_tile_type = other_tile.get_tile_type()
                    if other_tile_type in ["EmptyTile", "NumberTile"]:
                        # print("other_tile_type found! proceed to click: "
                        # + other_tile_type)
                        other_tile.process_left_click_tile()
                except IndexError:  # do nothing
                    pass
        return True

    def get_symbol(self) -> str:
        return " "
