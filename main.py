from window import Window
from geometry import *
def main():
    win = Window(800, 600)
    c1 = Cell(5,5, 50, 50, False, True, True,True)
    c2 = Cell(50,5, 100, 50, True, True, False,False)
    win.draw_cell(c1,"red")
    win.draw_cell(c2, "black")
    win.draw_move(c1,c2)

    win.wait_for_close()
    return 0



main()
