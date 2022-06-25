import pygame


class EventHandler:

    def __init__(self, grid, selected_points, drawn_lines):

        self.grid = grid
        self.selected_points = selected_points
        self.drawn_lines = drawn_lines

        self.stop_running = False

    def perform_actions_triggered_by_event(self, event):

        self.perform_actions_triggered_by_click(event)
        self.perform_actions_triggered_by_pressed_key(event)
        self.perform_actions_triggered_by_mouse_position()

    def perform_actions_triggered_by_click(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:

            point_is_clicked = self.selected_points.if_point_is_clicked_select_or_deselect_point()

            if point_is_clicked:

                self.selected_points.create_line_if_two_points_selected(self.drawn_lines)
                return

            self.drawn_lines.if_line_is_clicked_select_or_deselect_line_if_clicked()

    def perform_actions_triggered_by_mouse_position(self):

        x, y = pygame.mouse.get_pos()

        self.grid.highlight_vertical_line_if_touched(x, y)
        self.grid.highlight_horizontal_line_if_touched(x, y)

        self.drawn_lines.highlight_drawn_line_if_mouse_touches_line(x, y)

    def perform_actions_triggered_by_pressed_key(self, event):

        self.quit_if_pressed_quit_button(event)
        self.quit_if_typed_q(event)

        self.selected_points.deselect_point_if_typed_a(event)
        self.drawn_lines.remove_selected_lines_if_typed_delete(event)

    def quit_if_pressed_quit_button(self, event):

        if event.type == pygame.QUIT:
            self.stop_running = True

    def quit_if_typed_q(self, event):

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                self.stop_running = True