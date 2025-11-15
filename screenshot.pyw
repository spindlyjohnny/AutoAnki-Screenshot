import json
import urllib.request
import pyperclip
import pyautogui
import random
import string
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

def getfields(ID):
    if(type(ID) != int) or ID not in yomitanIDs:
        return
    else:
        index = yomitanIDs.index(ID)
        return invoke("notesInfo",notes = yomitanIDs)[index]['fields']
savedata = {"deck" : "","field" : "","path" : ""}
try:
    data = open("savedata.json")
except:
    savedata["deck"] = input("Which deck to modify?")
    savedata["field"] = input("Which field to modify?")
    savedata["path"] = input("Where to store screenshots?")
    with open("savedata.json", mode="w", encoding="utf-8") as data:
         json.dump(savedata, data)
if data != None:
    data = open("savedata.json")
    savedata = json.load(data)
    data.close()
yomitanIDs = invoke('findNotes',query = "deck:"+ savedata["deck"])
#sentencequery = invoke('findNotes',query = 'sentence:*' + pyperclip.paste() + "*")
wordquery = invoke('findNotes',query = 'word:*' + pyperclip.paste() + "*")
def AutoScreenshot():
    if len(wordquery) > 0:
        fields = getfields(wordquery[0])#['Picture']
        if fields == None:
            return
        else:
            #haspic = fields['Picture']
            haspic = fields[savedata['field']]
            if haspic['value'] != '':
                return
            else:
                filename = "".join(random.choices(string.ascii_uppercase + string.digits, k=16)) + ".png"
                path = rf"C:\Users\saifu\AppData\Roaming\Anki2\User 1\collection.media\{filename}"
                #path = savedata['path'] + filename
                pyautogui.screenshot(path)
                invoke("storeMediaFile",filename = filename,path = path)
                invoke("updateNoteFields", note={
                    "id": wordquery[0],
                    "fields": {
                    "Picture": f'<img src="{filename}">'
                    }
                })
    else:
        return
AutoScreenshot()