from __future__ import annotations
from typing import List, Dict, Optional
from Tile import Tile
from EmptyTile import EmptyTile
from BombTile import BombTile
from NumberTile import NumberTile
from random import randint
import random

random.seed(0)


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
    _is_game_over: bool
    _flagged_bombs: int

    def __init__(self, row_size: int = 5, col_size: int = 5,
                 num_bombs: int = 3) -> None:

        self.start_new_game(row_size, col_size, num_bombs)

    def start_new_game(self, row_size: int = 9, col_size: int = 9,
                       num_bombs: int = 10):
        self._row_size = row_size
        self._col_size = col_size
        self._num_bombs = num_bombs
        self.board = self.create_board()
        self._is_game_over = False
        self._flagged_bombs = 0

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

        board = [[None] * self._col_size for x in range(self._row_size)]

        for arow in range(self._row_size):
            for acol in range(self._col_size):
                tile_type = tile_draw.output_draw()

                # Placeholder before implementation with BombTile and EmptyTile
                board[arow][acol] = tile_type

                if tile_type == 'Bomb':
                    board[arow][acol] = BombTile(board, (arow, acol))
                else:
                    board[arow][acol] = EmptyTile(board, (arow, acol))

        # Set numbered tiles
        for arow in range(self._row_size):
            for acol in range(self._col_size):
                cur_tile = board[arow][acol]
                if isinstance(cur_tile, EmptyTile):
                    count = 0

                    # Count number of bomb tiles
                    for x_shift in [-1, 0, 1]:
                        for y_shift in [-1, 0, 1]:
                            if x_shift == y_shift == 0:
                                continue  # Skip this loop iteration
                            try:
                                index = (cur_tile.get_position()[0] + x_shift,
                                         cur_tile.get_position()[1] + y_shift)
                                other_tile = board[index[0]][
                                    index[1]]
                                if index[0] >= 0 and index[1] >=0 and \
                                        isinstance(other_tile, BombTile):
                                    count += 1
                            except IndexError:  # do nothing
                                pass
                    if count > 0:
                        board[arow][acol] = NumberTile(board, (arow, acol),
                                                       count)

        return board

    def print_board(self):
        # This is a function to test board generation
        for arow in range(self._row_size):
            row_accum = "["
            for acol in range(self._col_size):
                row_accum += self.board[arow][acol].to_string() + ","
            row_accum += "]"
            print(row_accum)

    def reveal(self, arow, acol):
        if self._is_game_over:
            return
        try:
            if not self.board[arow][acol].reveal_tile():  # if bomb
                self._is_game_over = True
        except IndexError:
            print("Out of Bounds")

    def flag(self, arow, acol):
        if self._is_game_over:
            return
        try:
            the_tile = self.board[arow][acol]
            if the_tile.flag_tile() and isinstance(the_tile, BombTile):
                if the_tile.is_flagged():
                    self._flagged_bombs += 1
                    if self.is_game_won():
                        self._is_game_over = True
                else:
                    self._flagged_bombs -= 1
        except IndexError:
            print("Out of Bounds")

    def is_game_won(self) -> bool:
        # return if all bombs are flagged
        return self._flagged_bombs == self._num_bombs

    def is_game_over(self):
        return self._is_game_over

    def get_tile(self, row: int, col: int) -> Tile:
        return self.board[row][col]

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
    '''test = Sampler({1: ['Bomb', 1], 2: ['Empty', 6]})
    for i in range(5):
        print("You drew a " + test.output_draw() + "!")
        test.print_sample_state()'''
    board_test = Board()
    keep_playing = True
    while keep_playing:
        while not board_test.is_game_over():
            board_test.print_board()
            try:
                row = int(input("Enter a row: "))
                col = int(input("Enter a column: "))
                click_type = int(input(
                    "Enter 0 for left click, and 1 for right click" +
                    ", and anything else aborts your move: "))
                if click_type == 0:
                    board_test.reveal(row, col)
                elif click_type == 1:
                    board_test.flag(row, col)
                else:
                    print("move aborted")
            except:
                print("You didn't input a correct number, try again")
        if board_test.is_game_won():
            print("You won the game!")
        board_test.print_board()
        print("Game is over!")
        play_again = input("Do you want to play again? [enter y/n]: ")
        if play_again == "y":
            board_test.start_new_game()
        elif play_again == "n":
            keep_playing = False
