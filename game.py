import sys
import pygame
from pygame.locals import *
from scene_stack import SceneStack
from game_scene import GameScene, Difficulty

fps = 60

display_width = 1920
display_height = 1080

white = (255, 255, 255)
grass = (0, 80, 0)


def quit_game():
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Vacation')
    fps_clock = pygame.time.Clock()
    font = pygame.font.Font(pygame.font.get_default_font(), 30)

    scene_stack = SceneStack()
    game_scene = GameScene(display_width, display_height, scene_stack, Difficulty.Easy)
    scene_stack.push_scene(game_scene)

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
        scene_stack.update()
        scene_stack.draw(surface)
        fps_display = font.render(str(int(fps_clock.get_fps())), False, white)
        surface.blit(fps_display, (5, 5))
        pygame.display.update()
        fps_clock.tick(fps)
