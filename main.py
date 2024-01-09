from window import Window
from maze import Maze
from config import *

def main():
    maze = Maze(5,5,18,25, 30,30, Window(800,600))
    maze.solve()
    return 0



main()
