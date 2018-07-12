from pygame import Surface, HWSURFACE, draw


class Road(object):
    white = (255, 255, 255)
    road_color = (10, 10, 10)
    clear_color = (255, 0, 255)
    
    lanes = 3

    def __init__(self, width, height):
        self.road_surface = self.road_lines = None
        self.width = self.height = self.left = self.right = self.lane_width = self.line_width = self.line_height = \
            self.line_gap = self.line_animation = self.line_offset = 0
        self.rect = (0, 0, 0, 0)
        self.resize(width, height)

    def resize(self, width, height):
        # reset the surfaces so they are redrawn with new sizes
        self.road_surface = self.road_lines = None
        # initialise all the values
        self.width = height * 0.6
        self.height = height
        self.left = (width - self.width) / 2
        self.right = self.left + self.width
        self.rect = (0, 0, self.width, self.height)
        self.lane_width = self.width / self.lanes
        self.line_width = int(self.width * 0.03)
        self.line_height = int(height * 0.15)
        self.line_gap = int(height * 0.1)
        self.line_animation = self.line_height + self.line_gap

    def update(self, amount):
        self.line_offset += amount
        if self.line_offset > self.line_animation:
            self.line_offset -= self.line_animation

    def draw(self, surface):
        if not self.road_surface:
            self.road_surface = Surface((self.width, self.height), flags=HWSURFACE)
            self.road_surface.set_colorkey(self.clear_color)
            self.road_surface.fill(self.clear_color)
            draw.rect(self.road_surface, self.road_color, self.rect)
            draw.line(self.road_surface, self.white, (0, 0), (0, self.height), self.line_width)
            draw.line(self.road_surface, self.white, (self.width, 0), (self.width, self.height), self.line_width)
        surface.blit(self.road_surface, (self.left, 0))
        if not self.road_lines:
            self.road_lines = Surface((self.width, self.height + self.line_animation), flags=HWSURFACE)
            self.road_lines.set_colorkey(self.clear_color)
            self.road_lines.fill(self.clear_color)
            for i in range(0, self.height + self.line_animation, self.line_animation):
                for j in range(1, self.lanes):
                    x = self.lane_width * j
                    draw.line(self.road_lines, self.white, (x, i), (x, i + self.line_height), self.line_width)
        surface.blit(self.road_lines, (self.left, self.line_offset - self.line_animation))
