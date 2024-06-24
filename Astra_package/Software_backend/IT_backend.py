"""
This file contains backend of IT head.
"""


# Astra modules


from . import ID_generator



class IT_head_functions:
    """
    Class contains all the functions used by IT head.
    """
    
        
    @staticmethod
    def execute_query(cursor_object,query)->str | bool:
        """
        Function used to execute queries, and sends error as stirng if any,raised during execution of query.
        """
        try:
            cursor_object.execute(query)
        except Exception as e:
            return str(e)
        else:
            return True
    

    @staticmethod
    def add_departments(**data):
        """
        Function used to add departments available in hospital,this function uses id_generator function to generate id and uses that id in 
        query.
        """
        cursor_object=data['cursor object']
        dept_id=ID_generator()
        query=f"""
        INSERT INTO departments
        (dept_id,dept_name,total_doctors)
        VALUES
        (
        '{dept_id}','{data['department name']}',{data['total doctors']}
        );
        """
        return IT_head_functions.execute_query(cursor_object,query)
       
    @staticmethod
    def add_hospital_staff(**data):
        """
        Function used to add hospital staff such as receptionist.
        """
        cursor_object=data['cursor object']
        dept_id=ID_generator()
        query=f"""
        INSERT INTO departments
        (dept_id,dept_name,total_doctors)
        VALUES
        (
        '{dept_id}','{data['department name']}',{data['total doctors']}
        );
        """
        return IT_head_functions.execute_query(cursor_object,query)
    
    @staticmethod
    def add_doctors_list(**data):
        """
        Function used to enter the doctors to the doctors list.
        """
        cursor_object=data['cursor object']
        dept_id=ID_generator()
        query=f"""
        INSERT INTO departments
        (dept_id,dept_name,total_doctors)
        VALUES
        (
        '{dept_id}','{data['department name']}',{data['total doctors']}
        );
        """
        return IT_head_functions.execute_query(cursor_object,query)
        
    
    @staticmethod
    def add_pharmacy(**data):
        """
        Funcitons used to enter pharmacist to the list
        """
        cursor_object=data['cursor object']
        dept_id=ID_generator()
        query=f"""
        INSERT INTO departments
        (dept_id,dept_name,total_doctors)
        VALUES
        (
        '{dept_id}','{data['department name']}',{data['total doctors']}
        );
        """
        return IT_head_functions.execute_query(cursor_object,query)
        
    
    @staticmethod
    def change_user_passwrod(**data):
        """
        Function used by IT to help other change their forgotten password.
        """
        cursor_object=data['cursor object']
        dept_id=ID_generator()
        query=f"""
        INSERT INTO departments
        (dept_id,dept_name,total_doctors)
        VALUES
        (
        '{dept_id}','{data['department name']}',{data['total doctors']}
        );
        """
        return IT_head_functions.execute_query(cursor_object,query)

    

if __name__=='__main__':
    import mysql.connector
    database=mysql.connector.connect(host='localhost',user='test',passwd='test',database='testing4')
    cursor_object=database.cursor()
    data={'cursor object':cursor_object,'department name':'ENT','total doctors':18}
    print(IT_head_functions.add_departments(**data))
    