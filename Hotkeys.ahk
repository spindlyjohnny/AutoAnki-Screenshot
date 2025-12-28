!p::Run "cardlimit.py"
^p::{
    Run "screenshot.pyw"
    if !FileExist("savedata.json")
        Run "main.py"
    return
}
^+a::{
    Run "C:\Users\saifu\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\YomiNinja.lnk" 
    Run "C:\Users\saifu\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anki.lnk"
    return
}
