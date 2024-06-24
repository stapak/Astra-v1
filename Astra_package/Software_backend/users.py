from projectExceptions import NotAuthorized,UserDetailsNotFound,TreatmentComplete
from patients import *

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

            "add_pharmacy":False,
            "remove_pharmacy":False,

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
    
    
    def add_diagnostic(self):
        if self.authority['add_diagnostic']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
    
    def add_session_report(self):
        if self.authority['add_session_report']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
    
    def conclude_treatment(self):
        if self.authority['conclude_treatment']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        
    
    def register_patient(self):
        if self.authority['register_patient']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        
    
    def view_medical_history(self):
        if self.authority['view_medical_history']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
        
    def edit_patient_details(self):
        if self.authority['edit_patient_details']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
    
    def patient_list(self):
        if self.authority['register_patient']:
            raise NotImplemented('The method is not implimented by the child class')
        else:
            raise NotAuthorized('User is not authorized to use this method.')
    
#--------------------User child class-------------------------------------------------------------------------------------
        

class Head(User):
    def __init__(self,cursor_object,name):
        super().__init__()
        self.cursor_object=cursor_object
        self.authority['add_tech_support']=True
        self.authority['remove_tech_support']=True
        
        self.authority['add_doctor']=True
        self.authority['remove_doctor']=True
        
        self.authority['add_receptionist']=True
        self.authority['remove_receptionist']=True

        self.authority['add_diagnostic']=True
        self.authority['remove_diagnostic']=True

        self.authority['add_pharmacy']=True
        self.authority['remove_pharmacy']=True
        
        #----------- User Object address initialization---------------------------------------------------------------------
        query=f"""
        SELECT * FROM user_table
        WHERE user_name = {name};
        """
        self.cursor_object.execute(query)
        user_details={}
        raw_data=self.cursor_object
        
    
        


        
class Doctor(User):
    def __init__(self,cursor_object,patient_object):
        super().__init__()
        
        self.patient_object=patient_object
        self.authority['add_session_report']=True
        self.cursor_object=cursor_object

    
    def add_session_report(self,name,s_result,medications,treatment):
        data={
            "session_diagnostic":s_result,
            "medication":medications,
            "treatment":treatment
        }



        self.patient_object.session_result(name,data)


    def conclude_treatment(self):
        pass

    
    
    

    







