class Player(object):

    x = []  # the x-coordinates of the snake's cells
    y = []  # the y-coordinates of the snake's cells

    direction = 0   # the start direction of the snake (right)

    update_count_max = 2
    update_count = 0

    def __init__(self, length, cell_size):
        self.length = length
        self.step = cell_size

        for i in range(length, 0, -1):
            self.x.append(i * self.step)
            self.y.append(0)

    def update(self):
        """move the snake"""
        self.update_count += 1
        if self.update_count > self.update_count_max:

            for i in range(self.length-1, 0, -1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]

            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step

            self.update_count = 0

    def move_right(self):
        """move right"""
        self.direction = 0

    def move_left(self):
        """move left"""
        self.direction = 1

    def move_up(self):
        """move up"""
        self.direction = 2

    def move_down(self):
        """move down"""
        self.direction = 3

    def draw(self, surface, image):
        """
        draw the snake

        :param surface: the surface the snake is being drawing on
        :param image: the path to the image of the snake
        """
        for i in range(0, self.length):
            surface.blit(image, (self.x[i], self.y[i]))
