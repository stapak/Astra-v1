"""
contains general functions of the backend
"""


from uuid import uuid4 

def ID_generator():
    raw_id=str(uuid4())
    id_sliced=raw_id.split('-')
    id_joined=''.join(id_sliced)
    generated_id=id_joined[0:20]
    return generated_id
    
if __name__=='__main__':
    pass
    
