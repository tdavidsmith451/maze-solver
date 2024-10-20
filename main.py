from graphics import *
from cell import *
from maze import *

def main():
    win = Window(800, 600)

    maze = Maze(50, 50, 15, 15, 50, 50, win, 0)

    win.wait_for_close()

main()