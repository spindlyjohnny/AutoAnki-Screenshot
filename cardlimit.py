import screenshot as ss
import time
limit = int(input("Today's limit:"))
def CardLimit(limit):
    if len(todaycards) > limit:
        ss.invoke('deleteNotes',notes = [todaycards[-1]])
    else:
        return
while True:
    todaycards = ss.invoke('findNotes',query = 'added:1')
    CardLimit(limit)
    if len(todaycards) > limit:
        root = ss.tk.Tk()
        root.withdraw()
        root.wm_attributes("-topmost", 1)
        ss.messagebox.showinfo(title="Limit exceeded", message="Card limit exceeded.", parent=root)
        root.destroy()
        break
    else:
        CardLimit(limit)
        print("No. of cards added: " + str(len(todaycards)) + ", limit = " + str(limit))
        time.sleep(5)
        print("No. of cards added: " + str(len(todaycards)) + ", limit = " + str(limit))