import weakref


class Scene(object):

    def __init__(self, width, height, scene_stack):
        self.width = width
        self.height = height
        self.scene_stack_ref = weakref.ref(scene_stack)

    def resize(self, width, height):
        self.width = width
        self.height = height

    def update(self):
        pass

    def draw(self, surface):
        pass

    def get_scene_stack(self):
        return self.scene_stack_ref()
