from __future__ import annotations
from typing import List, Dict, Optional
import Tile, EmptyTile, BombTile, NumberTile
from random import randint


class Board:
    """Holds the board and handles edits on the board

    == Public Attributes ==
    board: holds the board with all the tiles

    == Private Attributes ==
    _row_size: the number of rows in the board
    _col_size: the number of columns in the board
    _num_bombs: the number of bombs to be placed when creating the board

    === Representation Invariants ===


    """
    _row_size: int
    _col_size: int
    _num_bombs: int
    board: List[List[Tile]]

    def __init__(self, row_size: int = 9, col_size: int = 9,
                 num_bombs: int = 10) -> None:

        self._row_size = row_size
        self._col_size = col_size
        self._num_bombs = num_bombs

        self.board = self.create_board()
        # self.set_numbered_tiles()

    def create_board(self) -> List[List[Tile]]:
        """
        Creates the board using given row and column size and adds number of
        bomb tile and fills the rest accordingly

        :return: List of  Lists with tiles of the board
        """

        num_tiles = self._row_size * self._col_size
        non_bomb_tile_count = num_tiles - self._num_bombs
        tile_draw = Sampler({1: ['Bomb', self._num_bombs],
                             2: ['Other', non_bomb_tile_count]})

        board = [[None] * self._col_size for row in range(self._row_size)]

        for row in range(self._row_size):
            for col in range(self._col_size):
                tile_type = tile_draw.output_draw()

                # Placeholder before implementation with BombTile and EmptyTile
                board[row][col] = tile_type

                if tile_type == 'Bomb':
                    # board[row][col] = BombTile(self, (row, col))
                    pass
                else:
                    # board[row][col] = EmptyTile(self, (row, col))
                    pass

        def set_numbered_tiles():
            # TODO refresh the board with NumberTiles in the correct positions
            pass

        return board

    def print_board(self):
        # This is a function to test board generation
        for row in self.board:
            print(row)


class Sampler:
    """
    Takes in an ordered sample and draws from them without replacement.
    The data is inputted as a dictionary representing
    numbers mapping to lists defining the name of the item and their count.
    The keys in the dictionary represent the ordering of the items.

    The indexes of these items depend on their count and order in the dictionary
    , and are between 1 and the total number
    of items in the whole sample, at all times.

    For example, in
    {1: ['Bomb', 20]
     2: ['Empty', 80]
    }
    At index 1, there is a 'Bomb'.
    At index 20, there is a 'Bomb'.
    At index 21, there is an 'Empty'.
    Index 0 does not exist.

    """
    _sample: dict
    _sample_count: int

    def __init__(self, distribution: Dict[int, List[str, int]]):
        self._sample = distribution
        self._sample_count = self.sum_count()

    def sum_count(self) -> int:
        """
        Counts the total number of items in the dictionary
        :return: the number of items in the dictionary
        """
        count = 0
        for key in self._sample:
            count += self._sample[key][1]
        return count

    def is_empty(self) -> bool:
        """
        :return: whether there are items left to draw from in the sample.
        """
        return self._sample_count == 0

    def output_draw(self) -> str:
        if not self.is_empty():
            index = randint(1, self._sample_count)
            key = self.find_item(index)
            item = self._sample[key][0]
            # remove the item from count at key
            self._sample[key][1] -= 1
            # remove item from total count
            self._sample_count -= 1
            return item
        return ''

    def find_item(self, index: int) -> int:
        """
        Returns the key of the item at index
        :param index:
        :return: a key existing in self._sample
        """
        count = 0
        for i in range(1, len(self._sample) + 1):
            subject = self._sample[i]
            count += subject[1]
            if index <= count:
                return i

    def print_sample_state(self):
        print(self._sample)


if __name__ == '__main__':
    test = Sampler({1: ['Bomb', 1], 2: ['Empty', 6]})
    for i in range(5):
        print("You drew a " + test.output_draw() + "!")
        test.print_sample_state()
    board_test = Board()
    board_test.print_board()
