import mysql.connector
from projectExceptions import NotAuthorized




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

            # authority to Edit patients data

            
        }

    def add_doctor(self):
        if self.authority['add_doctor']==True:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
    

if __name__=='__main__':
    user=User()
    user.add_doctor()

