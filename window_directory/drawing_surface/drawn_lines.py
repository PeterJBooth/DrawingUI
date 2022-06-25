import pygame


class DrawnLines:

    def __init__(self):

        self.line_list = []
        self.highlighted_line = None

        self.selected_line_list = []

    def add_line_to_line_list(self, line):

        self.line_list.append([line.x1,
                               line.y1,
                               line.x2,
                               line.y2,
                               line.m,
                               line.c,
                               line.is_inverted])

    def highlight_drawn_line_if_mouse_touches_line(self, x, y):

        self.highlighted_line = None

        for line in self.line_list:

            self.check_if_mouse_is_touching_line(x, y, line)

    def check_if_mouse_is_touching_line(self, x, y, line):

        x1 = line[0]
        y1 = line[1]
        x2 = line[2]
        y2 = line[3]

        is_in_range = self.check_if_mouse_is_between_both_ends_of_line(x1, y1, x2, y2, x, y)

        if not is_in_range:

            return

        is_inverted = line[6]

        x, y = self.invert_x_y_if_drawn_line_x_y_was_inverted(x, y, is_inverted)

        m = line[4]
        c = line[5]

        is_touching_line = self.check_if_distance_between_mouse_and_line_is_small(m, c, x, y)

        if is_touching_line:

            self.create_highlighted_line(x1, y1, x2, y2)

    @staticmethod
    def invert_x_y_if_drawn_line_x_y_was_inverted(x, y, is_inverted):

        if is_inverted:
            y, x = x, y

        return x, y

    @staticmethod
    def check_if_mouse_is_between_both_ends_of_line(x1, y1, x2, y2, x, y):

        small_x = min(x1, x2)
        big_x = max(x1, x2)

        is_in_range = small_x - 10 < x < big_x + 10

        if not is_in_range:
            return is_in_range

        small_y = min(y1, y2)
        big_y = max(y1, y2)

        is_in_range = small_y - 10 < y < big_y + 10

        return is_in_range

    @staticmethod
    def check_if_distance_between_mouse_and_line_is_small(m, c, x, y):

        c_mouse = y - m * x
        distance_to_line = abs(c - c_mouse)

        is_touching_line = distance_to_line < 10

        return is_touching_line

    def create_highlighted_line(self, x1, y1, x2, y2):

        self.highlighted_line = [x1, y1, x2, y2]

    def if_line_is_clicked_select_or_deselect_line_if_clicked(self):

        if self.highlighted_line is not None:

            is_selected = self.check_whether_line_is_already_selected()
            self.select_or_deselect_line(is_selected)

    def check_whether_line_is_already_selected(self):

        if self.selected_line_list.count(self.highlighted_line) == 1:
            is_selected = True

        else:
            is_selected = False

        return is_selected

    def select_or_deselect_line(self, is_selected):

        if is_selected:

            self.deselect_line()

        else:

            self.select_line()

    def deselect_line(self):

        self.selected_line_list.remove(self.highlighted_line)

    def select_line(self):

        self.selected_line_list.append(self.highlighted_line)

    def remove_selected_lines_if_typed_delete(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DELETE:
                self.remove_selected_lines()

    def remove_selected_lines(self):

        lines_to_remove = self.find_lines_in_line_list_equal_to_selected_lines()

        self.remove_lines_from_line_list(lines_to_remove)

    def find_lines_in_line_list_equal_to_selected_lines(self):

        lines_to_remove = []

        for selected_line in self.selected_line_list:

            for line in self.line_list:

                if selected_line == line[0:4]:

                    lines_to_remove.append(line)

        return lines_to_remove

    def remove_lines_from_line_list(self, lines_to_remove):

        for line in lines_to_remove:

            self.line_list.remove(line)

        self.deselect_all_lines()

    def deselect_all_lines(self):

        self.selected_line_list = []



# connected_lines
# when last point of connected line is equal to first point of connected line --> polygon_list

# Not that simple
# branches

# each connection create a new list of lines

