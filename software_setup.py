import json

path="credentials.json"
with open(path) as obj:
    cred=obj.load(obj)["cred"]


def first_setup(cursor_object,hosptal_name):
    """
    This function runs at the start of the software and is executed only once for setting up the initial database.
    """
    query=f"""
    CREATE DATABASE IF NOT EXIST {hosptal_name}
    """
    cursor_object.execute(query)

    query2="""
    CREATE TABLE IF NOT EXIST patient_list(
    patient_id INT PRIMERY KEY,
    patient_name VARCHAR(50),
    phone_no INT,
    blood_group VARCHAR(3),
    patient_adderess VARCHAR(100),
    initial_diagnostic VARCHAR(1000),    
    doctor_name VARCHAR(50)
    );
    """
    cursor_object.execute(query2)


    