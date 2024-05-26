"""
This file is for getting software ready with creating a database,cloud.
"""



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


def create_DB_staff(cursor_object,user_name,password):
    """
    Fucntion used to create user for database and connect that user to the database.
    This function has access restriction and can only be used by head of the department.
    """
    pass




def start_boot(cursor_object,hospital_name):
    """
    Fucntion used to start/boot the software.This function uses call the function internally and use them for necessary start
    the soft ware.
    """
    create_database(cursor_object,hospital_name)

