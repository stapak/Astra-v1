"""
This file has functions to start in various formats such as 'setup software','run software' etc.
"""

#-------------------------------------------------- Modules ---------------------------------------------------------------------------------

#----------------------------------Built in liabraries--------------

import json
import mysql.connector



#-------------------------- Astra modules ------------------------------------------

# Backend Modules 
from Software_backend.software_setup import Software_setup


#Frontend Modules 
import Software_UI.setup_frames as setup_frames
from Software_UI.software_windows import Window



#--------------------------- Actual code -------------------------------------------------------------------------------------------


#-------------------- setup page related funtions --------------------------------

"""
Created a common frames list which is base for all software function depending on setup or work frames are 
added to this list by other function.

"""
frames_list=[]

current_page=0
class SwitchPages:
    """
    This class contains functions used to switch between pages.
    """
    @staticmethod
    def switch_back():
        global current_page
        current_page=current_page-1
        frame=frames_list[current_page]
        frame.tkraise()
        frame.place(x=0,y=0)
        
    
    @staticmethod
    def switch_front():
        global current_page
        current_page=current_page+1
        frame=frames_list[current_page]
        frame.tkraise()
        frame.place(x=0,y=0)
        
        

def start_setup():
    """
    Function used to pack pages by creating class objects and append them in frames list
    """
    #Initailizing window object
    window=Window()
    window_object=window.setup_window()
    
    #Initializing 1st page.
    setup_page_1=setup_frames.Welcome_page(window_object,SwitchPages)
    
    #Initailizing 2nd page.
    setup_page_2=setup_frames.Terms_condition_page(window_object,SwitchPages)
    
    #Initailizing 3rd page.
    def mediator_function_3rd(key):
        return Software_setup.license_key_verification(key)
    setup_page_3=setup_frames.Software_activation_page(window_object,SwitchPages,verify_function=mediator_function_3rd)
    
    #Initializing 4th page
    global hospital_name
    def mediator_function_4th(name):
        global hospital_name
        hospital_name=name
        Software_setup.register_hospital_name(name)
    setup_page_4=setup_frames.Name_registration_page(window_object,SwitchPages,register_name=mediator_function_4th)
    
    #Initializing 5th page
    user_data={}
    def mediator_function_5th(id,password,host):
        global user_data
        
        user_data={'host':host,
                   'user id':id,'user password':password}
        return Software_setup.database_verification(**user_data)
        
    setup_page_5=setup_frames.Admin_setup_page(window_object,SwitchPages,DBMS_verification=mediator_function_5th)

    #Initializing 6th page.
    def mediator_function_6th():
        global user_data
        global hospital_name
        user_data['hospital name']=hospital_name
        return Software_setup.setup_database(**user_data)
    setup_page_6=setup_frames.DBMS_setup_page(window_object,SwitchPages,dbms_setup_function=mediator_function_6th)
    
    #Initializing 7th page.
    def mediator_function_8th():
        frames_list[0:6]
        del frames_list[0]#this line will be executed after all elements of list are deleted hence last page will be of index 0.
        return None
    setup_page_7=setup_frames.setup_finish_page(window_object,finish_setup=mediator_function_8th)

    # Adding every frame to list.
    frames_list.append(setup_page_1)
    frames_list.append(setup_page_2)
    frames_list.append(setup_page_3)
    frames_list.append(setup_page_4)
    frames_list.append(setup_page_5)
    frames_list.append(setup_page_6)
    frames_list.append(setup_page_7)
   
   
    
    window_object.mainloop()
    
    
    

    




with open('software_info.json') as file_object:
    bootup_info=json.load(file_object)


# If 'setup_complete' variable has true value then bootup software will be called.
if bootup_info['setup_complete']:
    pass
else:
    pass



if __name__=='__main__':
    start_setup()
    pass