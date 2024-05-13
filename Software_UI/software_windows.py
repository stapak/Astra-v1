"""
This File contain window related settings.

"""




from tkinter import *
import json
import os
import time



class Window:
    """
    Creates window objects and sets basic settings 
    """
    def __init__(self):
        pass

    def create_window(self):
        root =Tk()
        root.title('Astra Hospital Management')
        return root

    #--------------------window with different sizes------------------------------
    def normal_window(self):
        root_object=self.create_window()
        width=1080
        height=720
        self.root_object.geometry(f'{width}x{height}')
        return root_object


   


     




if __name__=='__main__':
      
      window_root=Window()
      window_root.start_window()
      window_root.start_window()
      
      