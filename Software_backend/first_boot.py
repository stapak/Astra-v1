"""
This file is for getting software ready with creating a database,cloud.
"""
from . import cursor_object



def create_database(cursor_object,hospital_name):
    """
    This function runs at the start of the software and is executed only once for setting up the initial database.
    """
    
    query=f"""
    CREATE DATABASE IF NOT EXIST {hospital_name}
    """
    cursor_object.execute(query)
    
    query2=f"""
    USE DATABASE {hospital_name}
    """
    cursor_object.execute(query2)

    query3="""
    CREATE TABLE IF NOT EXIST patient_list(
    patient_id INT PRIMERY KEY AUTO_INCREMENT,
    patient_name VARCHAR(50),
    patent_DOB DATE,
    phone_no INT,
    blood_group VARCHAR(3),
    patient_adderess VARCHAR(100),
    initial_diagnostic VARCHAR(1000),    
    doctor_name VARCHAR(50)
    );
    """
    cursor_object.execute(query3)


def start_boot(hospital_name):
    create_database(cursor_object,hospital_name)

