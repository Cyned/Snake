class Game(object):

    level = 1   # the level of the snake

    def is_collision(self, x1, y1, x2, y2):
        """
        :param x1: x-coordinate of the first object;
        :param y1: y-coordinate of the first object;
        :param x2: x-coordinate of the second object;
        :param y2: y-coordinate of the second object;

        :return: True if it was a collision between these two objects.
        """
        if x1 == x2:
            if y1 == y2:
                self.level = self.level + 1
                return True
        return False

    @staticmethod
    def is_out(x, y, win_width, win_height):
        """
        :param x: x-coordinate of the object;
        :param y: y-coordinate of the object;
        :param win_width: the width of the game field;
        :param win_height: the height of the game field;

        :return: True if the snake is out of the game field.
        """
        if x < 0 or x > win_width or y < 0 or y > win_height:
            return True
        return False
