from tkinter import *
import random
from tkinter.messagebox import*

score_ordinateur = 0
score_utilisateur = 0
score = str(score_utilisateur) + ' - ' + str(score_ordinateur)
resume = ''
print(score)

# Cette fonction se lance dès que le joueur appuie sur le bouton ciseaux
def ciseaux():
    # On recupere les variables de manière globale afin qu'elles soient modifier en dehors de la fonction
    global score_ordinateur
    global score_utilisateur
    global score
    global resume

    # On genere le coup  de l'ordinateur par un randint
    ordinateur_coup= random.randint(1,3)
    pierre = 1 #pierre prends la valeur 1
    feuille = 2 #feuille prends la valeur 2
    ciseaux = 3 #ciseaux prends la valeur 3

    #On compare le coup du joueur à l'ordinateur
    if(ordinateur_coup==pierre):
        score_ordinateur = score_ordinateur +1
        print("L'ordinateur a joue pierre, vous perdez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        resume ='L"ordinateur a joue pierre, vous perdez cette manche'
    elif(ordinateur_coup==ciseaux):
        print("L'ordinateur a joue ciseaux, egalite sur cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        resume='L"ordinateur a joue ciseaux, egalite sur cette manche'
    elif(ordinateur_coup==feuille):
        score_utilisateur= score_utilisateur + 1
        print("L'ordinateur a joue feuille, vous remportez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        resume = 'L"ordinateur a joue feuille, vous remportez cette manche'
    score = str(score_utilisateur) + ' - ' + str(score_ordinateur)
    Resume.config(text=resume)
    Score.config(text=score)   
    resultat()

# Cette fonction se lance dès que le joueur appuie sur le bouton pierre
def pierre():
    global score_utilisateur
    global score_ordinateur
    global score
    global resume
    ordinateur_coup= random.randint(1,3)
    pierre = 1 #pierre prends la valeur 1
    feuille = 2 #feuille prends la valeur 2
    ciseaux = 3 #ciseaux prends la valeur 3
    if(ordinateur_coup==pierre):
        print("L'ordinateur a joue pierre, egalite sur cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        resume= 'L"ordinateur a joue pierre, egalite sur cette manche'
    elif(ordinateur_coup==ciseaux):
        score_utilisateur = score_utilisateur+1
        print("L'ordinateur a joue ciseaux, vous gagnez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        resume= 'L"ordinateur a joue ciseaux, vous gagnez cette manche'
    elif(ordinateur_coup==feuille):
        score_ordinateur= score_ordinateur + 1
        print("L'ordinateur a joue feuille, vous perdez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        resume= 'L"ordinateur a joue feuille, vous perdez cette manche'
    score = str(score_utilisateur) + ' - ' + str(score_ordinateur)
    Resume.config(text=resume)
    Score.config(text=score)
    resultat()

# Cette fonction se lance dès que le joueur appuie sur le bouton feuille
def feuille():
    global score_utilisateur
    global score_ordinateur
    global score
    global resume
    ordinateur_coup= random.randint(1,3)
    pierre = 1 #pierre prends la valeur 1
    feuille = 2 #feuille prends la valeur 2
    ciseaux = 3 #ciseaux prends la valeur 3
    if ordinateur_coup == ciseaux:
        score_ordinateur= score_ordinateur + 1
        print("L'ordinateur a joue ciseaux, vos perdez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        resume='L"ordinateur a joue ciseaux, vous perdez  cette manche'
    elif ordinateur_coup ==pierre:
        score_utilisateur = score_utilisateur +1

        print("L'ordinateur a joue pierre, vous remportez cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        resume='L"ordinateur a joue pierre, vous remportez cette manche'
    elif ordinateur_coup == feuille:
        print("L'ordinateur a joue feuille, egalite sur cette manche le score est donc de :", score_utilisateur," - ", score_ordinateur)
        resume='L"ordinateur a joue feuille, egalite sur cette manche'

    score = str(score_utilisateur) + ' - ' + str(score_ordinateur)
    #On modifie le labec Resume par la valeur de la variable resume
    Resume.config(text=resume)
    #Modifie le label Score par la valeur score
    Score.config(text=score)
    resultat()

#Fonction qui verifie si un des deux joueurs à 2 points
def resultat():
    global score_ordinateur
    global score_utilisateur
    global score
    global resume
    ordinateur_coup= random.randint(1,3)
    pierre = 1 #pierre prends la valeur 1
    feuille = 2 #feuille prends la valeur 2
    ciseaux = 3 #ciseaux prends la valeur 3

    if score_utilisateur == 2:
        print("Bravo vous avez remportez le pierre, feuille, ciseaux !")
        Resume.config(text='Bravo vous avez remportez le pierre, feuille, ciseaux !')
        retry()
    elif score_ordinateur == 2:
        print("Dommage...Vous avez perdu :( ")
        Resume.config(text='Dommage...Vous avez perdu :(')
        retry()


def retry(): #Fonction pour recommencer lorsque que l'on perd ou gagne
    if askyesno('Ordinateur', 'Voulez vous recommencer?'):
        global score_ordinateur
        global score_utilisateur
        score_ordinateur=0
        score_utilisateur=0
        score = str(score_utilisateur) + ' - ' + str(score_ordinateur)
        Score.config(text=score)
        Resume.config(text='')
    else:
        showinfo('Ordinateur', 'Dommage...')
        Mafenetre.destroy()

#On créer la fenetre du projet
Mafenetre = Tk()
#On lui donne un titre
Mafenetre.title('Pierre Feuille ciseaux')
#Importation des images
feuilleimg= PhotoImage(file='papier.gif')
pierreimg= PhotoImage(file='pierre.gif')
ciseauximg= PhotoImage(file='ciseaux.gif')
#Le label qui affiche le score
Score = Label(Mafenetre,text=score, bg = "white")
Score.pack()
#Celui qui affiche les dialogues
Resume = Label(Mafenetre, bg = "white")
Resume.pack()

# Score = Label(Mafenetre,  text="-", bg = "white")
# Score.place(x=20, y=20)
# Score.pack()
# ScoreOrdi = Label(Mafenetre, text=score_ordinateur, bg = "white")
# ScoreOrdi.place(x=20, y=25)
# ScoreOrdi.pack()


#Button pierre
Pierre = Button(Mafenetre, text ='Pierre', command=pierre)
Pierre.configure(image=pierreimg)
Pierre.pack(side = LEFT, padx = 50, pady = 50)

#Button feuille
Feuille = Button(Mafenetre, text ='Feuille', command=feuille)
Feuille.configure(image=feuilleimg)
Feuille.pack(side = LEFT, padx = 50, pady = 50)

#Buton ciseaux
Ciseaux = Button(Mafenetre, text ='Ciseaux', command =ciseaux)
Ciseaux.configure(image=ciseauximg)
Ciseaux.pack(side = LEFT, padx = 50, pady = 50)





Mafenetre.mainloop()