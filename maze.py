from geometry import *
from window import Window
import time

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.win = win
        self._cells= [[None for i in range(0,num_cols)] for j in range(0,num_rows)]
    
    def _create_cells(self):
        x1 = self.__x1
        y1 = self.__y1
        for i in range(0,self.__num_rows):
            for j in range(0, self.__num_cols):
                self._cells[i][j] = Cell()
                self._draw_cell(i,j)

    def _draw_cell(self, i, j):
        self._cells[i][j].set_x1(self.__x1 + (j * self.__cell_size_x))
        self._cells[i][j].set_x2(self.__x1 + ((j+1) * self.__cell_size_x))
        self._cells[i][j].set_y1( self.__y1 + (i * self.__cell_size_y) )
        self._cells[i][j].set_y2( self.__y1 + ((i+1) * self.__cell_size_y))
        self.win.draw_cell(self._cells[i][j],"black")
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
    
    def _BREAK_ENTRANCE_AND_EXIT(self):
        self._cells[0][0].has_left_wall = False
        self._cells[-1][-1]. has_right_wall = False
        self._cells[0][0]._draw_left(self.win.canva, "white")
        self._cells[-1][-1]._draw_right(self.win.canva, "white")
        self._animate()