"""
This file is used to start the software.
"""

# Built in liabraries.
import json
import mysql.connector



#-------------------------- Astra modules ------------------------------------------


#--------- Backend Modules --------------------------
from Software_backend import *



#-------- Front End Modules
from Software_UI import *


with open('software_info.json') as file_object:
    bootup_info=json.load(file_object)
    

# If 'setup_complete' variable has true value then bootup software will be called.
if bootup_info['setup_complete']:
    pass
else:
    pass



