from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import os
py=sys.executable

root = Tk()
root.title('Dietos skaičiuoklė')
root.geometry("800x600")
root.resizable(width=False, height=False)
background_image=tk.PhotoImage(file='images/running.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

menubar = Menu(root)

def message():
    messagebox.showinfo("Savarankiškas darbas", "Gvidas Rimeikis PS9")

def dieta():
    root.destroy()
    os.system('%s %s' % (py, 'dieta.py'))
def BMI():
    root.destroy()
    os.system('%s %s' % (py, 'bmi.py'))
def pratimai():
    root.destroy()
    os.system('%s %s' % (py, 'pratimai.py'))
    

formules = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Meniu', menu = formules) 
formules.add_command(label ='BMI skaičiuoklė', command = BMI) 
formules.add_command(label ='Dietos skaičiuoklė', command = dieta) 
formules.add_command(label ='Sporto pratimai', command = pratimai)
formules.add_command(label="Išeiti", command=root.quit) 

apie = Menu(menubar, tearoff = 0) 
menubar.add_cascade(label ='Apie', menu = apie) 
apie.add_command(label ='Apie', command = message) 

root.config(menu = menubar)


var = IntVar()
label1 = Label(root, text="Įveskite amžių")
label1.place(x=100, y=100)
age = Entry(root, width=20)
age.place(x=200, y=100)
label2 = Label(root, text="Pasirinkite lytį")
label2.place(x=100, y=150)
r1 = Radiobutton(root, text = "Vyras", variable = var, value = 1)
r1.place(x=200, y=150)
r2 = Radiobutton(root, text = "Moteris", variable = var, value = 2)
r2.place(x=280, y=150)
label3 = Label(root, text="Įveskite ūgį (cm)")
label3.place(x=100, y=200)
cm = Entry(root, width=20)
cm.place(x=200, y=200)
label1 = Label(root, text="Įveskite svorį (kg)")
label1.place(x=100, y=250)
kg = Entry(root, width=20)
kg.place(x=200, y=250)

 
def chosingNumbers():
    global akt, ans
    akt = mynumber.get()
    ans = 1.1
    if (akt == "0-1 kartų į savaitę"):
        ans = 1.1
    elif (akt == "1-3 kartus į savaitę"):
        ans = 1.375
    elif (akt == "3-5 kartus į savaitę"):
        ans = 1.55
    elif (akt == "5-7 kartus į savaitę"):
        ans = 1.725
 
label = ttk.Label(root, text = "Fizinis aktyvumas")
label.grid(column = 0, row = 0)
label.place(x=100, y=300)
 
mynumber = tk.StringVar()
combobox = ttk.Combobox(root, width = 20 , textvariable = mynumber)
combobox['values'] = ("0-1 kartus į savaitę","1-3 kartus į savaitę","3-5 kartus į savaitę","5-7 kartus į savaitę")
combobox.grid(column = 1, row = 0)
combobox.place(x=200, y=300)
 
button = ttk.Button(root, text = "Patvirtinti", command = chosingNumbers)
button.grid(column = 1, row = 1)
button.place(x=345, y=298)

#
def myClick():
    svoris = float(kg.get())
    ugis = float(cm.get())
    metai = float(age.get())
    lytis = float(var.get())
    if (lytis == 1):
        conv = str(((10 * svoris) + (6.25 * ugis) - (5 * metai)) * ans)
    elif (lytis == 2):
        conv = str((655 + (9.6 * svoris) + (1.8 * ugis) - (4.7 * metai)) * ans)
    conv5 = str(round(float(conv),1))
    conv2 = str(round(float(conv) * 0.93,1))
    conv3 = str(round(float(conv) * 0.86,1))
    conv4 = str(round(float(conv) * 0.71,1))
    BMR = "Jums reikia: " + '\n' + conv5 + " kalorijų, kad išlaikyti esamą svorį" + '\n' + conv2 + ", kalorijų, kad numesti 0.25kg per savaitę" + '\n' + conv3 + " kalorijų, kad numesti 0,5kg per savaitę" + '\n' + conv4 + " kalorijų, kad numesti 1 kg per savaitę"
    myLabel = Label(root, text = BMR)
    myLabel.place(x=130, y=400)

btn = Button(root, text = "Apskaičiuoti BMI", command = myClick)
btn.place(x=200, y=350)

root.mainloop()
	