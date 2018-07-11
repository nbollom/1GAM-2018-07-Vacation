

class Road(object):
    white = (255, 255, 255)
    road_color = (10, 10, 10)

    lanes = 3

    def __init__(self, width, height):
        self.road_surface = self.road_lines = None
        self.resize(width, height)

    def resize(self, width, height):
        # reset the surfaces so they are redrawn with new sizes
        self.road_surface = self.road_lines = None
        self.width = height * 0.6
        self.left = (width - self.width) / 2
        self.right = self.left + self.width
        self.rect = (self.left, 0, self.width, height)
        self.lane_width = self.width / self.lanes
        self.line_width = self.width * 0.1
        self.line_height = int(height * 0.15)
        self.line_gap = int(height * 0.1)
        self.line_animation = self.line_height + self.line_gap
