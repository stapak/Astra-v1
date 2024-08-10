"""
File contains all the frames class related to IT interface.

"""



from time import sleep
from threading import Thread



# Tkinter Libraries.

from tkinter import  END, SCROLL, Button, Frame, IntVar, Label, LabelFrame
from tkinter import Listbox, Menu, Scrollbar, StringVar ,Text, Toplevel,messagebox
from tkinter.ttk import Labelframe,Entry,Combobox,Checkbutton


#---------------------------------------Variable/attributes of file ---------------------------------------

BACKGROUND_COLOR="#DCDCDC"
BASIC_FONT=('Lucida Console',15) 
ENTRY_FONT=('Lucida Console',12)
normal_bold_font=("Arial",15,"bold")
normal_font=("Arial",10)


class IT_Base():
    """
    Class used to contain base setting for all "IT" frames. This class is separated from the base class because menu options are more and need 
    be programmed separatly.
    """
    @staticmethod
    def menubar_setup(window_object,function_list):
       
        # Function of the frame
        def about_us():
            """
            Function used by about us menu bar option.
            """
            import webbrowser
            webbrowser.open_new("https://www.youtube.com/shorts/SXHMnicI6Pg")

        def database_workspace():
            workspace_widget=IT_Database_Workspace(window_object,function_list['execute query'])
            
        #---------------------------------------------------------------------- Menu Bar --------------------------------------------------
        main_menu=Menu(master=window_object)
        

        #------------------------------ View sub menu----------------------------
        workspace_submenu=Menu(master=main_menu,tearoff=0)
        main_menu.add_cascade(label="Workspace",menu=workspace_submenu)
        
        # View Options
        workspace_submenu.add_command(label="Dashboard",command=None)
        workspace_submenu.add_command(label="Monitor",command=None)
        workspace_submenu.add_command(label="Database Workspace",command=database_workspace)
        
        #------------------------------Edit Sub-Menu -------------------------------
        edit_submenu=Menu(master=main_menu,tearoff=0)
        main_menu.add_cascade(label="Edit",menu=edit_submenu)
        
        # User related options
        user_menu=Menu(master=edit_submenu,tearoff=0)
        user_menu.add_command(label="Add user",command=None)   
        user_menu.add_command(label="remove user",command=None)
        user_menu.add_command(label="Edit user",command=None)

        # Department related options.
        department_menu=Menu(master=edit_submenu,tearoff=0)
        department_menu.add_command(label="Add Department",command=None)
        department_menu.add_command(label="Remove Department")
        department_menu.add_command(label="Edit Department")
        

        edit_submenu.add_cascade(label="edit user",menu=user_menu)
        edit_submenu.add_cascade(label="edit department",menu=department_menu)
        
        #------------------------------ Export sub menu ----------------------------
        export_submenu=Menu(master=main_menu,tearoff=0)
        main_menu.add_cascade(label="Export",menu=export_submenu)

        export_submenu.add_command(label="Patient Details")
        export_submenu.add_command(label="Hospital Details")
        
        #------------------------------ Account sub menu ---------------------------
        account_submenu=Menu(master=main_menu,tearoff=0)
        main_menu.add_cascade(label="Account",menu=account_submenu)
        account_submenu.add_command(label="View Account",command=None)
        account_submenu.add_command(label="Edit",command=None)
        account_submenu.add_separator()
        account_submenu.add_command(label="Logout",command=None)
        
        #----------------------------- Help sub Menu -------------------------------
        help_submenu=Menu(master=main_menu,tearoff=0)
        main_menu.add_cascade(label="Help",menu=help_submenu)
        
        help_submenu.add_command(label="About",command=about_us)
        help_submenu.add_command(label="Working",command=None)
        help_submenu.add_command(label="Contact Us",command=None)
        window_object.config(menu=main_menu)
    
        


class ITBaseFrame(Frame):
    """
    BaseClass for all IT frame classes.It initializes height widht and menubar of the frame.
    """
    def __init__(self,window_object,backend_functions=None):
        super().__init__(window_object,bg="light grey",width=1535,height=775)
        self.place(x=0,y=0)
        IT_Base.menubar_setup(window_object,backend_functions)




