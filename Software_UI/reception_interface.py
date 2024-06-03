"""
This file contains frames related to all the work of the receptionist.

"""


from math import comb
from tkinter import  Frame, LabelFrame, Place
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from tkinter import PhotoImage
import tkinter as tk
from tkinter import Listbox
from tkinter import IntVar
from tkinter import StringVar
from tkinter import messagebox


from tkinter.ttk import Checkbutton 
from tkinter.ttk import Entry 
from tkinter import Scrollbar
from tkinter.ttk import Button as Button2
from tkinter.ttk import Combobox





# Other liabraries
from PIL import Image,ImageTk
import json
import os
import time

# My liabraries
from software_windows import Window

#---------------------------------------------- Varibales of frames-------------------------------------------------
blue_background="#7CB9E8"
grey_background="light grey"
base_height=780
base_width=1535
HOSPITAL_NAME=None


#----------------------------------------------- Frames of windows---------------------------------------------------
class BaseReceptionFrame(Frame):
    def __init__(self,window_object):
        self.window_oject=window_object
        super().__init__(window_object,bg=grey_background,width=base_width,height=base_height)
        self.place(x=0,y=0)
        name_frame=Frame(self,bg=blue_background,width=base_width,height=50)
        name_frame.place(x=0,y=0)
        hospital_label=Label(master=name_frame,text=HOSPITAL_NAME,bg=blue_background,font=("Arial",15))
        hospital_label.place(x=5,y=10)
        




class Dashboard(BaseReceptionFrame):
    pass





class RegisterPatient(BaseReceptionFrame):
    """
    This sub class will be used to create
    """
    def __init__(self, window_object,register_patient=None):
        super().__init__(window_object)
        
        #-------------------------------------------------------Patient personal Information-------------------------------------------------
        personal_info_frame=LabelFrame(master=self,height=199,width=1535,text="Patient Personal Information",borderwidth=1,relief="groove")
        personal_info_frame.place(x=0,y=51)
        
        #---------------------variables
        basic_font=('Lucida Console',15)        

        first_name=tk.StringVar()
        last_name=tk.StringVar()
        
        DOB_variable_date=StringVar()
        DOB_variable_month=StringVar()
        DOB_variable_year=StringVar()
                

        blood_group=tk.StringVar()
        gender_variable=StringVar()
        IDproof_variable=StringVar()
        IDproof_number=IntVar()
        
        #------------------First line-----------------------------------------------
        first_name_label=Label(master=personal_info_frame,text="First Name:",font=basic_font)
        first_name_label.place(x=5,y=5)
        first_name_entry=Entry(master=personal_info_frame,textvariable=first_name,font=basic_font,width=16)
        first_name_entry.place(y=2,x=150,height=35)
        

        last_name_label=Label(master=personal_info_frame,text="Last Name/initials:",font=basic_font)
        last_name_label.place(x=370,y=5)
        last_name_entry=Entry(master=personal_info_frame,textvariable=last_name,font=basic_font,width=16)
        last_name_entry.place(y=2,x=600,height=35)
        

        DOB_label=Label(master=personal_info_frame,text="Date of Birth:",font=basic_font)
        DOB_label.place(x=825,y=5)
        DOB_combobox_date=Combobox(master=personal_info_frame,width=5,textvariable=DOB_variable_date,font=basic_font)
        DOB_combobox_date['values']=('1','2','3','4','5','6','7','8','9','10',
                                     '11','12','13','14','15','16','17','18','19','20',
                                     '21','22','23','24','25','26','27','28','29','30','31'
                                     )
        DOB_combobox_date.place(x=1000,y=5)
        
        DOB_combobox_month=Combobox(master=personal_info_frame,width=5,textvariable=DOB_variable_month,font=basic_font)
        DOB_combobox_month['values']=(
                                    'Jan','Feb','Mar','Apr','May','June',
                                     'July','Aug','Sept','Octo','Nove','Dece'
                                     )
        DOB_combobox_month.place(x=1100,y=5)
        
        DOB_entry_year=Entry(master=personal_info_frame,font=basic_font,textvariable=DOB_variable_year,width=4)
        DOB_entry_year.place(x=1200,y=5)
        
        
        Blood_grouop_label=Label(master=personal_info_frame,text="Blood group:",font=basic_font)
        Blood_grouop_label.place(x=1275,y=5)
        
        Blood_combobox=Combobox(master=personal_info_frame,width=4,textvariable=blood_group,font=basic_font)
        Blood_combobox['values']=('A+','A-','B+','B-','AB+','AB-','O+','O-')
        Blood_combobox.place(x=1425,y=5)
        
        
        #----------------------------------Second Line-----------------
        gender_label=Label(master=personal_info_frame,text="Gender:",font=basic_font)
        gender_label.place(x=5,y=55)
        
        gender_combox=Combobox(master=personal_info_frame,width=14,font=basic_font,textvariable=gender_variable)
        gender_combox['values']=('Male','Female','Other')
        gender_combox.place(x=150,y=55)
        
        
        IDproof_label=Label(master=personal_info_frame,text="ID proof:",font=basic_font)
        IDproof_label.place(y=55,x=370)
        
        IDproof_combox=Combobox(master=personal_info_frame,font=basic_font,textvariable=IDproof_variable,width=15)
        IDproof_combox['values']=['Adhar card','Driving Licence','Passprot','Pancard']
        IDproof_combox.place(x=600,y=55)
        
        IDnumber_label=Label(master=personal_info_frame,text="ID proof no.:",font=basic_font)
        IDnumber_label.place(y=55,x=825)

        IDnumber_entry=Entry(master=personal_info_frame,textvariable=IDproof_number,font=basic_font,width=20)
        IDnumber_entry.place(y=50,x=1000,height=35)
        

        
        #-------------------------------------------------------Contact Information-------------------------------------------------
        contact_info_frame=LabelFrame(master=self,height=250,width=1535,text="Contact Information",borderwidth=2,relief="groove")
        contact_info_frame.place(y=201,x=0)
        
        #--------------------------- Variables---------------------------
        contact_no1=IntVar()
        contact_no2=IntVar()
        current_address=StringVar()
        parmanent_address=StringVar()
        email_address=StringVar()
        
        
        contact_no1_label=Label(master=contact_info_frame,text="Mobile no.:",font=basic_font)
        contact_no1_label.place(x=5,y=5)
        contact_no1_entry=Entry(master=contact_info_frame,textvariable=contact_no1,font=basic_font,width=12)
        contact_no1_entry.place(y=5,x=150,height=35)
        
        contact_no2_label=Label(master=contact_info_frame,text="Phone no.:",font=basic_font)
        contact_no2_label.place(x=5,y=55)
        contact_no2_entry=Entry(master=contact_info_frame,textvariable=contact_no2,font=basic_font,width=12)
        contact_no2_entry.place(y=55,x=150,height=35)
        
        

         
        
        
        
        
        
    

class SessionBooing(BaseReceptionFrame):
    pass
        







if __name__=='__main__':
    window=Window()
    root=window.normal_window()
    
    #base_class_object=BaseReceptionFrame(root)
     
    
    add_object=RegisterPatient(root)

    root.mainloop()
    