from tkinter import *

class Layout(Tk):
    def __init__(self):
        super().__init__()
        width=1000
        height=500
        self.geometry(f'{width}x{height}')
        self.title("Astra")


        #-------------------GUI decoration begins form here----------------------------
        



class HomePage(Layout):
    pass



if __name__=='__main__':
    layout=Layout()

    layout.mainloop()