#Player class, stores character location and image file
class Player(object):
    def __init__(self, name, x, y, img):
        self.name = name
        self.x = x
        self.y = y
        self.img = img

#Cat class, stores cats location and image file
class Cat(object):
    def __init__(self, name, x, y, img):
        self.name = name
        self.x = x
        self.y = y 
        self.img = img 
        