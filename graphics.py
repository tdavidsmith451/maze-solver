import tkinter as tk
from tkinter import Canvas, BOTH

class Window:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)
        self.canvas.pack(fill=BOTH, expand=1)
        self.open = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.open = True
        while self.open == True:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.open = False
