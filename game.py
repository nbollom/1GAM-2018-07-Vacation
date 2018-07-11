import sys
import pygame
from pygame.locals import *

fps = 60

display_width = 1920
display_height = 1080

white = (255, 255, 255)
grass = (0, 80, 0)
road_color = (10, 10, 10)

road_width = display_height * 0.6
road_left = (display_width - road_width) / 2
road_right = road_left + road_width
road_rect = (road_left, 0, road_width, display_height)
lanes = 3
lane_width = road_width / lanes
line_width = int(road_width * 0.03)
line_height = int(display_height * 0.15)
line_gap = int(display_height * 0.1)
line_animation = line_height + line_gap
animation_step = 10


def quit_game():
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Vacation')
    fps_clock = pygame.time.Clock()
    font = pygame.font.Font(pygame.font.get_default_font(), 30)
    animation_counter = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                quit_game()
            elif event.type == KEYDOWN:
                if event.key == K_RETURN and event.mod & KMOD_ALT:
                    pygame.display.toggle_fullscreen()
                elif event.key == K_ESCAPE:
                    quit_game()
        surface.fill(grass)
        pygame.draw.rect(surface, road_color, road_rect)
        pygame.draw.line(surface, white, (road_left, 0), (road_left, display_height), line_width)
        pygame.draw.line(surface, white, (road_right, 0), (road_right, display_height), line_width)
        line_start = (-animation_counter % line_animation)
        for i in range(-line_start, display_height, line_animation):
            for j in range(1, lanes):
                x = lane_width * j + road_left
                pygame.draw.line(surface, white, (x, i), (x, i + line_height), line_width)
        fps_display = font.render(str(int(fps_clock.get_fps())), False, white)
        surface.blit(fps_display, (5, 5))
        pygame.display.update()
        fps_clock.tick(fps)
        animation_counter += animation_step
