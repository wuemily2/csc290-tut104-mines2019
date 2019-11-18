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
    position: tuple
    _image: pygame.image
    id: tuple

    def __init__(self, size: tuple, image: str) -> None:
        self.position = (0, 0)
        self._size = size
        self._image = pygame.image.load(os.path.join(os.path.dirname(__file__), "assets/" + image + ".png"))
        self._image.transform.scale(self._image, self._size)

    def draw(self, screen):

        # draw selected image
        screen.blit(self._image, self.position)

    def set_tile(self, tile: str) -> None:
        """
        Changes the image of the view and updates it the screen

        :param tile: name of the tile
                eg: "bomb" for bomb tile
        """
        self._image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "assets/" + tile + ".png"))
        self._image.transform.scale(self._image, self._size)

    def get_rect(self):
        return self._image.getrect()

    def set_tile_id(self, id: tuple) -> None:
        """
        :param id:
        :return:
        """
        self.id = id

    # def event_handler(self, event):
    #
    #     # change selected color if rectange clicked
    #     if event.type == pygame.MOUSEBUTTONDOWN:  # is some button clicked
    #         if event.button == 1:  # is left button clicked
    #             if self._rect.collidepoint(event.pos):  # is mouse over button


