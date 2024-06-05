"""
This file contains frames related to all the work of the receptionist.

"""


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
        
        #-------------------------------------------------------Patient personal Information Frame -------------------------------------------
        personal_info_frame=LabelFrame(master=self,height=125,width=1535,text="Patient Personal Information",borderwidth=2,relief="groove")
        personal_info_frame.place(x=0,y=51)
        
        #---------------------variables
        basic_font=('Lucida Console',15) 
        entry_font=('Lucida Console',12)

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
        

        last_name_label=Label(master=personal_info_frame,text="Last Name:",font=basic_font)
        last_name_label.place(x=370,y=5)
        last_name_entry=Entry(master=personal_info_frame,textvariable=last_name,font=basic_font,width=16)
        last_name_entry.place(y=2,x=500,height=35)
        

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
        IDproof_combox.place(x=500,y=55)
        
        IDnumber_label=Label(master=personal_info_frame,text="ID proof no.:",font=basic_font)
        IDnumber_label.place(y=55,x=825)
        IDnumber_entry=Entry(master=personal_info_frame,textvariable=IDproof_number,font=entry_font,width=20)
        IDnumber_entry.place(y=50,x=1000,height=35)
        

        
        #-------------------------------------------------------Contact Information Frame -------------------------------------------------
        contact_info_frame=LabelFrame(master=self,height=90,width=1535,text="Contact Information",borderwidth=2,relief="groove")
        contact_info_frame.place(y=171,x=0)
        
        #--------------------------- Variables---------------------------
        contact_no1=IntVar()
        contact_no2=IntVar()
        email_address=StringVar()
        
        #------------------------ Widgets--------------------------------
        
        contact_no1_label=Label(master=contact_info_frame,text="Contact no.:",font=basic_font)
        contact_no1_label.place(x=5,y=5)
        contact_no1_entry=Entry(master=contact_info_frame,textvariable=contact_no1,font=entry_font,width=12)
        contact_no1_entry.place(y=2,x=150,height=35)
        
        contact_no2_label=Label(master=contact_info_frame,text="Contact no2.:",font=basic_font)
        contact_no2_label.place(x=370,y=5)
        contact_no2_entry=Entry(master=contact_info_frame,textvariable=contact_no2,font=entry_font,width=12)
        contact_no2_entry.place(y=2,x=540,height=35)
        
        email_label=Label(master=contact_info_frame,text="Email Address:",font=basic_font)
        email_label.place(x=825,y=5)
        email_entry=Entry(master=contact_info_frame,textvariable=email_address,width=49,font=entry_font)
        email_entry.place(y=2,x=1000,height=35)
        

        
        #-------------------- Current Address Frame --------------------------------------------------------------------------------------
        current_address_frame=LabelFrame(master=self,height=140,width=1535,text="Current Address",borderwidth=2,relief="groove")
        current_address_frame.place(y=251,x=0)
        #-------------------- variables ------------------------
        house_no=StringVar()
        block_no=StringVar()
        bulding_name=StringVar()
        land_mark=StringVar()
        town_variable=StringVar()
        district_variable=StringVar()
        state_variable=StringVar()
        contry_variable=StringVar()
        contry_variable.set('India')
        


        #------------------ widgets------------------------------
        house_no_label=Label(master=current_address_frame,text="House no:",font=basic_font)
        house_no_label.place(x=5,y=5)
        house_no_entry=Entry(master=current_address_frame,textvariable=house_no,width=10,font=entry_font)
        house_no_entry.place(y=2,x=120,height=35)
        
        block_no_label=Label(master=current_address_frame,text="block no:",font=basic_font)
        block_no_label.place(x=270,y=5)
        block_no_entry=Entry(master=current_address_frame,textvariable=block_no,width=10,font=entry_font)
        block_no_entry.place(y=2,x=390,height=35)
        
        bulding_name_label=Label(master=current_address_frame,text="bulding Name:",font=basic_font)
        bulding_name_label.place(x=545,y=5)
        bulding_name_entry=Entry(master=current_address_frame,textvariable=bulding_name,width=15,font=entry_font)
        bulding_name_entry.place(y=2,x=710,height=35)
        
        land_mark_label=Label(master=current_address_frame,text="Land Mark:",font=basic_font)
        land_mark_label.place(x=900,y=5)
        land_mark_entry=Entry(master=current_address_frame,textvariable=land_mark,width=46,font=entry_font)
        land_mark_entry.place(y=2,x=1030,height=35)
        
        #------------------------- Second line --------------------
        town_name_label=Label(master=current_address_frame,text="Town:",font=basic_font)
        town_name_label.place(x=5,y=55)
        town_name_entry=Entry(master=current_address_frame,textvariable=town_variable,width=15,font=entry_font)
        town_name_entry.place(y=52,x=70,height=35)
        
        district_name_label=Label(master=current_address_frame,text="District:",font=basic_font)
        district_name_label.place(x=270,y=55)
        district_name_entry=Entry(master=current_address_frame,textvariable=district_variable,width=10,font=entry_font)
        district_name_entry.place(y=52,x=390,height=35)
        
        state_name_label=Label(master=current_address_frame,text="State:",font=basic_font)
        state_name_label.place(x=630,y=55)
        state_name_entry=Entry(master=current_address_frame,textvariable=state_variable,width=15,font=entry_font)
        state_name_entry.place(y=52,x=710,height=35)
        
        contry_name_label=Label(master=current_address_frame,text="Country:",font=basic_font)
        contry_name_label.place(x=923,y=55)
        contry_name_entry=Entry(master=current_address_frame,textvariable=contry_variable,width=15,font=entry_font)
        contry_name_entry.place(y=52,x=1030,height=35)
        


        #------------------ Permanent Address Frame -----------------------------------------------------------------------------
        parmanent_address_frame=LabelFrame(master=self,height=140,width=1535,text="Permanent Address",borderwidth=2,relief="groove")
        parmanent_address_frame.place(y=370,x=0)
        
        #----------------- Variables ---------------------
        house_no2=StringVar()
        block_no2=StringVar()
        bulding_name2=StringVar()
        land_mark2=StringVar()
        town_variable2=StringVar()
        district_variable2=StringVar()
        state_variable2=StringVar()
        
        contry_variable2=StringVar()
        contry_variable2.set('India')
        

        #------------------ widgets------------------------------
        house_no_label2=Label(master=parmanent_address_frame,text="House no:",font=basic_font)
        house_no_label2.place(x=5,y=5)
        house_no_entry2=Entry(master=parmanent_address_frame,textvariable=house_no2,width=10,font=entry_font)
        house_no_entry2.place(y=2,x=120,height=35)
        
        block_no_label2=Label(master=parmanent_address_frame,text="block no:",font=basic_font)
        block_no_label2.place(x=270,y=5)
        block_no_entry2=Entry(master=parmanent_address_frame,textvariable=block_no2,width=10,font=entry_font)
        block_no_entry2.place(y=2,x=390,height=35)
        
        bulding_name_label2=Label(master=parmanent_address_frame,text="bulding Name:",font=basic_font)
        bulding_name_label2.place(x=545,y=5)
        bulding_name_entry2=Entry(master=parmanent_address_frame,textvariable=bulding_name2,width=15,font=entry_font)
        bulding_name_entry2.place(y=2,x=710,height=35)
        
        land_mark_label2=Label(master=parmanent_address_frame,text="Land Mark:",font=basic_font)
        land_mark_label2.place(x=900,y=5)
        land_mark_entry2=Entry(master=parmanent_address_frame,textvariable=land_mark2,width=46,font=entry_font)
        land_mark_entry2.place(y=2,x=1030,height=35)
        
        #------------------------- Second line --------------------
        town_name_label2=Label(master=parmanent_address_frame,text="Town:",font=basic_font)
        town_name_label2.place(x=5,y=55)
        town_name_entry2=Entry(master=parmanent_address_frame,textvariable=town_variable2,width=15,font=entry_font)
        town_name_entry2.place(y=52,x=70,height=35)
        
        district_name_label2=Label(master=parmanent_address_frame,text="District:",font=basic_font)
        district_name_label2.place(x=270,y=55)
        district_name_entry2=Entry(master=parmanent_address_frame,textvariable=district_variable2,width=10,font=entry_font)
        district_name_entry2.place(y=52,x=390,height=35)
        
        state_name_label2=Label(master=parmanent_address_frame,text="State:",font=basic_font)
        state_name_label2.place(x=630,y=55)
        state_name_entry2=Entry(master=parmanent_address_frame,textvariable=state_variable2,width=15,font=entry_font)
        state_name_entry2.place(y=52,x=710,height=35)
        
        contry_name_label2=Label(master=parmanent_address_frame,text="Country:",font=basic_font)
        contry_name_label2.place(x=923,y=55)
        contry_name_entry2=Entry(master=parmanent_address_frame,textvariable=contry_variable2,width=15,font=entry_font)
        contry_name_entry2.place(y=52,x=1030,height=35)
        
        #---------------------- Relative Information Frame -----------------------------------------------------
        relative_info_frame=LabelFrame(master=self,width=1535,height=180,text="Relative's Contact",borderwidth=2,relief='groove')
        relative_info_frame.place(y=500,x=0)
        
        #--------------- Variables ---------------------------------
        
        relative_first_name=StringVar()
        relative_last_name=StringVar()
        relative_contact_no=IntVar()
        relative_contact_no2=IntVar()
        relative_email=StringVar()
        relative_blood_group=StringVar()
        
        relative_house_no=StringVar()
        relative_block_no=StringVar()
        relative_bulding_name=StringVar()
        relative_land_mark=StringVar()
        relative_town_variable=StringVar()
        relative_district_variable=StringVar()
        relative_state_variable=StringVar()
        relative_contry_variable=StringVar()
        relative_contry_variable.set('India')
        
        #----------------- widgets --------------------------------
        first_name_label=Label(master=relative_info_frame,text="First Name:",font=basic_font)
        first_name_label.place(x=5,y=5)
        first_name_entry=Entry(master=relative_info_frame,textvariable=relative_first_name,font=basic_font,width=16)
        first_name_entry.place(y=2,x=150,height=35)

        last_name_label=Label(master=relative_info_frame,text="Last Name:",font=basic_font)
        last_name_label.place(x=370,y=5)
        last_name_entry=Entry(master=relative_info_frame,textvariable=relative_last_name,font=basic_font,width=16)
        last_name_entry.place(y=2,x=500,height=35)
        
        contact_no1_label=Label(master=relative_info_frame,text="Contact no:",font=basic_font)
        contact_no1_label.place(x=725,y=5)
        contact_no1_entry=Entry(master=relative_info_frame,textvariable=relative_contact_no,font=entry_font,width=12)
        contact_no1_entry.place(y=2,x=860,height=35)
      
        contact_no2_label=Label(master=relative_info_frame,text="Contact no2:",font=basic_font)
        contact_no2_label.place(x=1000,y=5)
        contact_no2_entry=Entry(master=relative_info_frame,textvariable=relative_contact_no2,font=entry_font,width=12)
        contact_no2_entry.place(y=2,x=1150,height=35)
        

        Blood_grouop_label=Label(master=relative_info_frame,text="Blood group:",font=basic_font)
        Blood_grouop_label.place(x=1295,y=5)
        Blood_combobox=Combobox(master=relative_info_frame,width=4,textvariable=relative_blood_group,font=basic_font)
        Blood_combobox['values']=('A+','A-','B+','B-','AB+','AB-','O+','O-')
        Blood_combobox.place(x=1445,y=5)
        
        #---------- Second line ---------------------------------
        house_no_label2=Label(master=relative_info_frame,text="House no:",font=basic_font)
        house_no_label2.place(x=5,y=55)
        house_no_entry2=Entry(master=relative_info_frame,textvariable=relative_house_no,width=10,font=entry_font)
        house_no_entry2.place(y=52,x=120,height=35)
        
        block_no_label2=Label(master=relative_info_frame,text="block no:",font=basic_font)
        block_no_label2.place(x=270,y=55)
        block_no_entry2=Entry(master=relative_info_frame,textvariable=relative_block_no,width=10,font=entry_font)
        block_no_entry2.place(y=52,x=390,height=35)
        
        bulding_name_label2=Label(master=relative_info_frame,text="bulding Name:",font=basic_font)
        bulding_name_label2.place(x=545,y=55)
        bulding_name_entry2=Entry(master=relative_info_frame,textvariable=relative_bulding_name,width=15,font=entry_font)
        bulding_name_entry2.place(y=52,x=710,height=35)
        
        land_mark_label2=Label(master=relative_info_frame,text="Land Mark:",font=basic_font)
        land_mark_label2.place(x=900,y=55)
        land_mark_entry2=Entry(master=relative_info_frame,textvariable=relative_land_mark,width=46,font=entry_font)
        land_mark_entry2.place(y=52,x=1030,height=35)
        
        #------------------------- third line --------------------
        town_name_label2=Label(master=relative_info_frame,text="Town:",font=basic_font)
        town_name_label2.place(x=5,y=105)
        town_name_entry2=Entry(master=relative_info_frame,textvariable=town_variable2,width=15,font=entry_font)
        town_name_entry2.place(y=102,x=70,height=35)
        
        district_name_label2=Label(master=relative_info_frame,text="District:",font=basic_font)
        district_name_label2.place(x=270,y=105)
        district_name_entry2=Entry(master=relative_info_frame,textvariable=relative_district_variable,width=10,font=entry_font)
        district_name_entry2.place(y=102,x=390,height=35)
        
        state_name_label2=Label(master=relative_info_frame,text="State:",font=basic_font)
        state_name_label2.place(x=630,y=105)
        state_name_entry2=Entry(master=relative_info_frame,textvariable=relative_state_variable,width=15,font=entry_font)
        state_name_entry2.place(y=102,x=710,height=35)
        
        contry_name_label2=Label(master=relative_info_frame,text="Country:",font=basic_font)
        contry_name_label2.place(x=923,y=105)
        contry_name_entry2=Entry(master=relative_info_frame,textvariable=relative_contry_variable,width=15,font=entry_font)
        contry_name_entry2.place(y=102,x=1030,height=35)
        
        #------------------------- Medical histroy -----------------------------------------------------------------------------
        medical_history_frame=LabelFrame(master=self,width=1535,height=110,text="Medical History",borderwidth=2,relief='groove')
        medical_history_frame.place(y=670,x=0)
        
        #-------------- Variables -----------------------------
        patient_department=StringVar()
        attending_doctor=StringVar()
        
        #------------- widgets ----------------------------
        department_label=Label(master=medical_history_frame,text="Department:",font=basic_font)
        department_label.place(x=5,y=5)
        department_combobox=Combobox(master=medical_history_frame,width=15,font=basic_font,textvariable=patient_department)
        department_combobox.place(y=5,x=150)
        
        attending_doctor_label=Label(master=medical_history_frame,text="Doctor:",font=basic_font)
        attending_doctor_label.place(y=5,x=375)
        attending_doctor_combox=Combobox(master=medical_history_frame,width=15,font=basic_font,textvariable=attending_doctor)
        attending_doctor_combox.place(y=5,x=470)
        
         
        
        
        
        
        
    

class SessionBooking(BaseReceptionFrame):
    pass
        







if __name__=='__main__':
    window=Window()
    root=window.normal_window()
    
    #base_class_object=BaseReceptionFrame(root)
     
    
    add_object=RegisterPatient(root)

    root.mainloop()
    