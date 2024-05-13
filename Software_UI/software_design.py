"""
Contains all the frames for the dashboard for the staff of the hospital.

"""


from software_windows import *
from tkinter import Frame
from tkinter import Label

class Login_page(Frame):
    
    
    def __init__(self,window_object):
        super().__init__(window_object,bg="black",height=800,width=200)
        self.pack()
    """

    def __init__(self,window_object):
        super().__init__(window_object,bg="black",height=500,width=900)
        self.pack()
    """

    
     



        
    




class Dashboard:
    pass


class Dashboard_reception(Dashboard):
    pass


class Dashboard_doctor(Dashboard):
    pass


class Dashboard_testing_center(Dashboard):
    pass




if __name__=='__main__':
    root=Window()
    root=root.normal_window()
    Login_page(root)
    root.mainloop()


    