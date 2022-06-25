class Line:

    def __init__(self, x1, y1, x2, y2):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.m = None
        self.c = None
        self.is_inverted = False

        self.create_equation_of_line()

    def create_equation_of_line(self):

        x1, y1, x2, y2 = self.invert_xs_and_ys_if_gradient_greater_than_1()

        self.get_gradient(x1, y1, x2, y2)
        self.get_intercept(x1, y1)

    def invert_xs_and_ys_if_gradient_greater_than_1(self):

        x1 = self.x1
        y1 = self.y1

        x2 = self.x2
        y2 = self.y2

        if abs(self.y2 - self.y1) > abs(self.x2 - self.x1):

            self.is_inverted = True
            x1, y1 = y1, x1
            x2, y2 = y2, x2

        return x1, y1, x2, y2

    def get_gradient(self, x1, y1, x2, y2):

        self.m = (y2 - y1) / (x2 - x1)

    def get_intercept(self, x1, y1):

        self.obtain_c_with_x1_and_y1(x1, y1)

    def obtain_c_with_x1_and_y1(self, x1, y1):

        # y = mx + c
        # c = y - mx

        self.c = y1 - self.m * x1
