"""
This File contains Frame class related to doctor interface.
"""

# Tkinter Liabrary imports

import tkinter as tk
from tkinter import  END, SCROLL, Button, Frame, IntVar, Label, LabelFrame
from tkinter import Listbox, Menu, Scrollbar, StringVar ,Text, Toplevel,messagebox
from tkinter.ttk import Entry








# Important Variable
BACKGROUND_COLOR="#DCDCDC"
BASE_FONT=("Arial",15)
BASE_WIDTH=1535
BASE_HEIGHT=775

# User Detials.

HOSPITAL_NAME='tESTING 1'
USER_NAME='TEsting 2'
USER_ID=None

class DoctorDashboard(Frame):
    """
    Frame class representing the DashBoard of the doctor.
    
    """
    def __init__(self,window_object,doctor_functions:dict):
        super().__init__(master=window_object,width=BASE_WIDTH,height=BASE_HEIGHT)
        self.place(x=0,y=0)
        
        # Function of Frame
        def fetch_appointments():
            """
            Function used to fetch the patient appointments from the database.
            """
            appointments=doctor_functions['fetch appointments'](USER_ID)
            for appointment in appointments:
                appointment_listbox.insert(tk.END,appointment)
            
        
        def appointment_page(trash):
            """
            Used to redirect to patient appointment frame by creating the window object in this function itself.
            """
            selection_index=appointment_listbox.curselection()
            selected_patient=appointment_listbox.get(selection_index)
        #----------------------------------------------------------------- Hospital Name Frame -------------------------------------  
        
        hospital_name_frame=Frame(master=self,height=75,width=BASE_WIDTH,background='light blue')
        hospital_name_frame.place(x=0,y=0)
        
        hospital_name_label=Label(master=hospital_name_frame,text=HOSPITAL_NAME,foreground='red',font=("Arial",40,'bold'),background='light blue',justify='center')
        hospital_name_label.place(x=0,y=5,width=BASE_WIDTH)
        
        #----------------------------------------------------------------- Widget Frames --------------------------------------------

        # Left Frame
        left_widget_frame=Frame(master=self,width=1135,height=700,background='light green')
        left_widget_frame.place(x=0,y=75)
            
        appointment_label=Label(master=left_widget_frame,text="Today's Appointments",font=('Arial',25),justify="center",background='light green')
        appointment_label.place(x=0,y=5,width=1135)
            
        appointment_listbox=Listbox(master=left_widget_frame,width=183,height=38)
        appointment_listbox.place(x=10,y=75)
        
        appointment_scrollbar=Scrollbar(master=left_widget_frame,orient='vertical',command=appointment_listbox.yview)
        appointment_scrollbar.place(x=1105,y=75,height=610,width=10)
        
        appointment_listbox.config(yscrollcommand=appointment_scrollbar.set)
        appointment_listbox.bind('<<ListboxSelect>>', appointment_page)
        
        refresh_button=Button(master=left_widget_frame,text="Refresh",font=("Arial",10),command=fetch_appointments)
        refresh_button.place(x=1020,y=45,width=100)
    
            
        # Right Frame
        right_widget_frame=Frame(master=self,width=400,height=700,background='white')
        right_widget_frame.place(x=1135,y=75)
        
        user_name_label=Label(master=right_widget_frame,text=f'Welcom ,{USER_NAME}',font=('Arial',25),background='white')
        user_name_label.place(x=10,y=10)
        
        
    



if __name__=='__main__':
    from software_windows import Window
    root=Window()
    root=root.normal_window()
    sample={}
    testing1=DoctorDashboard(root,sample)
    root.mainloop()