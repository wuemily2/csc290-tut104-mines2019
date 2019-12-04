import pygame
from typing import List
import os


class TileView:
    """
    The TileView class handles changes needed for the view of each tile
    and updates itself

    == Attributes ==
    _size: size of the tile
    _image: The image of the current tile,
            eg: closed tile image if the tile is closed
    _rect: the bounding box of the tile that is used to keep track of collision
            with other tiles.
    _position: position of the tile on a given screen, (0, 0) by default
    id: stores the information on the row and column coordinate of the button
    """
    _size: tuple
    _image: pygame.image
    _rect: pygame.Rect
    _position: List[int]
    id: tuple

    def __init__(self, size: tuple, image: str, id: tuple) -> None:
        self._size = size
        self.id = id
        self._image = pygame.image.load(os.path.join(
            os.path.dirname(__file__), "assets/" + image + ".png"))
        self._image = pygame.transform.scale(self._image, size)

    def draw(self, screen: pygame.display, position: List[int]) -> None:
        """
        Draws the tile on the specified screen and position
        :param screen: The screen the tile should be drawn on to
        :param position:
        """
        self._position = position.copy()
        self._rect = self._image.get_rect().move(position[0], position[1])
        screen.blit(self._image, position)

    def update(self, screen: pygame.display, image: str) -> None:
        """
        Redraws the tile on the given screen with an updated image. Uses
        the stored position as the position on the screen.
        :param screen: The screen the tile should be drawn on to
        :param image: the name of new image to be displayed on the tile
        """
        self._image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "assets/" + image + ".png"))
        self._image = pygame.transform.scale(self._image, self._size)
        screen.blit(self._image, self._position)

    def get_rect(self) -> pygame.Rect:
        """
        Gets rectangle of the Tile which is needed to check if the mouse clicked
        on its area.
        :return: the rectangle box belonging to the the tile.
        """
        return self._rect


