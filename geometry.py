from tkinter import Tk, BOTH, Canvas

from config import *


class Point:
    def __init__(self,x = 0,y = 0):
        self.x = x
        self.y = y

class Line:
    def __init__(self,p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def draw(self,canvas, fill_colour):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill = fill_colour, width = 2
        )
        canvas.pack()

class Cell:
    def __init__(self,x1 = 0,y1 = 0,x2 = 0, y2 = 0, has_top_wall = True, has_right_wall =True , has_bottom_wall = True, has_left_wall = True, visited = False):
        self.has_top_wall = has_top_wall
        self.has_right_wall = has_right_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_left_wall = has_left_wall
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        self.visited = visited
    def set_x1(self,x1):
        self.__x1 = x1
    def set_x2(self,x2):
        self.__x2 = x2
    def set_y1(self,y1):
        self.__y1 = y1
    def set_y2(self,y2):
        self.__y2 = y2
     
    def get_bottom_right(self):
        if self.__y1 > self.__y2:
            return (self.__x1,self.__y1)
        else:
            return (self.__x2,self.__y2)

    def get_top_left(self):
        if self.__y1 < self.__y2:
            return (self.__x1,self.__y1)
        else:
            return (self.__x2,self.__y2)


    def draw(self, canva, fill_colour):
        if self.has_top_wall:
           self._draw_top(canva,fill_colour)
        else:
            self._draw_top(canva, back_ground_color)
        if self.has_bottom_wall:
            self._draw_bottom(canva, fill_colour)
        else:
            self._draw_bottom(canva, back_ground_color)
        if self.has_left_wall:
            self._draw_left(canva, fill_colour)
        else:
            self._draw_left(canva, back_ground_color)
        if self.has_right_wall:
           self._draw_right(canva, fill_colour)
        else:
            self._draw_right(canva, back_ground_color)
    
    def _draw_top(self, canva,fill_colour):
        x1,y1 = self.get_top_left()
        x2,y2 = self.get_bottom_right()
        p1 = Point(x1,y1)
        p2 = Point(x2,y1)
        line = Line(p1,p2)
        line.draw(canva, fill_colour)

    def _draw_bottom(self,canva, fill_colour):
        x1,y1 = self.get_top_left()
        x2,y2 = self.get_bottom_right()
        p1 = Point(x1,y2)
        p2 = Point(x2,y2)
        line = Line(p1,p2)
        line.draw(canva, fill_colour)

    def _draw_left(self,canva ,fill_colour):
        x1,y1 = self.get_top_left()
        x2,y2 = self.get_bottom_right()
        p1 = Point(x1,y1)
        p2 = Point(x1,y2)
        line = Line(p1,p2)
        line.draw(canva, fill_colour)

    def _draw_right(self,canva ,fill_colour):
        x1,y1 = self.get_top_left()
        x2,y2 = self.get_bottom_right()
        p1 = Point(x2,y1)
        p2 = Point(x2,y2)
        line = Line(p1,p2)
        line.draw(canva, fill_colour)

    
    def draw_move(self,canva, to_cell, undo=False):
        ax1,ay1 =  self.get_top_left()
        ax2, ay2 = self.get_bottom_right()
        ax = ax1 + (ax2- ax1)//2
        ay = ay1 + (ay2 - ay1)//2

        bx1,by1 = to_cell.get_top_left()
        bx2, by2 = to_cell.get_bottom_right()
        bx = bx1 + (bx2- bx1)//2
        by = by1 + (by2 - by1)//2

        p1 = Point(ax, ay)
        p2 = Point(bx, by)

        line = Line(p1, p2)

        if undo:
            line.draw(canva, "grey")
        else:
            line.draw(canva, "red")
            
        

