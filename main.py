from window import Window
from maze import Maze
from geometry import *
from config import *

def main():
    
    maze = Maze(5,5,13,20, 39,39, Window(800,600))
    maze._create_cells()
    
    maze._break_entrance_and_exit()
    maze._break_walls_r(0,0)
    maze.win.wait_for_close()
    return 0



main()
