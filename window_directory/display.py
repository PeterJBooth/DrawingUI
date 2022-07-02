import pygame

grid_image = pygame.image.load('Assets/Window_image.png')
highlighted_vert_line = pygame.image.load('Assets/Highlighted vertical line.png')
highlighted_hor_line = pygame.image.load('Assets/Highlighted horizontal line.png')
red_dot = pygame.image.load('Assets/Chosen Point.png')
MANUAL_CURSOR_IMG = pygame.image.load('Assets/Chosen Point.png')
icon = pygame.image.load('Assets/icon.jpg')

class Display:

    def __init__(self, event_handler):

        self.grid = event_handler.grid
        self.selected_points = event_handler.selected_points
        self.drawn_lines = event_handler.drawn_lines

        WIDTH, HEIGHT = 1300, 727
        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

        # Create surfaces
        self.grid_highlight_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.drawing_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        pygame.display.set_caption("")
        pygame.display.set_icon(icon)
        pygame.mouse.set_visible(False)  # hide the cursor

    def display_window(self):

        self.WIN.blit(grid_image, (0, 0))
        self.grid_highlight_surface.fill((0, 0, 0, 0))
        self.drawing_surface.fill((0, 0, 0, 0))

        self.display_highlighted_grid_line()
        self.display_selected_points()
        self.display_lines_drawn_on_grid()
        self.display_highlighted_drawn_lines()
        self.display_selected_drawn_lines()
        # self.display_shape_fill()

        if self.selected_points.first_point is not None:
            self.connect_line_to_mouse()

        self.WIN.blit(self.grid_highlight_surface, (0, 0))
        self.WIN.blit(self.drawing_surface, (0, 0))

        self.display_mouse()

        pygame.display.update()

    def display_highlighted_grid_line(self):

        self.display_highlighted_horizontal_grid_line()
        self.display_highlighted_vertical_grid_line()

    def display_highlighted_horizontal_grid_line(self):

        if self.grid.horizontal_lines.highlighted is True:
            self.grid_highlight_surface.blit(highlighted_hor_line,
                                             (275, self.grid.horizontal_lines.highlighted_line_position))

    def display_highlighted_vertical_grid_line(self):

        if self.grid.vertical_lines.highlighted is True:
            self.grid_highlight_surface.blit(highlighted_vert_line,
                                             (self.grid.vertical_lines.highlighted_line_position, 2))

    def display_selected_points(self):

        # The second point doesn't need to be displayed as once two points are selected, they are removed

        if self.selected_points.first_point is None:
            return

        x, y = self.selected_points.first_point.x, self.selected_points.first_point.y
        self.draw_circle_over_selected_point(x, y)

    def draw_circle_over_selected_point(self, x, y):

        image_height, image_width = 11, 11

        corrected_x = x - image_width // 2
        corrected_y = y - image_height // 2

        self.drawing_surface.blit(red_dot, (corrected_x, corrected_y))

    def display_lines_drawn_on_grid(self):

        for line in self.drawn_lines.line_list:

            first_point_x, first_point_y, second_point_x, second_point_y, _, _, _ = line

            pygame.draw.line(self.grid_highlight_surface, (200, 36, 51), (first_point_x, first_point_y),
                             (second_point_x, second_point_y), width=2)

    def display_highlighted_drawn_lines(self):

        if self.drawn_lines.highlighted_line is not None:

            first_point_x, first_point_y, second_point_x, second_point_y = self.drawn_lines.highlighted_line

            pygame.draw.line(self.grid_highlight_surface, (255, 125, 121), (first_point_x, first_point_y),
                             (second_point_x, second_point_y), width=2)

    def display_selected_drawn_lines(self):

        for selected_drawn_line in self.drawn_lines.selected_line_list:

            first_point_x, first_point_y, second_point_x, second_point_y = selected_drawn_line

            pygame.draw.line(self.grid_highlight_surface, (255, 125, 121), (first_point_x, first_point_y),
                             (second_point_x, second_point_y), width=3)

    def display_shape_fill(self):

        # return if the shape has less than 3 vertices
        line_list = self.drawn_lines.line_list

        if len(line_list) < 3:

            return

        shape_coordinates = []

        for line in line_list:

            first_point_x, first_point_y = line[0], line[1]
            shape_coordinates.append((first_point_x, first_point_y))

        pygame.draw.polygon(self.drawing_surface, (255, 0, 0), shape_coordinates, width=0)

    def connect_line_to_mouse(self):

        x, y = pygame.mouse.get_pos()

        pygame.draw.line(self.grid_highlight_surface, (200, 36, 51), (x, y),
                         (self.selected_points.first_point.x, self.selected_points.first_point.y), width=2)

    def display_mouse(self):

        x, y = pygame.mouse.get_pos()
        self.WIN.blit(MANUAL_CURSOR_IMG, (x - 5, y - 4))

