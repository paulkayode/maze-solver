from tkinter import Tk, BOTH, Canvas
from geometry import Line

class Window:

    def __init__(self ,width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.canva = Canvas(width = width, height = height)
        self.canva.pack()
        self.__is_running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
    
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
    
    def close(self):
        self.__is_running = False

    def draw_line(self,line, fill_colour):
        line.draw(self.canva, fill_colour)
    def draw_cell(self,cell, fill_colour):
        cell.draw(self.canva,fill_colour)
    def draw_move(self ,c1, c2, undo=False):
        c1.draw_move(self.canva, c1,c2, undo)
