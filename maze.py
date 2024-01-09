from geometry import *
win = Window(800, 600)
from window import Window
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = Window(800, 600)
        self.__cells= [[None for i in range(0,num_cols)] for j in range(0,num_rows)]
    
    def _create_cells(self):
        x1 = self.__x1
        y1 = self.__y1
        for i in range(0,self.__rum_rows):
            for j in range(0, self.__num_cols):
                self.__cells[i][j] = Cell()
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        self.__cells[i][j].set_x1(self.__x1 + (j * self.__cell_size_x))
        self.__cells[i][j].set_x2(self.__x1 + ((j+1) * self.__cell_size_x))
        self.__cells[i][j].set_y1( self.__y1 + (i * self._cell_size_y) )
        self.__cells[i][j].set_y2( self.__y1 + ((i+1) * self._cell_size_y))
        self.__win.draw_cell(self.__cells[i][j])
        self._animate()
    
    def _animate(self):
        self.__win.redraw()
        time.sleep(0.05)