import mysql.connector

class patient:
    def __init__(self,cursor_object):
        self.cursor_object=cursor_object
    
    def _patient_personal(self,patient_name):
        query=f"""
            CREATE TABLE {patient_name}(
            session_date DATE NOT NULL,
            session_diagnostic VARCHAR(10000) NOT NULL,
            medications VARCHAR(1000),
            treatment VARCHAR(1000),
            check_Up DATE,
            test_report VARCHAR(1000),
            test_keypoints VARCHAR(100)
            );

         """
        self.cursor_object.execute(query)

        

    def session_result(self,**data):
        result=result
        query=f"""
        INSERT INTO {data['name']}
        (session_date,session_diagnostic,medications,treatment,check_up,diagnos_report,diagnos_keypoints)
        VALUES
        ({result['date']},{result['diagnostic']},{result['medication']},
        );
        """
        self.cursor_object.execute(query)

    def register(self,**patient_info):
        # This function adds patients details to the patient list and creates a personal table to track patients medical history 
        query="""
        INSERT INTO patient_list
        (patient_id,patient_name,patient_DOB,phone_no,blood_group,initial_diagnostic,doctor_name)
        VALUES
        ({patient_info['name']},{patient_info['DOB']},{patient_info['phone no']},{patient_info['blood group']},{patient_info['intial diagnostic']},{patient_info['doctor name']}
        );
        """
        self.cursor_object.execute(query)
        self._patient_personal(patient_info['name'])

    def medical_history(self,patient_name):
        # This function uses patients personal table to show their medical history.
        query=f"""
        SELECT * FROM {patient_name}
        """
        self.cursor_object.execute(query)
        patient_history=self.cursor_object
        return patient_history
    
    def add_diagnos_result(self,**data):
        query=f"""
        INSERT INTO {data['patient name']}
        """
    
    





if __name__=='__main__':
    Database=mysql.connector.connect(host="localhost",
                                     user="root",
                                     passwd="admin",
                                     auth_plugin='mysql_native_password',
                                     database="test")
    cursorobj=Database.cursor()
    patient=Patient(cursorobj)
    patient_info={"name":"","DOB":"","phone no":"",'blood_group':"","intial diagnostic":"",
                  'doctor name':''}
    for i in patient_info:
        print(f"Enter {i} of patient")
        patient_info[i]=input()
    
    patient.register(**patient_info)
