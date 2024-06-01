"""
This file contains all the code related to the setup window of the software
"""

# Tkinter  liabraries
from cgi import test
from msilib.schema import InstallUISequence
from re import T
from tkinter import TRUE, Entry, Frame, font
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from tkinter import Checkbutton as Checkbutton1
from tkinter import Scrollbar
from tkinter import PhotoImage
import tkinter as tk
from tkinter import Listbox
from tkinter import IntVar
from tkinter import messagebox

from tkinter.ttk import Checkbutton as Checkbutton2
from tkinter.ttk import Entry as Entry2
from tkinter.ttk import Scrollbar as Scrollbar2
from tkinter.ttk import Button as Button2



# Other liabraries
from PIL import Image,ImageTk
import json
import os
import time

# My liabraries
from software_windows import Window

#---------------------------------------Variable/attributes of file ---------------------------------------



background_color="#DCDCDC"


with open( os.path.join(os.path.dirname(os.path.realpath(__file__)),'setup_page_info.json'),encoding='utf-8' ) as fobj:
    setup_info=json.load(fobj)["welcome_greeting"]




#--------------------------------------class of file-------------------------------------------------------


class Welcome_page(Frame):
    """
    Class that contains the first welcome page of the setup window.
    """
    def __init__(self,window_object):
        self.window_oject=window_object
        super().__init__(window_object,bg="light grey",width=550,height=400)
        self.pack(fill="x")

        #------------------------------ Image Frame----------------------------------------

        image_frame=Frame(self,bg="#7CB9E8",width=180,height=350,relief=tk.RIDGE)
        image_frame.place(x=0,y=0)
        
        image1=Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'software_icon.png'))
        resize_image=image1.resize((150,100))
        image_object=ImageTk.PhotoImage(resize_image)
        window_icon_label=Label(image=image_object)
        window_icon_label.image=image_object
        window_icon_label.place(x=10,y=150)


        #-------------------------------Information frame----------------------------------
        details_frame=Frame(self,bg=background_color,height=350,width=370)
        details_frame.place(x=181,y=0)

        next_button=Button(self,text="Next",relief="groove",width=10)
        next_button.place(x=460,y=360)



class Terms_condition_page(Frame):
    """
    This class is used to code second page of startup which is terms and condition page.
    This frame is devided into 3 parts one to hold the photo and name of the software.
    One to hold the terms and condition and detailed dialog box
    One to hold the button of the page.

    """
    def __init__(self,window_object):
        self.window_oject=window_object
        super().__init__(window_object,bg="light grey",width=550,height=400)
        self.pack(fill="x")
        
        #---------------1st part:Company logo and name --------------------------------------------------------
        name_frame=Frame(self,width=550,height=70,bg="#7CB9E8")
        name_frame.place(x=0,y=0)
        company_name=Label(name_frame,text="Astra Softwares",font=("Arial",20,"bold"),bg="#7CB9E8")
        company_name.place(x=20,y=5)
        page_short_discription=Label(name_frame,text="License Agreement",bg="#7CB9E8",font=(10))
        page_short_discription.place(x=20,y=40)
        
        image=Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'software_icon.png'))
        resize_image=image.resize((100,60))
        image_object=ImageTk.PhotoImage(resize_image)
        photo_icon=Label(name_frame,image=image_object)
        photo_icon.image=image_object
        photo_icon.place(x=350,y=4)


        #-----------------------------2nd part:terms and condition box -------------------------
        TC_detailed_frame=Frame(self,width=550,height=290,bg=background_color)
        TC_detailed_frame.place(y=71,x=0)
        head_label=Label(TC_detailed_frame,text="Terms and Conditon of Use",font=("Arial",10,"bold"),bg=background_color)
        head_label.place(y=4,x=25)   
    
        scroll_box=Frame(TC_detailed_frame,bg="light blue",width=500,height=200,relief="ridge")   
        scroll_box.place(y=24,x=25) 

        scroll_bar_object=Scrollbar2(scroll_box)
        scroll_bar_object.place(x=483,y=0,height=200)
        
        terms_and_condition_listbox=Listbox(scroll_box,yscrollcommand=scroll_bar_object.set)#main content box
        terms_and_condition_listbox.place(y=0,x=0,height=200,width=483)

        scroll_bar_object.config(command=terms_and_condition_listbox.yview)

        tc=setup_info["terms and condition"]        
        for i in tc:
            terms_and_condition_listbox.insert(tk.END,i)

        
        #----------------------fucntion to change button state-----------------------------------------------
        
        quesiton_label=Label(TC_detailed_frame,text="If you agree to the terms and conditon please tick the checkbox",bg=background_color)
        quesiton_label.place(y=230,x=25)   
    
        check_var=IntVar()
        
        
        def change_state():
            if check_var.get()==1:
                next_button.config(state=tk.ACTIVE)                
            else:
                next_button.config(state=tk.DISABLED)
        
        agreeing_checkbutton=Checkbutton2(TC_detailed_frame,text="I agree to the condition",onvalue=1,
                                          offvalue=0,variable=check_var,command=change_state,takefocus=1)
        agreeing_checkbutton.place(y=260,x=25)

        #-----------------------3rd part:Button settings-------------------------------------------------------------------
        
        
        back_button = Button(self, text="back", relief="groove", width=10)
        back_button.place(x=370, y=370)
        
        next_button = Button(self, text="Next", relief="groove", width=10 ,state=tk.DISABLED)
        next_button.place(x=460, y=370)

        


