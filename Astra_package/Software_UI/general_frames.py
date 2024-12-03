"""
This file contains the general frames used by every user.
"""

# BuiltIn modules
import json
import sys
import time
from tkinter import Button, Frame, Label, Listbox, Scrollbar, StringVar, Toplevel, messagebox 
import tkinter as tk
#from ..AstraThreads import AstraThread
from multiprocessing import Process
from threading import Thread

from tkinter.ttk import Entry
from tkinter.ttk import Progressbar





width=700
height=500
BACKGROUND_COLOR="#DCDCDC"

"""

from ..Software_backend import _SOFTWARE_INFO_FILE_PATH
with open(_SOFTWARE_INFO_FILE_PATH) as jobj:
    HOSPITAL_NAME=json.load(jobj)["Hospital_Name"]

"""
HOSPITAL_NAME="testing"

class LoginPage(Frame):
    """
    This class is used to construct frames related to login page. Login page consists of three frames
    *one to display hospital name.
    *one for entry box of username and password.
    *one for loading screen.
   
    """
    def __init__(self,window_object,login_function,destroy_frame):
        """
        Object initialization of the class takes :
        *object of tkinter's tk class.
        *a function to login user.
        *
        """
        super().__init__(master=window_object,width=700,height=500)
        self.place(x=0,y=0)
        
        self.login_status=False # used to determine the statu of the login
                
        # Functions of the frame
        def login():
            """
            This function is used to start process and terminate them.
            """
            if check_credentials():
                progress_bar_frame.tkraise()
                show_progressbar_thread.start()
                start_login_thread.start()
                
                
        
        def check_credentials():
            """
            Function used to check the characters of the user credentials. 
            """
            if user_name_variable.get().lower() == 'root' :
                messagebox.showerror("Astra Says","Root Id can be only used on SQL server.")
                return False
            banned_characters=['"',"'"]
            for i in user_name_variable.get():
                if i in banned_characters:
                    messagebox.showerror("Astra Says","Incorrect user name")
                    return False
            
            for i in password_variable.get():
                if i in banned_characters:
                    messagebox.showerror("Astra Says","Incorrect password")
                    return False
            if user_name_variable.get() =='' :
                messagebox.showerror("Astra Says","Enter the username")
                return False
            elif password_variable.get() == '':
                messagebox.showerror("Astra Says","Enter password")
                return False
            else:
                return True
        
        def login_user():
            """
            This function is used to call the 'login function' and login the user.
            """
            data={}
            data["user name"]=user_name_variable.get()
            data["password"]=password_variable.get()
            
            self.login_status=login_function(**data)
            if self.login_status:
                show_progressbar_thread.join()
                destroy_frame()
                sys.exit()
               
            else:
                messagebox.showerror("Astra Says","Login Failed !")
                entry_frame.tkraise()
                show_progressbar_thread.join()
                sys.exit()
            
         
        def show_progressbar():
            """
            Function used to control the progress bar
            """
            i=0
            progress_variable=0           
            while(not self.login_status):
                while(i==0):
                    if progress_variable<=100:
                         progress_bar['value']=progress_variable
                         progress_bar.update_idletasks()
                         progress_variable+=10
                         time.sleep(0.5)
                    else:
                        i=1
                while(i==1):
                    if progress_variable>=0:
                         progress_bar['value']=progress_variable
                         progress_bar.update_idletasks()
                         progress_variable-=10
                         time.sleep(0.5)
                    else:
                        i=0
            return 
        
        def forgot_password(element):
            """
            """
            messagebox.showinfo("Astra Says","Contact admin to change password")
        
    
        # Thread of class
        show_progressbar_thread=Thread(target=show_progressbar,name="show progress bar")
        start_login_thread=Thread(target=login_user,name="Start Login")
        

        #---------------------- 1st Frame:Name Frame --------------------------------------------------
        
        name_frame=Frame(master=self,width=700,height=300,background=BACKGROUND_COLOR)
        name_frame.place(x=0,y=0)
            
        name_label=Label(master=name_frame,text=HOSPITAL_NAME,background=BACKGROUND_COLOR,font=("Arial",15))
        name_label.place(x=100,y=220)
        
        #-------------------- 2nd Frame: Entry Frame ---------------------------------------------------
        entry_frame=Frame(self,width=700,height=200,background=BACKGROUND_COLOR)
        entry_frame.place(x=0,y=301)
        

        user_name_variable=StringVar()
        password_variable=StringVar()
        

        user_name_label=Label(entry_frame,text="UserName",font=("Arial",15),background=BACKGROUND_COLOR)
        user_name_label.place(x=200,y=10)
        user_name_entry=Entry(entry_frame,textvariable=user_name_variable,font=("Arial",15))
        user_name_entry.place(x=300,y=10)
        
        password_label=Label(entry_frame,text="Password",font=("Arial",15),background=BACKGROUND_COLOR)
        password_label.place(x=200,y=50)
        password_entry=Entry(entry_frame,textvariable=password_variable,font=("Arial",15))
        password_entry.place(x=300,y=50)
        

        login_button=Button(master=entry_frame,text="Login",font=("lucida",10),background=BACKGROUND_COLOR,activebackground="#7CB9E8",relief="groove",
                            command=login)
        login_button.place(x=300,y=90,height=30,width=225)
        
        forgot_password_label=Label(master=entry_frame,text="forgot password ?",foreground="#EF0107",background=BACKGROUND_COLOR)
        forgot_password_label.place(x=430,y=130)
        forgot_password_label.bind(sequence="<Button>",func=forgot_password)
        
        #---------------------------------------- 3rd Frame : To show progressbar --------------------------------------------

        progress_bar_frame=Frame(self,width=700,height=200,background=BACKGROUND_COLOR)
        progress_bar_frame.place(x=0,y=301)
        
        message_label=Label(master=progress_bar_frame,text="Loading Please Wait........",font=("Arial",15),background=BACKGROUND_COLOR)
        message_label.place(x=230,y=55)
        
        progress_bar=Progressbar(master= progress_bar_frame,orient="horizontal",length=100,mode="indeterminate")
        progress_bar.place(x=200,y=85,height=30,width=300)
        
        entry_frame.tkraise()
        
        
        
