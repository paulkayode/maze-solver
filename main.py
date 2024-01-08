from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self ,width, height):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canva = Canvas()
        self.__canva.pack()
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


def main():
    win = Window(800, 600)
    win.wait_for_close()
    return 0



main()
