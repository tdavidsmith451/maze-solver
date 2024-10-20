from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 5, 5, 50, 50, win, 0)
    maze.solve()

    win.wait_for_close()

main()