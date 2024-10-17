import tkinter as tk
from tkinter import Canvas, BOTH

class Window:
    def __init__(self, width, height):
        self.__root = tk.Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", height=height, width=width)
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__open = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self):
        self.__open = True
        while self.__open == True:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__open = False

    def draw_line(self, line, fill_color):
        line.draw(self.__canvas, fill_color)