class BaseSearchWindow(Toplevel):
    """
    This class represents search box for queriying through any of table.
    
    """
    USER_SELECTED_VALUE=None
    def __init__(self,window_object,window_title=None|str ,search_function = None):
        super().__init__(window_object,background=BACKGROUND_COLOR)
        width=600
        height=725
        xpoint=470
        ypoint=50
        self.geometry(f'{width}x{height}+{xpoint}+{ypoint}')
        self.resizable(width=False,height=False)
        
        # Variable Declaration
        pageTitle=tk.StringVar()
        pageTitle.set(window_title)
        search_variable=tk.StringVar()
        
        # Function Defination
        def search():
            """
            The function is used to use backend funtion and get the list of similar strings.
            """
            search_keyword=search_variable.get()
            output_list=search_function(search_keyword)
            for output in output_list:
                result_listbox.insert(tk.END,output)
        
        def select(trash):
            """
            This function is used to change the frame according to the desired frame once user clicks on any of the options inside the Listbox.
            this takes trash as arguments but as bind funtion passes some arguments when it calls the function.
            """
            selected_index=result_listbox.curselection()
            self.USER_SELECTED_VALUE=result_listbox.get(selected_index)
            
            
        # Widgets of the frame.
        page_title_label=Label(master=self,textvariable=pageTitle,font=("Arial",25),background="light blue")
        page_title_label.place(x=0,y=10,width=600)
        
        search_label=Label(master=self,text="Search:",font=("Arial",15),background=BACKGROUND_COLOR)
        search_label.place(x=10,y=80)
        
        search_entry=Entry(master=self,textvariable=search_variable,font=("Arial",15))
        search_entry.place(x=85,y=80,width=350)
        
        search_button=Button(master=self,text="Search",font=("Arial",10),command=search)
        search_button.place(x=450,y=80,width=100)
        #------------------------------------------------------------ 
        result_label=Label(master=self,text="Results",font=('Arial',15),background=BACKGROUND_COLOR)
        result_label.place(x=10,y=120)
        
        columns_name_label=Label(master=self,text="Names\t\t\t\t\tID",font=('Arial',15),background=BACKGROUND_COLOR)
        columns_name_label.place(x=25,y=150)
        
        result_scrollbar=Scrollbar(master=self,orient='vertical')
        result_scrollbar.place(x=560,y=180,height=532)
        
        result_listbox=Listbox(master=self,width=88,height=33,yscrollcommand=result_scrollbar.set)
        result_listbox.place(x=25,y=180)
        
        result_scrollbar.config(command=result_listbox.yview)
        result_listbox.bind('<<ListboxSelect>>',select)
        
        

if __name__=='__main__':
    from software_windows import Window
    root=Window()
    root=root.login_window()
    
    """
    def login(**data):
        return True
    def destroy():
        root.destroy()
        sys.exit()
    frame_root=LoginPage(root,login,destroy)
    """
    def testing1(test):
        return ['1','2','3','4\\']    
    testing=BaseSearchWindow(root,"sample testing",testing1)
    
    root.mainloop()
    testing.mainloop()
    
    print(testing.USER_SELECTED_VALUE)