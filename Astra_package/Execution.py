# File for execution to execute the software setup or user logins.


#--------------------- Built-ins ----------------------------------
import mysql.connector
import os 
import json


#--------------------- Astra libraries ----------------------------

from .Software_backend.projectExceptions import WrongUserInformation,HostError
from .setupExecution import start_setup


#------------------ Variables to be used in other modules of the package  -------------------







def Login(*data):
    """
    Function to login user
    """
    def database_verification(**data):
        try:
            database_object=mysql.connector.connect(host=data['host'],
                                                user=data['user id'],
                                                passwd=data['user password'])
        except mysql.connector.errors.ProgrammingError:
            return WrongUserInformation
        except mysql.connector.errors.DatabaseError:
            return HostError
        except Exception as E:
            return E



def Execute():
    """
    Function to check the setup, if basic details json file is not found it will restart setup.
    """
    jsonfile=os.path.join(os.path.dirname(os.path.realpath(__file__)),'Software_backend\license_keys.json')
    
    # Reading for the presence of json file 
    global _SOFTWARE_INFO_FILE_PATH
    with open(jsonfile) as jobj:
        _SOFTWARE_INFO_FILE_PATH=json.load(jobj)['boot file path']
    if not _SOFTWARE_INFO_FILE_PATH:
        start_setup()
    else:
        pass