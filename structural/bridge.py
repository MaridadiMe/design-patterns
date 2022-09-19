class DrawCircleApiOne:
    """ Implementation specific abstraction: concrete class one """
    def draw_circle(self, x, y, radius):
        print('API 1 Drawing circle at {}, {} with radius {}'.format(x,y,radius))

class DrawCircleApiTwo:
    """ Implementation specific abstraction: concrete class 2 """
    def draw_circle(self, x, y, radius):
        print('API 2 Drawing circle at {}, {} with radius {}'.format(x,y,radius))

class Circle(object):
    """ implementation independent abstraction """
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius 
        self._drawing_api = drawing_api 

    def draw(self):
        """ implementation specific abstraction take care of by another abstraction """
        self._drawing_api.draw_circle(self._x, self._y, self._radius)


    def scale(self, percent):
        """ implementation independent """
        self._radius *= percent


# build the first circle object by using api  one
circle1 = Circle(2,3,4, DrawCircleApiOne())
# draw circle
circle1.draw()

# build the first circle object by using api  one
circle2 = Circle(3,4,5, DrawCircleApiTwo())
# draw circle
circle2.draw()