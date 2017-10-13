from pygame import sprite

class Actor(sprite.Sprite):
    """description of class"""
    def __init__(self, _x, _y):
        sprite.Sprite.__init__(self)
        self.x = _x
        self.y = _y


