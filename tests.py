import unittest
from maze import *

class tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_cells2(self):
        num_cols = 20
        num_rows = 11
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_break_entrance_and_exit(self):
        m1 = Maze(0, 0, 20, 20, 5, 5)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[19][19].has_bottom_wall, False)

    def test_reset_cells_visited(self):
        m1 = Maze(0, 0, 20, 20, 5, 5)
        self.assertEqual(m1._cells[0][0].visited, False)
        self.assertEqual(m1._cells[19][19].visited, False)

    def test_walls(self):
        maze = Maze(50, 50, 5, 5, 50, 50, win=None, seed=0)
        self.assertEqual(maze._cells[0][0].has_right_wall, True)



if __name__ == "__main__":
    unittest.main()