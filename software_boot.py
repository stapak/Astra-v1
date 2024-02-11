"""
This file is used to start the software.
"""

import json
from Software_backend.first_boot import start_boot

path="boot_info.json"
with open(path) as file:
    boot_info=json.load(file)['first_boot']

def start(hospital_name=None):
    if  not boot_info['DBMS_ready']:
        start_boot(hospital_name)
        boot_info['DBMS_ready']=True
        print('hi',boot_info['DBMS_ready'])
        with open(path,'w') as file:
            json.dump(boot_info,file)
    
    else:
        print('hello',boot_info['DBMS_ready'])


   


