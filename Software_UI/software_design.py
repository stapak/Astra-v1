"""
Contains all the frames for the dashboard for the staff of the hospital.

"""


from software_windows import *
from tkinter import Frame
from tkinter import Label
import tkinter as tk
from tkinter import StringVar
import json


with open( os.path.join(os.path.dirname(os.path.realpath(__file__)), 'basic_info.json'),encoding='utf-8' ) as fobj:
    basic_info=json.load(fobj)["hospital info"]


class Login_page():
    """
    Used to control the login page design.
    
    """
    
    def __init__(self,window_object):
        self.window_object=window_object
        background_frame=Frame(window_object,bg="sky blue",width=1920,height=1080)
        background_frame.pack()
        Hospital_name_Frame=Frame(background_frame,bg="black",width=400,height=60)
        Hospital_name_Frame.grid(row=5,column=5)
        
        if basic_info['hospital_name'] == None:
            return 
        else:
            text_var=StringVar()
            text_var.set(basic_info["hospital_name"])

        #Hospital_name_label=Label(Hospital_name_Frame,textvariable=text_var)
        #Hospital_name_label.pack(anchor=tk.N)


        
    

    
     



        
    




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

    
    #print(basic_info)

    