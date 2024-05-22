Project : Astra v1
Aim : A Medical software to manage hospital staff and hospital services.

Features: 1.User Managment(hospital staff)
          2.Patient Management(patients personal detials,Medications,Session Outcome)
          3.File system
          4.Good graphical User Interface
          5.Cloud File Managment(if possible)

Future Updates:
                a.Table can be arranged in for a single medicine and its dosage changes per session
-------------------------------------------------------------------Feature Description----------------------------------------------------------
1.User Managment:
    Requirements: a.Every staff should be access all patients from the database.
                  b.Every staff should be able to access only the specific amount of data about the patient related to the work of the staff.
                  c.From the same login interface for every user, based on the user new dashboard.
                   


********************************************************************

2.Patient Managment:
    Requirements: a.should contain pesonal details(patient id,name,address,health diagnostic info) 
                  b.able to be used by multiple hospital staff(doctor booking by front desk,health report edited by doctors,
                                                              dianostic reports by diagnostic center,pharmacists to provide 
                                                              medicines.)
                  c.Should be able maintain records (such asevery session,current medications and treatments,future session 
                                                    dates and necessary diagnostics before session and other).
                  d.If possible it should maintain a digital copy of every diagnostic (such as mri reports,blood test reports etc.)
    
    Working: Patient details can be devided into 
                1.Permanent information(such as name,address,blood group,phone no,date of birth,id,first healt problem and diagnostics).
                  *these can be stored in common table which include data of all the patients,onece inserted will be changed only on special case.
                2.Session Information or diagnostic information
                  *these can be sotred in table one per patient containing all the information of all the session.
    
    Code discription: class cards
                        class client-----------------------------------
                            Fields:
                                *name           *address
                                *phone no       *date_of_birth
                                *blood group    *Initial_diagnostics
                                *Doctor_name
       
                            -------------------------------------------
                            Behaviours:
                                *Register         *Diagnostics_recomendation_reports(if possible)
                                *Session_result   *conclude_treatment
                                *Medications      *_create_table
                                *Treatment        *_orgnize

    

....................................................................................................................................
