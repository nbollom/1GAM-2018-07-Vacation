from enum import Enum, unique
from scene import Scene


@unique
class Difficulty(Enum):
    Easy = 0
    Normal = 1
    Hard = 2


class GameScene(Scene):
    grass = (0, 80, 0)

    def __init__(self, width, height, scene_stack, difficulty):
        super(GameScene, self).__init__(width, height, scene_stack)
        self.difficulty = difficulty
        self.counter = 0

    def update(self):
        pass

    def draw(self, surface):
        pass