class Software_activation_page(Frame):
    """
    This is class is used to enter the license key and verify the key.
    This frame is devided into 2 parts one for entering the key and another for button
    
    Initialization of the funciton of the class needs:
    *window_object:TK class root object
    *verification_function:A function name to verify key enterd
    
    """
    def __init__(self,window_object,verify_function=None):
        """
        Object initaialization takes two argumets:
        *window object and 
        *verification function which is called by function to verify entered key.
        
        """
        self.window_object=window_object
        super().__init__(window_object,bg="light grey",width=550,height=400)
        self.pack(fill="x")

        #---------------1st part:Company logo and name --------------------------------------------------------
        name_frame=Frame(self,width=550,height=70,bg="#7CB9E8")
        name_frame.place(x=0,y=0)
        company_name=Label(name_frame,text="Astra Softwares",font=("Arial",20,"bold"),bg="#7CB9E8")
        company_name.place(x=20,y=5)
        page_short_discription=Label(name_frame,text="Activate Your Software",bg="#7CB9E8",font=(10))
        page_short_discription.place(x=20,y=40)
        
        image=Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'software_icon.png'))
        resize_image=image.resize((100,60))
        image_object=ImageTk.PhotoImage(resize_image)
        photo_icon=Label(name_frame,image=image_object)
        photo_icon.image=image_object
        photo_icon.place(x=350,y=4)


        #-----------------------2nd part : Entry widget---------------------------------------------------------------

        activation_page_body=Frame(self,bg=background_color,width=550,height=280)
        activation_page_body.place(x=0,y=71)

        message_label=Label(activation_page_body,text="Before we move on please enter license key,so we can confirm ",
                            font=("Times New Roman",15),bg=background_color)
        message_label.place(x=0,y=0)
        message_label2=Label(activation_page_body,text="your purchase.",
                            font=("Times New Roman",15),bg=background_color)
        message_label2.place(x=0,y=20)

        license_key_label=Label(activation_page_body,text="Enter license key:",bg=background_color,font=70)
        license_key_label.place(x=0,y=50)

        
        message_variable=tk.StringVar()# this variable is used to send message on screen regarding key.

        def key_checking(entered_key):
            print(entered_key)
            if entered_key.isdigit() and len(entered_key)==12:
                if verify_function(entered_key):
                    message_label3.config(foreground='green')
                    message_variable.set('Key Verified')
                    message_label3.config(textvariable=message_variable)
                    time.sleep(2)
                    next_button.config(state=tk.ACTIVE)
                else:
                    message_label3.config(foreground='red')
                    message_variable.set('Key Invalid')
            else:
                message_label3.config(foreground='black')
                message_variable.set('Enter complete key')

            return True # return true after entering every key
        registerd_funciton=self.window_object.register(key_checking)



        license_key_entry=Entry2(activation_page_body,font=('arial',15))
        license_key_entry.place(x=160,y=50,width=300)
        license_key_entry.config(validate="key",validatecommand=(registerd_funciton,'%P'))
        message_label3=Label(activation_page_body,textvariable=message_variable,font=(30),bg=background_color,foreground="Green")
        message_label3.place(x=280,y=80)

        def send_error():
            messagebox.showerror("Astra Says","""If You don't have a key "fuck off!" """)
        no_key_button = Button(activation_page_body, text="I don't have a key", relief="flat", width=10,activeforeground="red",cursor="hand2",command=send_error)
        no_key_button.place(x=160, y= 80,width=100)



        #-----------------------3rd part:Button settings---------------------------------------------------------------     
        back_button = Button(self, text="back", relief="groove", width=10)
        back_button.place(x=370, y=360)
        
        next_button = Button(self, text="Next", relief="groove", width=10 ,state=tk.DISABLED)
        next_button.place(x=460, y=360)


