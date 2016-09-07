class Tile(object):
    """Basic tile class, just holds the position and image of the tile, and contains a method for rendering."""

    def __init__(self, x_pos, y_pos, image):
        self.position = (x_pos, y_pos)
        self.image = image

    def render(self, surface):
        surface.blit(self.image, self.position)
