from graphics import *

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

    def get_center_point(self):
        center_xcoord = (self._x2 - self._x1) / 2 + self._x1
        center_ycoord = (self._y2 - self._y1) / 2 + self._y1
        return Point(center_xcoord, center_ycoord)

    def draw_move(self, to_cell, undo=False):
        center_point = self.get_center_point()
        to_cell_center_point = to_cell.get_center_point()
        if undo == False:
            self._win.draw_line(Line(center_point, to_cell_center_point), "red")
        else:
            self._win.draw_line(Line(center_point, to_cell_center_point), "gray")