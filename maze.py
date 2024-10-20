from graphics import *
from cell import *
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        if seed != None:
            random.seed(seed)
        self._cells = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            col_cells = []
            for j in range(self.num_rows):
                col_cells.append(Cell(self.win))
            self._cells.append(col_cells)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self.win is None:
            return
        top_left_xcoord = self.x1 + self.cell_size_x * i
        top_left_ycoord = self.y1 + self.cell_size_y * j
        bottom_right_xcoord = top_left_xcoord + self.cell_size_x
        bottom_right_ycoord = top_left_ycoord + self.cell_size_y
        self._cells[i][j].draw(top_left_xcoord, top_left_ycoord, bottom_right_xcoord, bottom_right_ycoord)
        self._animate()

    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.03)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)

        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            possible_directions = []
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_directions.append((i - 1, j))
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                possible_directions.append((i + 1, j))
            if j > 0 and not self._cells[i][j - 1].visited:
                possible_directions.append((i, j - 1))
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                possible_directions.append((i, j + 1))
            if len(possible_directions) == 0:
                self._draw_cell(i, j)
                return
            direction = random.choice(possible_directions)

            if direction[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False

            if direction[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False

            if direction[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
                
            if direction[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            
            self._break_walls_r(direction[0], direction[1])
    
    def _reset_cells_visited(self):
        for r in self._cells:
            for c in r:
                c.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        #left
        if (
            i > 0
            and not self._cells[i - 1][j].visited
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        #right
        if (
            i < self.num_cols - 1
            and not self._cells[i + 1][j].visited
            and not self._cells[i][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        #up
        if (
            j > 0
            and not self._cells[i][j - 1].visited
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        #down   
        if (
            j < self.num_rows - 1
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)

        
        return False