class Name_registration_page(Frame):
    """
    This frame is used to get the hospital name 
    this frame has three parts:
    *one for company name 
    *one for entry label 
    *one for buttons.

    To create object of class:
    *window_object:
    """
    def __init__(self,window_object,register_name):
        self.window_oject=window_object
        super().__init__(window_object,bg="light grey",width=550,height=400)
        self.place(x=0,y=0)

        #---------------1st part:Company logo and name --------------------------------------------------------
        name_frame=Frame(self,width=550,height=70,bg="#7CB9E8")
        name_frame.place(x=0,y=0)
        company_name=Label(name_frame,text="Astra Softwares",font=("Arial",20,"bold"),bg="#7CB9E8")
        company_name.place(x=20,y=5)
        page_short_discription=Label(name_frame,text="Register Name",bg="#7CB9E8",font=(10))
        page_short_discription.place(x=20,y=40)
        
        image=Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'software_icon.png'))
        resize_image=image.resize((100,60))
        image_object=ImageTk.PhotoImage(resize_image)
        photo_icon=Label(name_frame,image=image_object)
        photo_icon.image=image_object
        photo_icon.place(x=350,y=4)

        #----------------------2nd part :Name entry widgets----------------------------------------------------------- 
        
        #variables of the frame
        message_variable=tk.StringVar()
        message_variable.set("Please enter the name of the hospital.")

        message_variable2=tk.StringVar()

        name_varible=tk.StringVar()



        def name_checking(name):
            print(name)
            if name.isalpha() and len(name)>3:
                message_variable2.set('Name Valid')
                message_label3.config(foreground='green')
                next_button.config(state=tk.ACTIVE)
                return True
            else:
                message_label3.config(foreground='red')
                message_variable2.set('Name Invalid')
                next_button.config(state=tk.DISABLED)
                return True 
            return True

        registered_function=window_object.register(name_checking)


        
        main_frame=Frame(self,bg=background_color,width=550,height=280)
        main_frame.place(x=0,y=71)
        message_label=Label(master=main_frame,textvariable=message_variable,bg=background_color,font=(15))
        message_label.place(x=5,y=2)
        message_label2=Label(master=main_frame,text="Hospital Name:",bg=background_color,font=("Lucida Console",15))
        message_label2.place(x=5,y=30)

        name_entry=Entry2(master=main_frame,font=("Lucida Console",20),textvariable=name_varible)
        name_entry.place(y=60,x=7,width=525)
        name_entry.config(validate="key",validatecommand=(registered_function,'%P'))

        message_label3=Label(master=main_frame,textvariable=message_variable2,font=(30),bg=background_color)
        message_label3.place(x=250,y=100)



        #-----------------------3rd part:Button settings---------------------------------------------------------------     
        back_button = Button(self, text="back", relief="groove", width=10)
        back_button.place(x=370, y=360)
        
        def register_name_function():
            register_name(name_varible.get())


        next_button = Button(self, text="Next", relief="groove", width=10 ,state=tk.DISABLED,command=register_name_function)
        next_button.place(x=460, y=360)

   

class DBMS_setup_page(Frame):
    """
    This class is used to display a DBMS page.
    """
    def __init__(self,window_object):
        pass
        
    
