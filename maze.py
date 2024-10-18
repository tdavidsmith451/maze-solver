from graphics import *
from cell import *
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j, self._cells[i][j])

    def _draw_cell(self, i, j, cell):
        if self.win is None:
            return
        top_left_xcoord = self.x1 + self.cell_size_x * j
        top_left_ycoord = self.y1 + self.cell_size_y * i
        bottom_right_xcoord = top_left_xcoord + self.cell_size_x
        bottom_right_ycoord = top_left_ycoord + self.cell_size_y
        cell.draw(top_left_xcoord, top_left_ycoord, bottom_right_xcoord, bottom_right_ycoord)
        self._animate()

    def _animate(self):
        self.win.redraw()
        time.sleep(0.01)