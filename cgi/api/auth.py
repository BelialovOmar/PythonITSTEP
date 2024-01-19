#!C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\python.exe
import json
import os

def query_params() :
    qs = os.environ['QUERY_STRING']
    return { k: v for k, v in 
    ( pair.split('=', 1) for pair in 
        qs.split('&') ) } if len(qs) > 0 else { }

print ("Connect-Type: application/json")
print ("Connection: close")
print ()
print('"WORKS!"')
print( json.dumps( query_params()))
