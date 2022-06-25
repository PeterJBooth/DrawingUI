class GridLines:

    def __init__(self, first_line_position, last_line_position):

        self.line_positions = []
        self.highlighted = False
        self.highlighted_line_position = None

        self.get_line_positions(first_line_position, last_line_position)

    def get_line_positions(self, first_line_position, last_line_position):

        for line_position in range(first_line_position, last_line_position + 25, 25):

            self.line_positions.append(line_position)
