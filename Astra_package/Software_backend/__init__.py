"""
contains general functions of the backend.

"""


from uuid import uuid4 

def ID_generator():
    raw_id=str(uuid4())
    id_sliced=raw_id.split('-')
    id_joined=''.join(id_sliced)
    generated_id=id_joined[0:20]
    return generated_id


# Inside '_SOFTWARE_INFO_FILE_PATH' variable json file (containing basic info of software) path will be stored.
_SOFTWARE_INFO_FILE_PATH=None

    
if __name__=='__main__':
    pass
    
