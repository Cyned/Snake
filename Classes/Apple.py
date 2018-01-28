class Apple(object):

    def __init__(self, x, y, cell_size):
        self.x = x * cell_size
        self.y = y * cell_size

    def draw(self, surface, image):
        """
        draw an apple

        :param surface: the surface the apple is being drawing on
        :param image: the path to the image of the apple
        """
        surface.blit(image, (self.x, self.y))