class ITDashBoard(ITBaseFrame):
    """
    Class containing frame for dash board of IT head.
    """
    FRAME_NAME="ITDashBoard"
    
    def __init__(self,window_object,backend_functions=None):
        super().__init__(window_object,)
       

        #------------------------------ Login frame
        login_frame=Frame(master=self,width=1000,height=775,bg="black")
        login_frame.place(x=0,y=0)
        
        # Functions of frame
        
        def display_table():
            """
            the function that calls it self to update the login register,this function works on a thread.
            """
            display_input=backend_functions['login register']()
            
            login_listbox.insert(0,"User Name                                                    | login time                                                                  | logout time                                                      | Status                        ")
            for i in display_input:
                 line=str(i[0])+"                                             "+str(i[1])+"                                                      "+i[2]
                 login_listbox.insert(END,line)

            sleep(5)
            login_listbox.delete(0,END)
            display_table()
                
            
        
        # Frame Widgets
        login_label=Label(master=login_frame,text="Login Register",background=BACKGROUND_COLOR,font=('Lucida Console',20),foreground="#FF0000",borderwidth=10)
        login_label.place(x=5,y=5,width=990)        

        scrollbar=Scrollbar(master=login_frame,orient="vertical",relief="groove")
        scrollbar.place(x=978,y=50,height=715)        

        login_listbox=Listbox(master=login_frame,yscrollcommand=scrollbar.set,background=BACKGROUND_COLOR)
        login_listbox.place(x=5,y=50,height=715,width=975)
        
        
        register_thread=Thread(target=display_table)
        register_thread.start()
        



        scrollbar.config(command=login_listbox.yview)
        
         
        
    

class IT_Database_Workspace(Toplevel):
    """
    Top level entity is used for a workspace for IT head to work and interact with data base directly through queries.
        INPUT:
        *Execute_query  :  function  to execute the query .
        *current_object : Object of Tk class to create toplevel entity. 
    """
    FRAME_NAME="DataBase WorkSpace"
    def __init__(self,current_object,execute_query=None):
        super().__init__(master=current_object)
        self.title("Astra DataBase Connector")
        width=800
        height=500
        xpoint=250
        ypoint=100
        self.geometry(f'{width}x{height}+{xpoint}+{ypoint}')
        self.resizable(width=False,height=False)
        
        # Execution Frame
        self.output=None#variable to store output globally
        def call_function():
            query=input_box.get("1.0", "end-1c")
            print(query)
            self.output=execute_query(query)
            for i in self.output:
                line=""
                for j in i:
                    line= line + str(j)+"  "
                    output_listbox.insert(END,line)
        

            
        execution_frame=LabelFrame(master=self,width=800,height=250,text="Enter Queries")
        execution_frame.place(x=0,y=0)
        
        input_box=Text(master=execution_frame,font=ENTRY_FONT,background='light blue')
        input_box.place(x=10,y=10,height=190,width=776)
        
        execute_button=Button(master=execution_frame,text="Execute",relief='groove',command=call_function)
        execute_button.place(x=720,y=203,width=60)
        
        #output frame
        output_frame=LabelFrame(master=self,text="Output",height=250,width=800)
        output_frame.place(x=0,y=250)
        
        output_yscrollbar=Scrollbar(master=output_frame,orient='vertical',relief='groove')
        output_yscrollbar.place(y=0,x=770,height=230,width=20)
        
        output_xscrollbar=Scrollbar(master=output_frame,orient='horizontal',relief='groove')
        output_xscrollbar.place(y=210,x=5,height=20,width=765)
        
        output_listbox=Listbox(master=output_frame,bg='light blue',xscrollcommand=output_xscrollbar.set,yscrollcommand=output_yscrollbar.set)
        output_listbox.place(x=5,y=0,height=210,width=770)
        
        output_yscrollbar.config(command=output_listbox.yview)
        output_xscrollbar.config(command=output_listbox.xview)
        
        
          
        self.mainloop()

        

