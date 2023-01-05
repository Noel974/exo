from tkinter import *
import random

#fenetre
root = Tk()
root.geometry(400*400)
root.resizable(0,0)
root.title('Pierre feuille Ciseaux')
root.config(bg ="sheashell3")

#heading
Label(root, text="pierre, feuille, ciseaux", font="arial 20 bold", bg ="sheashell2").pack()

#user
