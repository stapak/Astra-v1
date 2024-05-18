"""
This file contains all the code related to the setup window of the software
"""

from software_windows import Window
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import PhotoImage
import tkinter as tk
import json
import os

#---------------------------------------Variable/attributes of file ---------------------------------------




with open( os.path.join(os.path.dirname(os.path.realpath(__file__)),'setup_page_info.json'),encoding='utf-8' ) as fobj:
    welcome_greeting=json.load(fobj)["welcome_greeting"]




#--------------------------------------class of file-------------------------------------------------------


class Welcome_page(Frame):
    def __init__(self,window_object):
        self.window_oject=window_object
        super().__init__(window_object,bg="light grey",width=700,height=500)
        self.pack(fill="x")

        #------------------------------ Image Frame----------------------------------------

        image_frame=Frame(self,bg="#0076CE",width=300,height=450,relief=tk.RIDGE)
        image_frame.place(x=0,y=0)
        #window_icon=PhotoImage(file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'software_icon.png'))
        #window_icon_label=Label(image=window_icon)
        #window_icon_label.pack()


        #-------------------------------Information frame----------------------------------
        details_frame=Frame(self,bg="#DCDCDC",height=450,width=500)
        details_frame.place(x=201,y=0)

        next_button=Button(self,text="Next",relief="groove",width=10)
        next_button.place(x=590,y=460)



class Terms_condition_page(Frame):
    """
    This class is used to code second page of startup which is terms and condition page.

    """
    def __init__(self,window_object):
        self.window_oject=window_object
        super().__init__(window_object,bg="light grey",width=700,height=500)
        self.pack(fill="x")

class Software_activation_page:
    pass

class Name_registration_page:
    pass

class DBMS_setup_page:
    pass
    
class Root_setup_page:
    pass

class Cloud_setup_page:
    pass

    


        
        



if __name__=='__main__':
    root=Window()
    root=root.setup_window()
    setup_page=Welcome_page(root)
    root.mainloop()
