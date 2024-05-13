"""
This file is used to start the software.
"""

# Built in liabraries.
import json
import mysql.connector

# Created Modules.
from Software_backend.software_setup import start_boot


# the variable username and password will be shared later.
user_name=user_name
password=password



def create_cursor_object(user_name,password,DB_name,host_address):
    db=mysql.connector.connect(host=host_address,user=user_name,passwd=password,database=DB_name)
    cusor_object=db.cursor()
    return cusor_object



