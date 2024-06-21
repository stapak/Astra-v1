"""
This file is for getting software ready with creating a database,cloud.
"""

# built-in libraries

import os
import mysql.connector
import json
from werkzeug.security import check_password_hash

# Astra libraries
from .projectExceptions import HostError,WrongUserInformation


class Software_setup:
    """
    This class contains all the functions necessary for seting up software.
    """    
    @staticmethod
    def license_key_verification(license_key):
        """
        This function will be used inside 'setup software' file's 'software activation page' frame.
        This function is used to test license key enterd by user        
        """
        jsonfile=os.path.join(os.path.dirname(os.path.realpath(__file__)),'license_keys.json')
        with open(jsonfile,encoding='utf-8' ) as jsonobj:
            license_keys=json.load(jsonobj)["license keys"]
        for key in license_keys:
            if check_password_hash(key,license_key):
                jsonfile2=os.path.join(os.path.dirname(os.path.realpath(__file__)),'boot_info.json')
                with open(jsonfile2,encoding='utf-8' ) as jsonobj:
                    boot_info=json.load(jsonobj)
                boot_info["Hospital_lienced"]=True
                with open(jsonfile2,'w',encoding='utf-8') as jsonobj:
                    json.dump(boot_info,jsonobj,indent=6)

                return True
        return False
    
    @staticmethod
    def register_hospital_name(hospital_name:str):
        """
        This function will be used inside 'setup software' file's 'register hospital name' frame. 
        This register hospital name        
        """
        jsonfile=os.path.join(os.path.dirname(os.path.realpath(__file__)),'boot_info.json')
        with open(jsonfile,encoding='utf-8' ) as jsonobj:
            boot_info=json.load(jsonobj)
        
        boot_info["Hospital_Name"]=hospital_name
        
        with open(jsonfile,'w',encoding='utf-8') as jsonobj:
            json.dump(boot_info,jsonobj,indent=6)
    
    @staticmethod
    def database_verification(**data):
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
        
        database_object.close()
        return None
        
    
    @staticmethod
    def setup_database(**data):
        """
        Function used to setup database using database setup class and it's method.
        """
        database_object=mysql.connector.connect(host=data['host'],
                                                user=data['user'],
                                                passwd=data['password'])
        cursor_object=database_object.cursor()
        database_setup=Database_setup(cursor_object,data['hospital_name'])
        execution_list=[database_setup.create_database(),
                        database_setup.use_database(),
                        database_setup.create_staff_table(),
                        database_setup.create_departmetns_list(),
                        database_setup.create_doctors_list(),
                        database_setup.create_patient_list(),
                        database_setup.create_pharmacy_info(),
                        database_setup.create_login_info(),
                        database_setup.create_appointment_list(),
                        database_setup.create_medicine_list()
                        ]
        return execution_list
        
       
    @staticmethod
    def finish_setup(*class_objects):
        for i in class_objects:
            del i
            
        


class Database_setup:
    """
    This class contains all the methods to setup database.
    """
    def __init__(self,cursor_object,hospital_name):
        self.cursor_object=cursor_object
        self.hospital_name=hospital_name
              
    
    def create_database(self):
        """
        This function used to create database.
        """
        query=f"""
        CREATE DATABASE IF NOT EXISTS {self.hospital_name};
        """
        self.cursor_object.execute(query)
        return True
    
    def use_database(self):
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
        post ENUM("IT","recetionist") NOT NULL,
        ID_proof VARCHAR(20) NOT NULL,
        ID_number VARCHAR(25) NOT NULL,
        registrer_ID VARCHAR(15) NOT NULL,
        user_password VARCHAR(50) NOT NULL,
        login_status BOOLEAN NOT NULL
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
        
    
    def create_login_info(self):
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
        permanent_address VARCHAR(200) NOT NULL,
        initial_problem VARCHAR(200) NOT NULL,
        initial_diagnose VARCHAR(500) NOT NULL,
        department_id VARCHAR(20) NOT NULL,
        doctor_id VARCHAR(20) NOT NULL,
        registrer_id VARCHAR(20) NOT NULL,
        treatment_completed TINYINT DEFAULT 0 ,
        treatment_conclusion VARCHAR(500),
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
    #key=input("Enter the license key:")
    #print(Software_setup.license_key_verification(key))
    #Software_setup.register_hospital_name(50)
    print(Software_setup.setup_database(host='localhost',user='test',password='test',hospital_name="Testing"))