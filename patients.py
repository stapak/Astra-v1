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
            check_Up DATE
            );

         """
        self.cursor_object.execute(query)

        

    def session_result(self,patient_name,date,diagnostic,medications,treatment,check_Up):
        query="""
        INSERT INTO {patient_name}
        (session_date,session_diagnostic,medivations,treatment)
        VALUES
        (table_name,date,diagnostic,medications,treatment,check_up);
        """
        self.cursor_object.execute(query)

    def register(self,**patient_info):
        query="""
        INSERT INTO patient_list
        (patient_id,patient_name,phone_no,blood_group,initial_diagnostic,doctor_name)
        """
        self.cursor_object.execute()