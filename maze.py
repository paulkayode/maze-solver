from geometry import *
from window import Window
import time
import random
from config import *


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win = None,seed = None):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.win = win
        self._cells= [[None for i in range(0,num_cols)] for j in range(0,num_rows)]
        if seed is not None:
            random.seed(seed)
    
    def get_num_rows(self):
        return self.__num_rows
    
    def get_num_cols(self):
        return self.__num_cols
    
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
        if self.win is not None:
            self.win.draw_cell(self._cells[i][j],wall_color)
            self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)
    

    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_left_wall = False
        self._cells[-1][-1]. has_right_wall = False
        if self.win is not None:
            self.win.draw_cell(self._cells[0][0],wall_color)
            self.win.draw_cell(self._cells[-1][-1],wall_color)
            self._animate()

    def _break_walls_r(self,i,j):
        current = self._cells[i][j]
        current.visited = True
        while True:
            values = []
            
            dx = [0,0,1 ,-1]
            dy = [-1,1,0,0]

            for z in range(0,4):
                zx = i + dx[z]
                zy = j + dy[z]
                if (zx >= 0 
                    and zx < self.__num_rows 
                    and zy >= 0 
                    and zy <  self.__num_cols
                    and not self._cells[zx][zy].visited):
                    values.append(z)
            if len(values) == 0:
                if self.win is not None:
                    self.win.draw_cell(current, wall_color)
                return
            z = random.choice(values)
            zx = i + dx[z]
            zy = j + dy[z]
            if z == 3:
                self._cells[zx][zy].has_bottom_wall = False
                self._cells[i][j].has_top_wall = False
            elif z == 2:
                self._cells[zx][zy].has_top_wall = False
                self._cells[i][j].has_bottom_wall = False
            elif z == 1:
                self._cells[zx][zy].has_left_wall = False
                self._cells[i][j].has_right_wall = False
            else:
                self._cells[zx][zy].has_right_wall = False
                self._cells[i][j].has_left_wall = False
            self._break_walls_r(zx,zy)

    def _reset_cells_visited(self):
        for i in range(0,self.__num_rows):
            for j in range(0,self.__num_cols):
                self._cells[i][j].visited = False

            

