"""
contains general functions of the backend.
rules of backend function:
*Every function must specify input and output of it in discription.
*Every fucntion must have it's name stored in variable 'FUCNTION NAME'.
"""
from json import load
import os

from uuid import uuid4 

def ID_generator():
    raw_id=str(uuid4())
    id_sliced=raw_id.split('-')
    id_joined=''.join(id_sliced)
    generated_id=id_joined[0:20]
    return generated_id


# Inside '__SOFTWARE_INFO_FILE_PATH__' variable json file (containing basic info of software) path will be stored.
jsonfile=os.path.join(os.path.dirname(os.path.realpath(__file__)),'license_keys.json')
with open(jsonfile,'r') as jobj:
    _SOFTWARE_INFO_FILE_PATH=load(jobj)['boot file path']
    
if __name__=='__main__':
    #print(_SOFTWARE_INFO_FILE_PATH)
    pass
    
