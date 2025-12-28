!p::Run "C:\Users\saifu\OneDrive\Desktop\AutoAnki Screenshot\cardlimit.py"
^p::{
    Run "C:\Users\saifu\OneDrive\\Desktop\AutoAnki Screenshot\screenshot.pyw"
    if !FileExist("C:\Users\saifu\OneDrive\Desktop\AutoAnki Screenshot\savedata.json")
        Run "C:\Users\saifu\OneDrive\\Desktop\AutoAnki Screenshot\main.py"
    return
}
^+a::{
    Run "C:\Users\saifu\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\YomiNinja.lnk" 
    Run "C:\Users\saifu\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Anki.lnk"
    return
}
