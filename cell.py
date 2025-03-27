from window import *

class Cell:
    def __init__(self, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self.win = win
    
    def draw(self, x1, y1, x2, y2):
        if self.win is None:
            return
        # x1, y1 are top-left and x2, y2 are bottom right
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        p1 = Point(x1, y1)
        p2 = Point(x2, y1)
        p3 = Point(x1, y2)
        p4 = Point(x2, y2)
        line1 = Line(p1, p2)
        line2 = Line(p1, p3)
        line3 = Line(p2, p4)
        line4 = Line(p3, p4)
        if self.has_top_wall:
            self.win.draw_line(line1, "red")
        else:
            self.win.draw_line(line1, "white")
        if self.has_left_wall:
            self.win.draw_line(line2, "blue")
        else:
            self.win.draw_line(line2, "white")
        if self.has_right_wall:
            self.win.draw_line(line3, "green")
        else:
            self.win.draw_line(line3, "white")
        if self.has_bottom_wall:
            self.win.draw_line(line4, "black")
        else:
            self.win.draw_line(line4, "white")
    
    def draw_move(self, to_cell, undo=False):
        middle_x = (self._x1 + self._x2) / 2
        middle_y = (self._y1 + self._y2) / 2
        # Find the middle of the other cell
        other_x = (to_cell._x1 + to_cell._x2) / 2
        other_y = (to_cell._y1 + to_cell._y2) / 2
        point_middle1 = Point(middle_x, middle_y)
        point_middle2 = Point(other_x, other_y)
        line_middle = Line(point_middle1, point_middle2)
        if undo:
            self.win.draw_line(line_middle, "gray")
        else:
            self.win.draw_line(line_middle, "red")



