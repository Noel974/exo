
from tkinter import *
import random


#La fenêtre
root = Tk()
root.geometry('400x400')
root.resizable(0,0)
root.title('Pierre Papier Ciseaux')
root.config(bg ='RED')

#Titre
Label(root, text="Pierre, Papier, Ciseaux", font="arial 20 bold",).pack()

#Fonction du joueur
user_take = StringVar()
Label(root,text="choisir entre: Pierre, Papier, Ciseaux", font="arial 15 bold", bg="seashell2").place(x =20,y=70)
Entry(root, font="arial 15", textvariable=user_take, bg="antiquewhite2").place(x=90,y=130)

#Fonction de l'Ia 
comp_pick = random.randint(1,3)
if comp_pick == 1:
    comp_pick="Pierre"
elif comp_pick ==2:
    comp_pick="Papier"
else:
    comp_pick="Ciseaux"

#FFonction du jeux 
Result = StringVar()

def play():
      user_pick = user_take.get()
      if user_pick == comp_pick:
         Result.set('vous sélectionnez tous les deux le même')
      elif user_pick =='Pierre' and comp_pick =='Papier':
         Result.set('Vous avez perdu, Ia a selectienner Papier')
      elif user_pick =='Pierre' and comp_pick =='Ciseaux':
         Result.set('Vous avez gagné, Ia a selectienner Ciseaux')
      elif user_pick =='Papier' and comp_pick =='Ciseaux':
         Result.set('Vous avez perdu, Ia a selectienner Ciseaux')
      elif user_pick =='Papier' and comp_pick =='Pierre':
         Result.set('Vous avez gagné, Ia a selectienner Pierre')
      elif user_pick =='Ciseaux' and comp_pick =='Pierre':
         Result.set('Vous avez perdu, Ia a selectienner Pierre')
      elif user_pick =='Ciseaux' and comp_pick =='Papier':
         Result.set('Vous avez gagné, Ia a selectienner Papier')
      else:
         Result.set('invalide : choisissez -- Pierre, Papier, Ciseaux')


# Fonction de réinitialiser
def Reset():
    Result.set("")
    user_take.set("")

#Fonction pour sortir
def Exit():
    root.destroy()

#Les boutons
Entry(root, font ='arial 10 bold', textvariable= Result, bg ='antiquewhite2', width= 50,).place(x=25, y=250)

Button(root, font='arial 10 bold', text = 'Play', padx= 5,bg ='seashell4', command=play).place(x=150, y=190)
Button(root, font='arial 10 bold', text = 'Reset', padx= 5,bg ='seashell4', command=Reset).place(x=70, y=310)
Button(root, font='arial 10 bold', text = 'Exit', padx= 5,bg ='seashell4', command=Exit).place(x=230, y=310)


root.mainloop()