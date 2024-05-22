"""
This file contains all the code related to the setup window of the software
"""

from software_windows import Window
from tkinter import Frame
from tkinter import Label
from tkinter import Button
from tkinter import Radiobutton
from tkinter import Checkbutton as Checkbutton1
from tkinter import Scrollbar
from tkinter import PhotoImage
import tkinter as tk
from tkinter import Listbox
from tkinter import IntVar

from tkinter.ttk import Label as Label2
from tkinter.ttk import Checkbutton as Checkbutton2
from tkinter.ttk import Entry as Entry2
from tkinter.ttk import Scrollbar as Scrollbar2

from PIL import Image,ImageTk
import json
import os

#---------------------------------------Variable/attributes of file ---------------------------------------




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
        details_frame=Frame(self,bg="#DCDCDC",height=350,width=370)
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
        TC_detailed_frame=Frame(self,width=550,height=290,bg="#DCDCDC")
        TC_detailed_frame.place(y=71,x=0)
        head_label=Label(TC_detailed_frame,text="Terms and Conditon of Use",font=("Arial",10,"bold"),bg="#DCDCDC")
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
        
        quesiton_label=Label(TC_detailed_frame,text="If you agree to the terms and conditon please tick the checkbox",bg="#DCDCDC")
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
        page_short_discription=Label(name_frame,text="Activate Your Software",bg="#7CB9E8",font=(10))
        page_short_discription.place(x=20,y=40)
        
        image=Image.open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'software_icon.png'))
        resize_image=image.resize((100,60))
        image_object=ImageTk.PhotoImage(resize_image)
        photo_icon=Label(name_frame,image=image_object)
        photo_icon.image=image_object
        photo_icon.place(x=350,y=4)


        #-----------------------2nd part : Entry widget---------------------------------------------------------------

        activation_page_body=Frame(self,bg="#DCDCDC",width=550,height=280)
        activation_page_body.place(x=0,y=71)

        """
        heading_label=Label(activation_page_body,text="Activate Your Software",font=("Arial",30,"bold"),bg="#DCDCDC")
        heading_label.place(x=50,y=0)"""

        message_label=Label(activation_page_body,text="Before we move on please enter license key,so we can confirm ",
                            font=("Times New Roman",15),bg="#DCDCDC")
        message_label.place(x=0,y=0)
        message_label2=Label(activation_page_body,text="your purchase.",
                            font=("Times New Roman",15),bg="#DCDCDC")
        message_label2.place(x=0,y=20)

        license_key_label=Label(activation_page_body,text="Enter license key:",bg="#DCDCDC",font=(70))
        license_key_label.place(x=0,y=50)

        key=tk.StringVar()
        key.set('XXXX-XXXX')
        license_key_entry=Entry2(activation_page_body,textvariable=key,font=(15))
        license_key_entry.place(x=130,y=50,width=300)

        back_button = Button(activation_page_body, text="I don't have a key", relief="flat", width=10,activeforeground="red",
                             cursor="hand2")
        back_button.place(x=130, y= 80,width=100)


        #-----------------------3rd part:Button settings---------------------------------------------------------------     
        back_button = Button(self, text="back", relief="groove", width=10)
        back_button.place(x=370, y=360)
        
        next_button = Button(self, text="Next", relief="groove", width=10 ,state=tk.DISABLED)
        next_button.place(x=460, y=360)

        


    def verify_key():
        pass

class Name_registration_page(Frame):
    """
    This frame is used to get the hospital name 
    this frame has three parts:
    *one for company name 
    """
    def __init__(self,window_object):
        self.window_oject=window_object
        super().__init__(window_object,bg="light grey",width=550,height=400)
        self.pack(fill="x")




    

class DBMS_setup_page(Frame):
    pass
    
class Root_setup_page(Frame):
    pass

class Cloud_setup_page(Frame):
    pass

    


        
        


if __name__=='__main__':
    root=Window()
    root=root.setup_window()
    #setup_page=Welcome_page(root)
    #terms_condition_page=Terms_condition_page(root)
    key_page=Software_activation_page(root)
    root.mainloop()
