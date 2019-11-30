import pygame
import os

class TileView:
    """
    The TileView class handles changes needed for the view of each tile
    and updates itself

    == Attributes ==
    _size: size of the tile
    _position: position of the tile on a given screen, (0, 0) by default
    _image: The image of the current tile,
            eg: closed tile image if the tile is closed
    id: stores the information on the row and column coordinate of the button
    """
    _size: tuple
    _image: pygame.image
    rect: pygame.Rect
    position: tuple
    id: tuple

    def __init__(self, size: tuple, image: str, id: tuple) -> None:
        self._size = size
        self.id = id
        self._image = pygame.image.load(os.path.join(
            os.path.dirname(__file__), "assets/" + image + ".png"))
        self._image = pygame.transform.scale(self._image, size)

    def draw(self, screen, position):
        self.position = position.copy()
        self.rect = self._image.get_rect().move(position[0], position[1])
        screen.blit(self._image, position)

    def update(self, screen, image):

        self._image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "assets/" + image + ".png"))
        self._image = pygame.transform.scale(self._image, self._size)
        screen.blit(self._image, self.position)

    def get_rect(self) -> pygame.Rect:
        """
        Gets rectangle of the Tile which is needed to check if the mouse clicked
        on its area.
        :return: the rectangle box belonging to the the tile.
        """
        return self.rect


