/*-----------------------------------------------------------------------BACKEND commads---------------------------------------------------*/
/*-------------------------------1st commad : to create database with name of hospital,-----------------------*/
CREATE DATABASE dummy_hospital;

/*-------------------------------2nd commad: To use the database,---------------------------------------------*/
USE  dummy_hospital;

/*---------------------3rd commad: To create hospital staff database---------------------------------------*/
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
/*----------------------------------------------------------------------------------------------------------*/
DROP table pharmacy_info;

/*----------------------------4th command: To create table related to doctor's data------------------------------*/
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
/*----------------------------------------------------------------------------------------------*/

drop table doctor_info;

/*-------------------------5th commad: To create table related to pharmacy-------------------------------------*/
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
/*-------------------------------------------------------------------------------------*/


/*-----------------------------6th command : To create table related to login info----------------------------*/
CREATE TABLE login_info(
user_id VARCHAR(20) NOT NULL,
login_time_date DATETIME NOT NULL,
logout_time_date DATETIME NOT NULL,
FOREIGN KEY (user_id) REFERENCES hospital_staff(staff_id),
FOREIGN KEY (user_id) REFERENCES doctors_list(doctor_id),
FOREIGN KEY (user_id) REFERENCES pharmacy_info(pharmacist_id)
);
/*----------------------------------------------------------------------------------------------*/

drop table login_info;

/*--------------------------------7th command : To create table related to department--------------------------------------------*/
CREATE TABLE departments(
dept_id VARCHAR(20) NOT NULL PRIMARY KEY,
dept_name VARCHAR(20) NOT NULL ,
total_doctors INT 
);
/*------------------------------------------------------------------*/


/*------------------------8th command : To create patient table-----------------------------------*/
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

/*------------------------------------------------------------------*/
drop table patient_list;

alter table patient_list modify patient_id varchar(20) not null;

/*---------------------------------9th command : To create table related to book session for doctor and show it on doctor interface----------------------------------*/

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
/*-----------------------------------------------------------------------------*/

/*------------------- 10th command : To create medicine table --------------------------------------------------------------------------------------*/
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


