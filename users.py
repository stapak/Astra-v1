import mysql.connector

class User:
    def __init__(self):
        self.authority={
            # authority related to adding and removing users
            "add_doctor":False,
            "remove_doctor":False,

            "add_receptionist":False,
            "remove_receptionist":False,

            "add_diagnostic_center":False,
            "remove_diagnostic_center":False,

            "add_pharmacists":False,
            "add_pharmacists":False

            # authority to 
            
        }
