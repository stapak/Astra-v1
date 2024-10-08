# File to access the user's frame and present them.

#------------------ built-in libraries ------------------------------
import mysql.connector
import json



#------------------ Astra package -----------------------------------
from .Software_UI.general_frames import LoginPage
from .Software_UI.software_windows import Window
from .Execution import _SOFTWARE_INFO_FILE_PATH



#------------------ Interface Modules -------------------------------
from .Software_UI import IT_interface as ITUI
from .Software_UI import reception_interface as receUI
from .Software_UI import doctor_interface_frames as DocUI



#----------------- Backend Modules ----------------------------------
from .Software_backend import IT_backend as ITB



#------------------ Variables for Modules ----------------------------
with open(_SOFTWARE_INFO_FILE_PATH,'r') as jobj:
        host_address=json.load(jobj)['host']

WindowObject=None # Used to store root window object tk class.
CurrentInterface=None # Used to store object of the current frame.
GeneratedInterface={} # Dictionary used to generate and store object of the frame with the interface name.



def login_user(**login_credentials):
    """
    Function to connect to mysql server to check user credetials of user and 
    create a database object and store it .
    Takes arguments:
    *An dictionary with credential of user from LoginPage frame.
    """
    global database_object # Variable to export database object .
    global host_address    # Variable to import host address from json file.
    global user_role       # Variable to export user role for loading frame.
    
    database_object=mysql.connector.connect(user=login_credentials['user name'],passd=login_credentials['password'],host=host_address)
    cursor_object=database_object.cursor()
    
    # Query to get the role of the user.
    query=f'SHOW GRANTS FOR {login_credentials["user name"]} ;'
    cursor_object.execute(query)
    response=str(cursor_object.fetchall()[1])
    if response.find("DOCTOR") != -1 :
        pass
    elif response.find("receptionist") != -1 :
        pass 
    elif response.find("lab_technician") != -1 :
        pass
    elif response.find(""):
        pass 
    
    

def ShowLoginPage():
    """
    Function called to create login page object and 
    
    """
    window_root=Window()


    def destroy_login():
        """
        This internal function is to destroy the login page root.
        this function takes :
        *Root of the window to destroy.
        """
        global login_root
        login_root.destroy()
    
    login_page=LoginPage(window_root,login_user,destroy_login)
    




def ChangeFrame(frame_name):
    """
    Function to change function.
    Arguments:
    *Name of the frame to change.
    """
    GeneratedInterface[frame_name].tkrise()
    
