import pygame
import os


class TileView(object):
    """
    The TileView class handles changes needed for the view of each tile
    and updates itself

    == Attributes ==
    size: size of the tile
    position: position of the tile on a given screen, (0, 0) by default
    image: The image of the current tile,
            eg: closed tile image if the tile is closed
    screen: the screen for which the tileview belongs to
    """
    _size: tuple
    _position: tuple
    _image: pygame.image
    _screen: pygame.display

    def __init__(self, size: tuple, image_loc: str,
                 screen: pygame.display) -> None:

        self._position = (0, 0)
        self._size = size
        self._screen = screen
        self.set_image(image_loc)

    def draw(self, position: tuple) -> None:
        """
        Draws the TileView on a given pygame screen

        :param position: the position at which to draw
        """
        self._position = position
        rect = self._image.get_rect()
        rect = rect.move(self._position)

        # draws the image at the specified screen
        self._screen.blit(self._image, rect)

    def set_image(self, image_loc: str) -> None:
        """
        Changes the image of the view and updates it the screen

        :param image_loc: the location of the image
                eg: "assets/1.png"
        """
        self._image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), image_loc))
        self._image = pygame.transform.scale(self._image, self._size)
        self.draw(self._position)

    # TODO:

    # Saved for later implementaion
    # def event_handler(self, event):
    #     if event.type == pygame.MOUSEBUTTONDOWN:
    #         if event.button == 1:
    #             if self._rect.collidepoint(event.pos):
    #
