

class SceneStack(object):

    def __init__(self):
        self.scenes = list()

    def push_scene(self, scene):
        self.scenes.append(scene)

    def pop_scene(self):
        if len(self.scenes):
            self.scenes.pop(self.scenes[-1])

    def pop_all(self):
        self.scenes.clear()

    def replace_scene(self, old_scene, new_scene):
        index = self.scenes.index(old_scene)
        self.scenes[index] = new_scene

    def update(self):
        for scene in self.scenes:
            scene.update()

    def draw(self, surface):
        for scene in self.scenes:
            scene.draw(surface)
