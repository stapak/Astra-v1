# Structure of Software
This file contains all the information regarding working of software and code discription.
## Package structure
* Software is executed from ***Software_execution.py*** file that imports all funtions from ***astra package*** which contains all the source code of the software.
* Astra package codes are further divided into sub-packages and moudle files.
* Astra package structure:

		Astra v1/
		  |
		  |-----.gitignore
		  |
		  |-----Software_execution.py
		  |
		  |-----README.md
		  |
		  |-----SOFTWARE_WORKING.md
		  |
		  |-----Astra_package/
		           |-----__init__.py
		           |								               |-----software_boot_function.py
	               |
		           |-----Software_backend/
		           |
		           |-----Software_UI/
	               |
	               |-----sql_commands/
										  

*Software_execution.py*:
* 'Software_execution.py' file is used to call function from inside the package,subpackages and module.this file is just an execution
file and no working code is written in this file.
******
## Modules of package
### **__ init __.py**:
* This file contains the 'frame_list' which is used to store all the objects of the frame classes.
* Other initializations for creating a top level package.

### **software_boot_function.py**:
* This funtion contains all the code which initialize the list elements used in displaying the frame.
* Contains function to initialize frame objects and append them in the frame list.
* Contains funtion to call required frame from that frame list.
* Contains mediator functions which act as link between **UI** frames and backend methods.
* This file/module uses the subpackages related to **user-interface** and **backend** of software
***
## Subpackages of package
All the codes of software is devided into two parts:
* ***Software_UI*** which contains all the user interface frame classes , reltated functions etc.
* ***Softwaer_backend*** which contains all the code for managing the backend work such as creating


### Software_UI:
This subpackage contains all the user interface module which are built through tkinter frames class


### software_backend:
Subpackage contains all the module necessary for backend functioning of software such as communicating with database, or other works.	
	
***
# Working of software Step-by-step.
### working of setup:
Setup is used to setup the software and setup database.

	* Firstly,setup greets the user and shows agreement and terms of use of the software.
	* Afterwards license key is asked from user once proper key is entered then user is taken to next page.
	* In next step user is asked for new setup or recover from previous setup.
	* If it is new setup user is asked for a directory to store the basic info file or if it s old setup then basic info file location is asked.
 




