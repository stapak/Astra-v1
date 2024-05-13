import json
import os

os.chdir(os.getcwd()+'\Software_backend')
#print(os.getcwd())
#print(os.listdir())
with open('boot_info.json') as jobj:
    setting=json.load(jobj)

if __name__== '__main__':
    #print(os.listdir())
    #print(os.getcwd())
    #os.chdir(os.getcwd()+'\Software_backend')
    #print(os.getcwd())
    #print(os.listdir())
    for i in setting():
       print(i)