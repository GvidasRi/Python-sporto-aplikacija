from tkinter import *
from PIL import ImageTk,Image
from time import strftime
from tkinter import messagebox
import os
py=sys.executable

root = Tk()
root.title('Kūno masės indekso skaičiuoklė')
root.geometry("800x600")
root.resizable(width=False, height=False)
root.canvas = Canvas(width=800, height=600)
root.canvas.pack()
root.photo = PhotoImage(file='images/KMI.png')
root.canvas.create_image(125, 20, image=root.photo, anchor=NW)

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

label1 = Label(root, text="Įveskite svorį (kg)")
label1.place(x=160, y=380)
kg = Entry(root, width=50)
kg.place(x=270, y=380)
label2 = Label(root, text="Įveskite ūgį (cm)")
label2.place(x=160, y=430)
cm = Entry(root, width=50)
cm.place(x=270, y=430)

def myClick():
    svoris = float(kg.get())
    ugis = float(cm.get())
    conv = str(round(svoris*10000 / (ugis * ugis),1))
    bmi = "Jūsų BMI: " + conv
    myLabel = Label(root, text = bmi)
    myLabel.place(x=365, y=520)

btn = Button(root, text = "Apskaičiuoti BMI", command = myClick)
btn.place(x=360, y=480)

root.mainloop()
	