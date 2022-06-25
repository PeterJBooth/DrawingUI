from window_directory.drawing_surface.grid_lines import GridLines
import pygame


class Grid:

    def __init__(self):

        STARTING_LINE, FINISHING_LINE = 298, 1273
        self.vertical_lines = GridLines(STARTING_LINE, FINISHING_LINE)

        STARTING_LINE, FINISHING_LINE = 25, 700
        self.horizontal_lines = GridLines(STARTING_LINE, FINISHING_LINE)

    def highlight_vertical_line_if_touched(self, x, _):

        self.vertical_lines.highlighted = False

        for line_position in self.vertical_lines.line_positions:

            if x in range(line_position - 3, line_position + 4):
                self.vertical_lines.highlighted_line_position = line_position
                self.vertical_lines.highlighted = True

    def highlight_horizontal_line_if_touched(self, x, y):

        self.horizontal_lines.highlighted = False

        grid_left_side = self.vertical_lines.line_positions[0] - 25

        if x < grid_left_side:
            return

        for line_position in self.horizontal_lines.line_positions:

            if y in range(line_position - 3, line_position + 4):
                self.horizontal_lines.highlighted_line_position = line_position
                self.horizontal_lines.highlighted = True
