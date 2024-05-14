"""
Contains all the frames for the dashboard for the staff of the hospital.

"""


from software_windows import *
from tkinter import Frame
from tkinter import Label
import tkinter as tk

class Login_page(Frame):
    """
    Used to control the login page design.
    
    """
    
    def __init__(self,window_object):
        super().__init__(window_object,bg="sky blue",width=1920,height=1080)
        self.pack(anchor=tk.S)
        #Hospital_name_Frame=Frame(window_object)

        
    

    
     



        
    




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


    