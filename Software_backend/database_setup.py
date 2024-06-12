"""
This file is for getting software ready with creating a database,cloud.
"""

import mysql.connector

# Software liabraries
from projectExceptions import HostError,WrongUserInformation

class database_setup:
    """
    This class contains all the methods to setup database.
    """
    def __init__(self,cursor_object,hospital_name):
        self.cursor_object=cursor_object
        self.hospital_name=hospital_name
        
    @staticmethod
    def verify_database_user(**data):
        try:
            database_object=mysql.connector.connect(host=data['host'],
                                                user=data['host'],
                                                passwd=data['password'])
        except mysql.connector.errors.ProgrammingError:
            return WrongUserInformation
        except mysql.connector.errors.DatabaseError:
            return HostError
        except Exception as E:
            return E
        
    
    def create_database(self):
        """
        This function used to create database.
        """
        query=f"""
        CREATE DATABASE IF NOT EXIST {self.hospital_name};
        """
        self.cursor_object.execute(query)
        return True
    
    def using_database(self,**use_database_data):
        """
        This function used to pass command 'USE DATABASE'.
        """
        
        query=f"""
        USE {self.hospital_name};
        """
        self.cursor_object.execute(query)
        return True
    
    def create_staff_table(self):
        """
        Function is used to create staff table.
        """
        query="""
        CREATE TABLE hospital_staff(
        staff_id VARCHAR(20) PRIMARY KEY NOT NULL,
        name VARCHAR(50) NOT NULL,
        date_of_birth DATE NOT NULL,
        contact INT NOT NULL,
        contact2 INT ,
        education VARCHAR(100) NOT NULL,
        current_address VARCHAR(200) NOT NULL,
        permanent_address VARCHAR(200) NOT NULL,
        post  ENUM("IT","recetionist") NOT NULL,
        ID_proof VARCHAR(20) NOT NULL,
        ID_number VARCHAR(25) NOT NULL,
        registrer_ID VARCHAR(15) NOT NULL,
        user_password VARCHAR(50) NOT NULL,
        login_status BOOLEAN NOT NULL
        );
        """
        self.cursor_object.execute(query)
        return True
    
    def create_doctors_list(self):
        """
        Fucntion used to create doctors list.
        """
        query="""
        CREATE TABLE doctors_list(
        doctor_id VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        ID_proof VARCHAR(30) NOT NULL,
        id_no VARCHAR(30) NOT NULL,
        current_address VARCHAR(200) NOT NULL,
        permanent_address VARCHAR(200) NOT NULL,
        contact INT NOT NULL,
        contact2 INT,
        education VARCHAR(100) NOT NULL,
        post VARCHAR(20) NOT NULL,
        registrer_id VARCHAR(20) NOT NULL,
        password VARCHAR(30) NOT NULL,
        login_status BOOLEAN NOT NULL,
        dept_id VARCHAR(20) NOT NULL,
        FOREIGN KEY (registrer_id) REFERENCES hospital_staff(staff_id),
        FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        );
        """
        self.cursor_object.execute(query)
        return True
    
    def create_pharmacy_info(self):
        """
        Fucntion used to create pharmacy info table.
        """
        query="""
        CREATE TABLE pharmacy_info(
        pharmacist_id VARCHAR(20) PRIMARY KEY,
        name VARCHAR(50) NOT NULL,
        ID_proof VARCHAR(30) NOT NULL,
        id_no VARCHAR(30) NOT NULL,
        current_address VARCHAR(200) NOT NULL,
        permanent_address VARCHAR(200) NOT NULL,
        contact INT NOT NULL,
        contact2 INT,
        education VARCHAR(100) NOT NULL,
        registrer_id VARCHAR(20) NOT NULL,
        password VARCHAR(30) NOT NULL,
        login_status BOOLEAN NOT NULL,
        FOREIGN KEY (registrer_id) REFERENCES hospital_staff(staff_id)
        );
        """
        self.cursor_object.execute(query)
        return True
        
    
    def create_loign_info(self):
        """
        Fucntion used to create table storing login info.
        """
        query="""
        CREATE TABLE login_info(
        user_id VARCHAR(20) NOT NULL,
        login_time_date DATETIME NOT NULL,
        logout_time_date DATETIME NOT NULL,
        FOREIGN KEY (user_id) REFERENCES hospital_staff(staff_id),
        FOREIGN KEY (user_id) REFERENCES doctors_list(doctor_id),
        FOREIGN KEY (user_id) REFERENCES pharmacy_info(pharmacist_id)
        );
        """
        self.cursor_object.execute(query)
        return True
    
    def create_departmetns_list(self):
        """
        Fucntion used to create departments list.
        """
        query="""
        CREATE TABLE departments(
        dept_id VARCHAR(20) NOT NULL PRIMARY KEY,
        dept_name VARCHAR(20) NOT NULL ,
        total_doctors INT 
        );
        """
        self.cursor_object.execute(query)
        return True
    
    def create_patient_list(self):
        """
        Fucntion used to create patinet list.
        """
        query="""
        CREATE TABLE patient_list(
        patient_id VARCHAR(20) PRIMARY KEY NOT NULL,
        f_name VARCHAR(20) NOT NULL,
        l_name VARCHAR(20),
        DOB DATE NOT NULL ,
        age INT NOT NULL ,
        proof_id VARCHAR(20) NOT NULL,
        proof_no VARCHAR(20) NOT NULL,
        blood_group VARCHAR(3) NOT NULL,
        gender VARCHAR(10) NOT NULL,
        contact_no INT NOT NULL,
        contact_no2 INT,
        house_no VARCHAR(10) NOT NULL,
        building_name VARCHAR(10) NOT NULL,
        land_mark varchar(10) NOT NULL,
        town VARCHAR(20) NOT NULL,
        district VARCHAR(20) NOT NULL,
        state VARCHAR(20) NOT NULL,
        contry VARCHAR(20) NOT NULL,
        pincode INT NOT NULL,
        initial_problem VARCHAR(200) NOT NULL,
        initial_diagnose VARCHAR(500) NOT NULL,
        department_id VARCHAR(20) NOT NULL,
        doctor_id VARCHAR(20) NOT NULL,
        registrer_id VARCHAR(20) NOT NULL,
        treatment_completed TINYINT DEFAULT 0 ,
        FOREIGN KEY (department_id) REFERENCES departments(dept_id),
        FOREIGN KEY (doctor_id) REFERENCES doctors_list(doctor_id),
        FOREIGN KEY (registrer_id) REFERENCES hospital_staff(staff_id)
        );
        """
        self.cursor_object.execute(query)
        return True
    
    def create_appointment_list(self):
        """
        Fucntion used to create doctor's appointmetn list.
        """
        query="""
        CREATE TABLE appointment_list(
        task_id VARCHAR(20) NOT NULL,
        given_by VARCHAR(20) NOT NULL,
        given_to VARCHAR(20) NOT NULL,
        patient_id VARCHAR(20) NOT NULL,
        given_time_date DATETIME NOT NULL,
        task_date_time DATETIME NOT NULL,
        FOREIGN KEY (given_by) REFERENCES hospital_staff(staff_id),
        FOREIGN KEY (given_to) REFERENCES doctors_list(doctor_id),
        FOREIGN KEY (patient_id) REFERENCES patient_list(patient_id)
        );
        """
        self.cursor_object.execute(query)
        return True
    
    def create_medicine_list(self):
        """
        Fucntion used to create medicine list.
        """
        query="""
        CREATE TABLE medicine_list(
        medicine_id VARCHAR(20) NOT NULL,
        medicine_name VARCHAR(100) NOT NULL,
        storage_instruciton VARCHAR(200) ,
        manufactured_date DATE ,
        expiry_date DATE NOT NULL,
        medicine_cost INT NOT NULL,
        registerer_id VARCHAR(20) NOT NULL,
        FOREIGN KEY (registerer_id) REFERENCES pharmacy_info(pharmacist_id)
        );

        """
        self.cursor_object.execute(query)
        return True
    

if __name__=='__main__':
    pass