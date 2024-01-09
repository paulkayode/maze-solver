from window import Window
from geometry import *

win = Window(800, 600)
def main():
    
    c1 = Cell(750, 550,800 ,600, False, True, True,True)
    c2 = Cell(50,5, 100, 50, True, True, False,False)
    win.draw_cell(c1,"red")
    win.draw_cell(c2, "black")
    win.draw_move(c1,c2)

    win.wait_for_close()
    return 0



main()
