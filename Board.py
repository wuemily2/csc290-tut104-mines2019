from typing import List, Dict, Optional
import Tile


class Board:
    """Holds the board and handles edits on the board

    == Attributes ==
    _row_size: the number of rows in the board
    _col_size: the number of columns in the board
    _num_bombs: the number of bombs to be placed when creating the board
    board: holds the board with all the tiles

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

    def create_board(self) -> List[List[Tile]]:
        """
        Creates the board using given row and column size and adds number of
        bomb tile and fills the rest accordingly

        :return: List of  Lists with tiles of the board
        """
        for row in range(self._row_size):
            for col in range(self._col_size):
                pass

        return []
