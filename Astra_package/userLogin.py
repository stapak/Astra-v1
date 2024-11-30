# File to access the user's frame and present them.

#------------------ built-in libraries ------------------------------
import mysql.connector
import json
import os
import time



#------------------ Astra package -----------------------------------
from .Software_UI.general_frames import LoginPage
from .Software_UI.software_windows import Window



#------------------ Interface Modules -------------------------------
from .Software_UI import IT_interface as ITUI
from .Software_UI import reception_interface as receUI
from .Software_UI import doctor_interface_frames as DocUI



#----------------- Backend Modules ----------------------------------
from .Software_backend.IT_backend import IT_head_functions as ITB



#------------------ Variables for Modules ----------------------------
jsonfile=os.path.join(os.path.dirname(os.path.realpath(__file__)),'Software_backend\license_keys.json')
    
    # Reading for the presence of json file 
global _SOFTWARE_INFO_FILE_PATH
with open(jsonfile) as jobj:
    _SOFTWARE_INFO_FILE_PATH=json.load(jobj)['boot file path']

if  _SOFTWARE_INFO_FILE_PATH:
    with open(_SOFTWARE_INFO_FILE_PATH,'r') as jobj:
            software_info=json.load(jobj)
            HOST_ADDRESS=software_info['host']
            DatabaseName=software_info['Hospital_Name']
    
WindowObject=None # Used to store root window object tk class.
CurrentInterface=None # Used to store object of the current frame.
GeneratedInterface={} # Dictionary used to generate and store object of the frame with the interface name.
CursorObject=None # Used to store cursor object of the database.
UserRole=None # Used to store user role .




def login_user(**login_credentials):
    """
    Function to connect to mysql server to check user credetials of user and 
    create a database object and store it .
    Takes arguments:
    *An dictionary with credential of user from LoginPage frame.
    """
    global database_object # Variable to export database object .
    global HOST_ADDRESS    # Variable to import host address from json file.
    global UserRole    # Variable to export user role for loading frame.
    global DatabaseName    
    global CursorObject
    database_object=mysql.connector.connect(user=login_credentials['user name'],passwd=login_credentials['password'],host=HOST_ADDRESS,database=DatabaseName)
    CursorObject=database_object.cursor()
    
    # Query to get the role of the user.
    query=f"""SHOW GRANTS FOR '{login_credentials["user name"]}'@'{HOST_ADDRESS}' ;"""
    CursorObject.execute(query)
    response=str(CursorObject.fetchall()[-1])
    if response.find("DOCTOR") != -1 :
        pass
    elif response.find("receptionist") != -1 :
        pass 
    elif response.find("lab_technician") != -1 :
        pass
    elif response.find("IT"):
        UserRole="IT"
        return True
    
    



def ShowLoginPage():
    """
    Function called to create login page object and 
    
    """
    window_root=Window()
    window_root=window_root.login_window()
    global UserRole
    def destroy_login():
        """
        This internal function is to destroy the login page root.
        this function takes :
        *Root of the window to destroy.
        """
        global UserRole
        window_root.destroy()
        print(UserRole)
        GenerateUserInterface(UserRole)
    
    login_page=LoginPage(window_root,login_user,destroy_login)
    window_root.mainloop()





def ChangeFrame(frame_name):
    """
    Function to change function.
    Arguments:
    *Name of the frame to change.
    """
    FUNCTION_NAME='Change Frame'
    GeneratedInterface[frame_name].tkrise()
    




def GenerateUserInterface(User_role:str):
    """
    Function to generate all user interface for role and load all the objects of the frame and store
    them in the dictionary with frame name as key
    Arguments taken:
    *User_role - User role in string form
    
    """
    print("Entert the function")
    global GeneratedInterface
    global WindowObject
    global CurrentInterface
    global CursorObject
    BackendFunctions={ 'Change Frame':ChangeFrame } # dictionary to store backend functions of the respected user role.    

    WindowObject=Window()
    WindowObject=WindowObject.normal_window()
    match User_role:
        case "IT":
            BackendFunctions['login register']=ITB.login_register
            BackendFunctions['add departments']=ITB.add_departments
            BackendFunctions['add hospital staff']=ITB.add_hospital_staff
            BackendFunctions['add pharmacy']=ITB.add_pharmacy
            BackendFunctions['change user password']=ITB.change_user_passwrod
            BackendFunctions['execute query']=ITB.execute_query
            BackendFunctions['cursor object']=CursorObject
            
            dashboard_object=ITUI.ITDashBoard(window_object=WindowObject,backend_functions=BackendFunctions)
            GeneratedInterface['DashBoard']=dashboard_object

            GeneratedInterface['DashBoard'].tkraise()
        case "doctor": 
            pass
        case "receptionist":
            pass
        case "lab_technician":
            pass
        case "pharmacist":
            pass
        case _:
            pass
