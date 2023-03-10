import tkinter as tk
from tkinter import ttk
import tkinter.font as font

def getLetter(key):
    match key:
        case "ё":
            return "а"
        case "ц":
            return "б"
        case "к":
            return "в"
        case "н":
            return "г"
        case "ш":
            return "д"
        case "з":
            return "е"
        case "ъ":
            return "ё"
        case "ы":
            return "ж"
        case "а":
            return "з"
        case "р":
            return "и"
        case "л":
            return "й"
        case "ж":
            return "к"
        case "я":
            return "л"
        case "с":
            return "м"
        case "и":
            return "н"
        case "ь":
            return "о"
        case "ю":
            return "п"
        case "й":
            return "р"
        case "у":
            return "с"
        case "е":
            return "т"
        case "г":
            return "у"
        case "щ":
            return "ф"
        case "х":
            return "х"
        case "ф":
            return "ц"
        case "в":
            return "ч"
        case "п":
            return "ш"
        case "о":
            return "щ"
        case "д":
            return "ъ"
        case "э":
            return "ы"
        case "ч":
            return "ь"
        case "м":
            return "э"
        case "т":
            return "ю"
        case "б":
            return "я"
    return key

def task1():
    str = lTask['text']
    str = str.lower()
    strRes = ''
    i=0
    print(len(str))
    while i < len(str):
        key = getLetter(str[i])
        strRes = strRes + key
        i = i + 1
    lRes1['text'] = strRes
    return















root = tk.Tk()
root.title("Tab Widget")
tabControl = ttk.Notebook(root)
root.geometry('700x400')
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)
tab4 = ttk.Frame(tabControl)
tab5 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Задание №1')
tabControl.add(tab2, text='Задание №2')
tabControl.add(tab3, text='Задание №3')
tabControl.add(tab4, text='Задание №4')
tabControl.add(tab5, text='Задание №5')
tabControl.pack(expand=1, fill="both")


#task1
lInfo = ttk.Label(tab1,text="Напишите дешифратор для <<ШИФРА ПРОСТОЙ ЗАМЕНЫ>> и расшифруйте предоставленную строку:",font='Times 11')
lTask = ttk.Label(tab1,text="Зуеч уйзшр ирх р еёжёб, уьняёуиь жьеьйьл жёышьсг цгшзе шёиь юь знь кзйз.",font='Times 11')
bTask1 = ttk.Button(tab1, text='Расшифровать', command = task1)
lRes1 = ttk.Label(tab1,text="",font='Times 11')
lInfo.pack()
lTask.pack()
bTask1.pack()
lRes1.pack()


#task2




ttk.Label(tab2,
          text="Lets dive into the\
          world of computers").grid(column=0,
                                    row=0,
                                    padx=30,
                                    pady=30)

root.mainloop()