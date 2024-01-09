from window import Window
from maze import Maze
from geometry import *

def main():
    
    maze = Maze(5,5,13,20, 39,39, Window(800,600))
    maze._create_cells()
    
    maze._BREAK_ENTRANCE_AND_EXIT()
    maze.win.wait_for_close()
    return 0



main()
