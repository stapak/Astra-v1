from projectExceptions import NotAuthorized

class User:
    """
    This is the base user class that contains all the methods and authority atrribute of every user class.
    
    """
    def __init__(self):
        self.authority={
            # authority related to adding and removing users
            "add_tech_support":False,
            "remove_tech_support":False,

            "add_doctor":False,
            "remove_doctor":False,

            "add_receptionist":False,
            "remove_receptionist":False,

            "add_diagnostic_center":False,
            "remove_diagnostic_center":False,

            "add_pharmacists":False,
            "remove_pharmacists":False,

            # authority to Edit patients data
            "add_diagnostic":False,
            "add_session_report":False,
            "conclude_treatment":False,
            "register_patient":False,
            "view_medical_history":False,
            "edit_patient_details":False,
            "patient_list":False

            
        }


    #-----------------------User related authorities----------------------------------------------------------------------- 
    def add_tech_support(self):
        if self.authority['add_tech_support']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')

    def remove_tech_support(self):
        if self.authority['remove_tech_support']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        


    def add_doctor(self):
        if self.authority['add_doctor']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        
    def remove_doctor(self):
        if self.authority['add_doctor']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        

    def add_receptionist(self):
        if self.authority['add_receptionist']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
    
    def remove_receptionist(self):
        if self.authority['remove_receptionist']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        

   
    def add_diagnostic_center(self):
        if self.authority['add_diagnostic_center']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        
    def remove_diagnostic_center(self):
        if self.authority['remove_diagnostic_center']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        

    
    def add_pharmacists(self):
        if self.authority['add_pharmacists']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        
    def remove_pharmacists(self):
        if self.authority['remove_pharmacists']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        

   #----------------------- Patient related authorities ----------------------------------------------------------------------- 
    

if __name__=='__main__':
    user=User()
    user.add_doctor()

