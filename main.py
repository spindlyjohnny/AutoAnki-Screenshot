import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import json
import urllib.request
def request(action, **params):
    return {'action': action, 'params': params, 'version': 6}

def invoke(action, **params):
    requestJson = json.dumps(request(action, **params)).encode('utf-8')
    response = json.load(urllib.request.urlopen(urllib.request.Request('http://127.0.0.1:8765', requestJson)))
    if len(response) != 2:
        raise Exception('response has an unexpected number of fields')
    if 'error' not in response:
        raise Exception('response is missing required error field')
    if 'result' not in response:
        raise Exception('response is missing required result field')
    if response['error'] is not None:
        raise Exception(response['error'])
    return response['result']

savedata = {"deck" : "","field" : "","path" : ""}
try:
    data = open("savedata.json")
except:
    savedata["deck"] = input("Which deck to modify?")
    savedata["field"] = input("Which field to modify?")
    print("Where to store media?")
    savedata["path"] = filedialog.askdirectory()
    with open("savedata.json", mode="w", encoding="utf-8") as data:
         json.dump(savedata, data)
if data != None:
    data = open("savedata.json")
    savedata = json.load(data)
    data.close()