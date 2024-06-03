"""
This File contain window related settings.

"""

from tkinter import *
from tkinter import PhotoImage
import json
import os
import time


     
class Window:
    """
    Creates window objects and sets basic settings 
    """
    def __init__(self):
        pass

    def _create_window(self):
        root =Tk()
        root.title('Astra Hospital Management')
        window_icon=PhotoImage(file=os.path.join(os.path.dirname(os.path.realpath(__file__)), 'software_icon.png'))
        root.iconphoto(False,window_icon)
        return root

    #--------------------window with different sizes------------------------------
    def normal_window(self):
        self.root_object=self._create_window()
        width=1535
        height=780
        self.root_object.geometry(f'{width}x{height}')
        self.root_object.maxsize(width,height)
        return self.root_object
    
    def setup_window(self):
        self.setting_window_root=self._create_window()
        width=550
        height=400
        self.setting_window_root.geometry(f'{width}x{height}')
        self.setting_window_root.resizable(width=False,height=False)
        return self.setting_window_root
    
    def login_window(self):
        self.login_root=self._create_window()
        width=700
        height=500
        self.login_root.geometry(f'{width}x{height}')
        self.login_root.resizable(width=False,height=False)
        return self.login_root



   


     




if __name__=='__main__':
      
      window_root=Window()
      #window_root=window_root.setup_window()
      window_root=window_root.normal_window()
      #window_root=window_root.login_window()
      window_root.mainloop()
      
      
      