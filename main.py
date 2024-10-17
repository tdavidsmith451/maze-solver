from graphics import *
from cell import *

def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.draw(200, 200, 250, 250)

    win.wait_for_close()

main()