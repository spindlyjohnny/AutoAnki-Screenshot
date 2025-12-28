import pyperclip
import pyautogui
import random
import string
import main as sv
def getfields(ID):
    if(type(ID) != int) or ID not in yomitanIDs:
        return
    else:
        index = yomitanIDs.index(ID)
        return sv.invoke("notesInfo",notes = yomitanIDs)[index]['fields']
yomitanIDs = sv.invoke('findNotes',query = "deck:"+ sv.savedata["deck"])
#sentencequery = invoke('findNotes',query = 'sentence:*' + pyperclip.paste() + "*")
if type(pyperclip.paste()) == str:    
    if pyperclip.paste() != "" and len(sv.invoke('findNotes',query = 'word:*' + pyperclip.paste() + "*")) > 0:
        wordquery = sv.invoke('findNotes',query = 'word:*' + pyperclip.paste() + "*")[0]
    elif pyperclip.paste() == "" and len(sv.invoke("findNotes",query = "added:1")) > 0:
        wordquery = sv.invoke("findNotes",query = "added:1")[-1]
else:
    wordquery = None
#wordquery = invoke("findNotes",query = "added:1")[-1] if len(invoke("findNotes",query = "added:1")) > 0 else None#invoke('findNotes',query = 'word:*' + pyperclip.paste() + "*")
def AutoScreenshot():
    if wordquery != None:
        fields = getfields(wordquery)#['Picture']
        if fields == None:
            return
        else:
            #haspic = fields['Picture']
            haspic = fields[sv.savedata['field']]
            if haspic['value'] != '':
                return
            else:
                filename = "".join(random.choices(string.ascii_uppercase + string.digits, k=16)) + ".png"
                #path = rf"C:\Users\saifu\AppData\Roaming\Anki2\User 1\collection.media\{filename}"
                path = sv.savedata['path'] + "/" + filename
                pyautogui.screenshot(path)
                sv.invoke("storeMediaFile",filename = filename,path = path)
                sv.invoke("updateNoteFields", note={
                    "id": wordquery,
                    "fields": {
                    "Picture": f'<img src="{filename}">'
                    }
                })
                if pyperclip.paste() != "":
                    pyperclip.copy("")
    else:
        return
AutoScreenshot()