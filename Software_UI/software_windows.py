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
        return root

    #--------------------window with different sizes------------------------------
    def normal_window(self):
        self.root_object=self._create_window()
        width=1920
        height=1080
        self.root_object.geometry(f'{width}x{height}')
        window_icon=PhotoImage(file='E:\Mini Project\Astra v1\Software_UI\software_icon.png')
        self.root_object.iconphoto(False,window_icon)
        return self.root_object


   


     




if __name__=='__main__':
      
      window_root=Window()
      window_root.start_window()
      
      
      