class ITAddUser(ITBaseFrame):
    """
    Frame to add user by collecting user details.
        INPUT
       
    """
    def __init__(self,window_object):
        super().__init__(window_object)
        
        #--------------------------------------- Main Fucntions of the Frame ----------------------------------------------------------
        def add_user():
            """
            Function used to check all the variables and use external function to register user.
            
            """
            pass

        def cancel():
            """
            Function used to ask confirmation of the user before destroying the frame object.
            
            """
            output=messagebox.askyesno("Astray Says","Do you want to leave without adding user?")
            if output:
                self.destroy()
            
        #---------------------------------------- Heading Frame -----------------------------
        heading_frame=Frame(master=self,height=50,width=1535,bg='light blue')
        heading_frame.place(x=0,y=0)
        
        name_label=Label(master=heading_frame,text="Add User",bg='light blue',font=('Lucida Console',25,'bold'))
        name_label.place(x=5,y=5)
        
        cancel_button=Button(master=heading_frame,text='Cancel',font=BASIC_FONT,relief='groove',activeforeground='white',activebackground='red',command=cancel)
        cancel_button.place(x=1300,y=10)
        
        add_button=Button(master=heading_frame,text='Add User',font=BASIC_FONT,relief='groove',activeforeground='white',activebackground='green', command=add_user)
        add_button.place(x=1400,y=10)
        
        #----------------------------------------- Entry Frame --------------------------------
        entry_frame=Frame(master=self,height=725,width=1535,bg='light grey')
        entry_frame.place(x=0,y=50)
        
        # Frame Variables
        name_var=StringVar()
        id_proof_var=StringVar()
        id_number_var=StringVar()
        gender_var=StringVar()
        permanent_address_var=StringVar()
        current_address_var=StringVar()
        copy_details_var=IntVar()
        
        # Frame Functions
        def copy_details():
            """
            Function used to copy the current address to permanet address variable.
            """
            if copy_details_var.get():
                 current_address_var.set(current_address_text.get("1.0", "end-1c"))
                 permanent_address_var.set(current_address_var.get())
            else:
                permanent_address_var.set('')
        
        # Personal details
        personal_details_frame=Labelframe(master=entry_frame,text='Personal Details',height=400,width=1535)
        personal_details_frame.place(x=0,y=0)
        
        name_label=Label(master=personal_details_frame,text="Name:",font=BASIC_FONT)
        name_label.place(x=5,y=5)
        name_entry=Entry(master=personal_details_frame,textvariable=name_var,font=ENTRY_FONT,width=16)
        name_entry.place(y=2,x=70,height=35,width=300)
        
        gender_label=Label(master=personal_details_frame,text="Gender:",font=BASIC_FONT)
        gender_label.place(x=390,y=5)
        gender_combox=Combobox(master=personal_details_frame,width=14,font=BASIC_FONT,textvariable=gender_var)
        gender_combox['values']=('Male','Female','Other')
        gender_combox.place(x=480,y=5)
        
        IDproof_label=Label(master=personal_details_frame,text="ID proof:",font=BASIC_FONT)
        IDproof_label.place(y=5,x=700)
        IDproof_combox=Combobox(master=personal_details_frame,font=BASIC_FONT,textvariable=id_proof_var,width=15)
        IDproof_combox['values']=['Adhar card','Driving Licence','Passprot','Pancard']
        IDproof_combox.place(x=815,y=5)
        
        IDnumber_label=Label(master=personal_details_frame,text="ID proof no.:",font=BASIC_FONT)
        IDnumber_label.place(y=5,x=1050)
        IDnumber_entry=Entry(master=personal_details_frame,textvariable=id_number_var,font=ENTRY_FONT,width=20)
        IDnumber_entry.place(y=2,x=1220,height=35)
        
        current_address_label=Label(master=personal_details_frame,text="Current Address:",font=BASIC_FONT)
        current_address_label.place(x=0,y=55)
        address_scrollbar=Scrollbar(master=personal_details_frame,orient='vertical',relief="groove")
        address_scrollbar.place(x=1490,y=85,width=20,height=100)
        current_address_text=Text(master=personal_details_frame,font=ENTRY_FONT,yscrollcommand=address_scrollbar)
        current_address_text.place(x=10,y=85,height=100,width=1480)
        address_scrollbar.config(command=current_address_text.yview)
        
        copy_address_checkbox=Checkbutton(master=personal_details_frame,text="Permanent address same as current address",onvalue=1,offvalue=0,command=copy_details,variable=copy_details_var)
        copy_address_checkbox.place(x=5,y=190)
        
        
        permanent_address_label=Label(master=personal_details_frame,text="Permanent Address:",font=BASIC_FONT)
        permanent_address_label.place(x=0,y=220)
        address_scrollbar=Scrollbar(master=personal_details_frame,orient='vertical',relief="groove")
        address_scrollbar.place(x=1490,y=250,width=20,height=100)
        permanent_address_text=Text(master=personal_details_frame,font=ENTRY_FONT,yscrollcommand=address_scrollbar)
        permanent_address_text.place(x=10,y=250,height=100,width=1480)
        address_scrollbar.config(command=permanent_address_text.yview)
        
        # ---------------------------------------- Proffessional details -----------------------------------------------
        post_var=StringVar()
        
        proffessional_details_frame=Labelframe(master=entry_frame,text='Proffessional Details',height=310,width=1535)
        proffessional_details_frame.place(x=0,y=400)
        
        education_label=Label(master=proffessional_details_frame,text="Education:",font=BASIC_FONT)
        education_label.place(x=0,y=20)
        address_scrollbar=Scrollbar(master=proffessional_details_frame,orient='vertical',relief="groove")
        address_scrollbar.place(x=510,y=50,width=20,height=100)
        education_text=Text(master=proffessional_details_frame,font=ENTRY_FONT,yscrollcommand=address_scrollbar)
        education_text.place(x=10,y=50,height=100,width=500)
        address_scrollbar.config(command=education_text.yview)
        
        post_label=Label(master=proffessional_details_frame,text="Post:",font=BASIC_FONT)
        post_label.place(x=0,y=180)
        post_entry=Entry(master=proffessional_details_frame,font=ENTRY_FONT,width=44,textvariable=post_var)
        post_entry.place(x=65,y=175,height=35)
            
        
       
        
        
    
if __name__=='__main__':
    from software_windows import Window
    root=Window()
    root=root.normal_window()
    #it=ITDashBoard(root)
    #testing_frame=IT_Database_Workspace()
    #itframe_testing=IT_Database_Workspace(root)
    ittest2=ITAddUser(root)
    root.mainloop()