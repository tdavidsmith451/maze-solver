from graphics import *

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall == True:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(left_line, "black")

        if self.has_right_wall == True:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(right_line, "black")

        if self.has_top_wall == True:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(top_line, "black")

        if self.has_bottom_wall == True:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(bottom_line, "black")