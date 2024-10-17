from graphics import *
from cell import *

def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell2 = Cell(win)
    cell.draw(200, 200, 250, 250)
    cell2.draw(250, 200, 300, 250)
    cell.draw_move(cell2)

    win.wait_for_close()

main()