class Admin_setup_page(Frame):
    """
    This page is used to get the root ID and password of the setup window.
    To creat the object of this frame two arguments are needed:
    *window_object: Object of 'TK' class 
    *verify_DBMS: a fucntion to test root login,password and host of DBMS,returns a boolean algebra.

    """
    def __init__(self,window_object,DBMS_verification):
        self.window_oject=window_object
        super().__init__(window_object,bg="light grey",width=550,height=400)
        self.place(x=0,y=0)

        #---------------1st part:Company logo and name --------------------------------------------------------
        name_frame=Frame(self,width=550,height=70,bg="#7CB9E8")
        name_frame.place(x=0,y=0)
        company_name=Label(name_frame,text="Astra Softwares",font=("Arial",20,"bold"),bg="#7CB9E8")
        company_name.place(x=20,y=5)
        page_short_discription=Label(name_frame,text="Data Base Connection",bg="#7CB9E8",font=(10))
        page_short_discription.place(x=20,y=40)
        
        image=Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'software_icon.png'))
        resize_image=image.resize((100,60))
        image_object=ImageTk.PhotoImage(resize_image)
        photo_icon=Label(name_frame,image=image_object)
        photo_icon.image=image_object
        photo_icon.place(x=350,y=4)

        #-------------------------2nd part: main content---------------------------------------------------------
    
        main_frame=Frame(self,bg=background_color,width=550,height=280)
        main_frame.place(x=0,y=71)
        
        instruction_variable=tk.StringVar()
        instruction_variable.set('Please enter the IT Head id and password and host')

        instruction_label=Label(main_frame,bg=background_color,textvariable=instruction_variable,font=(10))
        instruction_label.place(x=5,y=5)
        
        id_variable=tk.StringVar()
        password_variable=tk.StringVar()
        host_variable=tk.StringVar()
        warning_variable=tk.StringVar()
        
        id_label=Label(master=main_frame,text="Admin Id:",font=(10),bg=background_color)
        id_label.place(x=5,y=35)
        id_entry=Entry2(master=main_frame,textvariable=id_variable,font=(10))
        id_entry.place(x=200,y=35)

        password_label=Label(master=main_frame,text="Admin password:",font=(10),bg=background_color)
        password_label.place(x=5,y=70)
        password_entry=Entry2(master=main_frame,textvariable=password_variable,font=(10))
        password_entry.place(x=200,y=70)

        host_label=Label(master=main_frame,text="DataBase host:",font=(10),bg=background_color)
        host_label.place(x=5,y=105)
        host_entry=Entry2(master=main_frame,textvariable=host_variable,font=(10))
        host_entry.place(x=200,y=105)
        
        def verify_dbms():
            return_value=DBMS_verification(id_variable.get(),password_variable.get(),host_variable.get())
            if return_value==None:
                messagebox.showinfo("Astra Says","DBMS connection successful!")
                pass
            else:
                warning_variable.set(str(return_value))
                messagebox.showerror("Astra Says",message=str(return_value))
                
            

        verify_button=Button(master=main_frame,text="verify connection",relief='groove',command=verify_dbms)
        verify_button.place(x=200,y=140)

        #-----------------------3rd part:Button settings---------------------------------------------------------------     
        back_button = Button(self, text="back", relief="groove", width=10)
        back_button.place(x=370, y=360)
        
        next_button = Button(self, text="Next", relief="groove", width=10 ,state=tk.DISABLED)
        next_button.place(x=460, y=360)



        


class Cloud_setup_page(Frame):
    pass

    



if __name__=='__main__':
    # Frame Verification tests.
    
    root=Window()
    root=root.setup_window()
    
    
    #setup_page=Welcome_page(root)
    #terms_condition_page=Terms_condition_page(root)
    #key_page=Software_activation_page(root)

    # activation page setup
    """
    """
    def verify(e):
        return True
    key_page=Software_activation_page(root,verify)
    
    
    # name registration page setup
    """
    def register_name(e):
        print("hi"+e)
        return None

    name=Name_registration_page(root,register_name)
    """
    
    #admin setup page test
    """
    def test_function(a,b,c):
        print(a,b,c)
        return None


    page=Admin_setup_page(root,test_function)
    """

    root.mainloop()
