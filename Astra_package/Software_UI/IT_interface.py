"""
File contains all the frames class related to IT interface.

"""

from distutils.util import execute
from time import sleep
from threading import Thread



# Tkinter Libraries.

from tkinter import  END, Button, Frame, Label, LabelFrame, Listbox, Menu, Scrollbar ,Text, Toplevel
from tkinter.ttk import Labelframe
from turtle import back

#---------------------------------------Variable/attributes of file ---------------------------------------

BACKGROUND_COLOR="#DCDCDC"
BASIC_FONT=('Lucida Console',15) 
entry_font=('Lucida Console',12)
normal_bold_font=("Arial",15,"bold")
normal_font=("Arial",10)


class IT_Base():
    """
    Class used to contain base setting for all "IT" frames. 
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
        

class ITDashBoard(Frame):
    """
    Class containing frame for dash board of IT head.
    """
    FRAME_NAME="ITDashBoard"
    
    def __init__(self,window_object,backend_functions=None):
        super().__init__(window_object,bg="light grey",width=1535,height=775)
        self.place(x=0,y=0)
        IT_Base.menubar_setup(window_object,backend_functions)

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
        
        input_box=Text(master=execution_frame,font=entry_font,background='light blue')
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

        
        
       
        
        
    
if __name__=='__main__':
    from software_windows import Window
    root=Window()
    root=root.normal_window()
    #it=ITDashBoard(root)
    #testing_frame=IT_Database_Workspace()
    itframe_testing=IT_Database_Workspace(root)
    root.mainloop()