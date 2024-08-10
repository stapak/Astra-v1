"""
File contains general function used by all users.
"""

import json
import mysql.connector


# Astra modules

from . import _SOFTWARE_INFO_FILE_PATH

with open(_SOFTWARE_INFO_FILE_PATH,'r') as fobj:
    host_info=json.load(fobj)['host']

def start_dashboard(role):
    pass



def login(**data):
    global host_info
    database_object=mysql.connector.connect(user=data['user id'],
                                            passwd=data['user password'],
                                            host=host_info)
    cursor_object=database_object.cursor()
    return cursor_object
    
def get_departments(cursor_object):
    """
    This funciton is used to get the list of the department
    INPUT:
    *cursor_object: object of the cursor for executing query.
    
    OUTUPUT:
    returns all the name of the departments in formated list .
    """
    query="""
    select dept_name from departments;
    """
    cursor_object.execute(query)
    dept_names=[]
    for i in cursor_object.fetchall():
        dept_names.append(i[0])
    return dept_names



    
    