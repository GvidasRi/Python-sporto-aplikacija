from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
import os
py=sys.executable

root = Tk()
root.title('Pagrindinis')
root.geometry("800x600")
root.resizable(width=False, height=False)
root.canvas = Canvas(width=800, height=600)
root.canvas.pack()
root.photo = PhotoImage(file='images/kauko.png')
root.canvas.create_image(0, 0, image=root.photo, anchor=NW)

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

label2 = Label(root, text="Gvidas Rimeikis. PS9")
label2.place(x=320, y=550)

root.config(menu = menubar)

root.mainloop()
	