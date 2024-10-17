from graphics import *

def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(2, 2), Point(200, 200)), "black")

    win.wait_for_close()

main()