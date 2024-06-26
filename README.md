# Project : Astra v1
Aim : A Medical software to manage hospital staff and hospital services.

## Technologies :
* Python programming language
* MySQL 
* tkinter

## Working :
1. ***User Interface*** is constructed using python tkinter library, and UI modules are packed in **Software_UI** subpackage.
1. ***Backend*** is constructed using python and MySQL-connector and Backend modules are packed in **Software_backend** subpackage.
1. ***Database*** Database is based on **MySQL** database,queries are written inside functions and when funtions are invoked queries are executed. 


## Features: 
1. User Managment(hospital staff)
1. Patient Management(patients personal detials,Medications,Session Outcome)
1. Database Managment System
1. Good graphical User Interface
<!-- 1. Cloud File Managment(if possible) -->

***
## Feature Description
### 1.User Managment:
Requirements: 
        a.Every staff should be access all patients from the database.
        b.Every staff should be able to access only the specific amount of data about the patient related to the work of the staff.
        c.From the same login interface for every user, based on the user new dashboard.

### 2. Patient Managment:

   Requirements: 
   a.should contain pesonal details(patient id,name,address,health diagnostic info) 
   b.able to be used by multiple hospital staff(doctor booking by front desk,health report edited by doctors,dianostic reports by diagnostic center,pharmacists to medicines
   c.Should be able maintain records (such asevery session,current medications and treatments,future session dates and necessary diagnostics before session and other).
   d.If possible it should maintain a digital copy of every diagnostic (such as mri reports,blood test reports etc.)
    
   