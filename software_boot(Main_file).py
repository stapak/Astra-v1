"""
This file is used to start the software.
"""

#-------------------------------------------------- Modules ---------------------------------------------------------------------------------

#----------------------------------Built in liabraries--------------
import json
from turtle import setup
import mysql.connector


#-------------------------- Astra modules ------------------------------------------

# Backend Modules 
from Software_backend import *
from Software_backend.software_setup import Database_setup


#Frontend Modules 
from Software_UI.setup_frames import *
from Software_UI.software_windows import Window



#--------------------------- Actual code -------------------------------------------------------------------------------------------


#-------------------- setup page related funtions --------------------------------


setup_frames_list=[]
current_page=0
window=Window()
window_root=window.setup_window()
setup_page1_object=Welcome_page(window_root)
setup_frames_list.append(setup_page1_object)
print(setup_frames_list)
    


class SwitchPages:
    """
    This class contains functions used to switch between pages.
    """
    @staticmethod
    def switch_back():
        frame=setup_frames_list[current_page-1]
        frame.tkrise()
    
    @staticmethod
    def switch_front():
        frame=setup_frames_list[current_page+1]
        frame.tkrise()
        

with open('software_info.json') as file_object:
    bootup_info=json.load(file_object)


# If 'setup_complete' variable has true value then bootup software will be called.
if bootup_info['setup_complete']:
    pass
else:
    pass




