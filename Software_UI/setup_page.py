from software_windows import Window
from tkinter import Frame
import tkinter as tk
import json
import os


with open( os.path.join(os.path.dirname(os.path.realpath(__file__)), 'setup_page_info.json'),encoding='utf-8' ) as fobj:
    welcome_greeting=json.load(fobj)["welcome_greeting"]


class Setup_page:
    def __init__(self,window_object):
        self.window_oject=window_object
        root_frame=Frame(window_object,bg="#0076CE",width=700,height=500)
        root_frame.pack()

    
    def welcome_page(self,window_object):

        
        













if __name__=='__main__':
    root=Window()
    root=root.setup_window()
    Setup_page(root)
    root.mainloop()
    
    #print(welcome_greeting)