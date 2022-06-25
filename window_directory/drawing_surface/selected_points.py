import pygame
from window_directory.drawing_surface.point import Point
from window_directory.drawing_surface.line import Line


class SelectedPoints:

    def __init__(self, grid):

        self.first_point = None
        self.second_point = None
        self.grid = grid

    def if_point_is_clicked_select_or_deselect_point(self):

        # If the mouse hover over a intersecting point on the self.grid
        if self.grid.horizontal_lines.highlighted and self.grid.vertical_lines.highlighted:

            point_is_clicked = True

            self.select_first_point_deselect_first_point_or_select_second_point()

            return point_is_clicked

    def select_first_point_deselect_first_point_or_select_second_point(self):

        if self.first_point is None:

            self.select_first_point()

        else:

            self.select_second_point_or_deselect_first_point()

    def select_first_point(self):

        x = self.grid.vertical_lines.highlighted_line_position
        y = self.grid.horizontal_lines.highlighted_line_position

        self.first_point = Point(x, y)

    def select_second_point_or_deselect_first_point(self):

        x = self.grid.vertical_lines.highlighted_line_position
        y = self.grid.horizontal_lines.highlighted_line_position

        # if where the mouse clicked is the first point
        if (x, y) == (self.first_point.x, self.first_point.y):

            self.deselect_first_point()

        else:

            self.select_second_point(x, y)

    def deselect_first_point(self):

        self.first_point = None

    def select_second_point(self, x, y):

        self.second_point = Point(x, y)

    def deselect_point_if_typed_a(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.first_point = None

    def create_line_if_two_points_selected(self, drawn_lines):

        if self.second_point is not None:
            self.create_line(drawn_lines)

    def create_line(self, drawn_lines):

        line = Line(self.first_point.x, self.first_point.y, self.second_point.x, self.second_point.y)
        drawn_lines.add_line_to_line_list(line)

        self.remove_points()

    def remove_points(self):

        self.first_point = None
        self.second_point = None
