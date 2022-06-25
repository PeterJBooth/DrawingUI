import pygame
from drawing_surface.grid import Grid
from drawing_surface.selected_points import SelectedPoints
from drawing_surface.drawn_lines import DrawnLines
from event_handler import EventHandler
from display import Display


# Change to centroid finder??
# For now improve drawing code
# Removable lines
# shape fill?
# Text box next to mouse showing distance from other point. (polar as well?)

grid_image = pygame.image.load('Assets/Window_image.png')
highlighted_vert_line = pygame.image.load('Assets/Highlighted vertical line.png')
highlighted_hor_line = pygame.image.load('Assets/Highlighted horizontal line.png')
red_dot = pygame.image.load('Assets/Chosen Point.png')
MANUAL_CURSOR_IMG = pygame.image.load('Assets/Chosen Point.png')


class MainWindow:

    def __init__(self):

        # Window variables
        self.clock = None
        self.WIN = None
        self.FPS = None
        self.grid_highlight_surface = None
        self.drawing_surface = None

        self.grid = Grid()
        self.selected_points = SelectedPoints(self.grid)
        self.drawn_lines = DrawnLines()
        self.event_handler = EventHandler(self.grid, self.selected_points, self.drawn_lines)
        self.display = Display(self.event_handler)

        self.construct_main_window()

    def construct_main_window(self):

        self.create_clock()

        while True:

            self.run()

            if self.event_handler.stop_running:
                break

    def create_clock(self):

        self.clock = pygame.time.Clock()
        self.FPS = 60

    def run(self):

        self.clock.tick(self.FPS)

        for event in pygame.event.get():

            self.event_handler.perform_actions_triggered_by_event(event)

        self.display.display_window()

if __name__ == "__main__":
    MainWindow()
