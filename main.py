from tkinter import *
import turtle

def the_end():
    Fenetre.destroy()

def checkInt() :
    try:
        val = int(entry.get())
        var.set("")
        return True
    except ValueError:
        var.set("veuillez entrer un entier")
        return False

def rejouerSequence() :
    tortue.reset()
    for i in range(len(liste_actions)) :
        test=(str(liste_actions[i])).split()
        if (test[0]=="Z"):
            tortue.forward(int(test[1]))
        elif (test[0]=="S"):
            tortue.backward(int(test[1]))
        elif (test[0]=="Q"):
            tortue.left(int(test[1]))
        elif (test[0]=="D"):
            tortue.right(int(test[1]))

def supprListe() :
    x = (((str(liste.curselection())).replace("(","")).replace(")","")).split(",")
    for i in range(len(x)-1):
        liste_actions.pop(int(x[i]))
        liste.delete(x[i])
    rejouerSequence()

def AddList(Move, taille) :
    liste_actions.append((Move+" "+taille))
    liste.insert(END, (Move,taille))

def avance():
    if (checkInt()) :
        AddList("Z",entry.get())
        tortue.forward(int(entry.get()))

def recule():
    if (checkInt()):
        AddList("S",entry.get())
        tortue.backward(int(entry.get()))

def tour_gauche():
    if (checkInt()):
        AddList("Q",entry.get())
        tortue.left(int(entry.get()))

def tour_droite():
    if (checkInt()):
        AddList("D",entry.get())
        tortue.right(int(entry.get()))

tortue = turtle.Turtle()
liste_actions = []

couleur_fond = '#e09f3e'  # couleur editeur
couleur_boutons = '#335c67'
couleur_texte_boutons = '#fff3b0'
Action = ""
Fenetre = Tk()
Fenetre.title("Editeur turtle")
Fenetre.geometry("360x720")

Fenetre.minsize(360, 600)  # taille de la fenêtre bloqué a 1080*600
Fenetre.maxsize(360, 600)

Fenetre.config(background=couleur_fond)
zone2 = Frame(Fenetre, bg='#777777')
zone3 = Frame(Fenetre, bg='#777777')

var = StringVar()
entry = Entry(Fenetre, font=("Helvetica", 12), fg='Black')
text = Label(Fenetre, textvariable=var, font=("Helvetica", 12), bg=couleur_fond)
EnvoiForward = Button(zone2, text="avance", font=("Helvetica", 12), bg=couleur_boutons, fg=couleur_texte_boutons, command=avance)
EnvoiBack = Button(zone2, text="recule", font=("Helvetica", 12), bg=couleur_boutons, fg=couleur_texte_boutons, command=recule)
EnvoiLeft = Button(zone3, text="tourne a gauche", font=("Helvetica", 12), bg=couleur_boutons, fg=couleur_texte_boutons, command=tour_gauche)
EnvoiRight = Button(zone3, text="tourne a droite", font=("Helvetica", 12), bg=couleur_boutons, fg=couleur_texte_boutons, command=tour_droite)

liste = Listbox(Fenetre, bg=couleur_fond)
Suppr = Button(Fenetre, text="Supprimer ligne", font=("Helvetica", 12), bg=couleur_boutons, fg=couleur_texte_boutons, command=supprListe)
EnregistreXML = Button(Fenetre, text="Enregistre fichier", font=("Helvetica", 12), bg=couleur_boutons, fg=couleur_texte_boutons)
ChargeXML = Button(Fenetre, text="Charger fichier", font=("Helvetica", 12), bg=couleur_boutons, fg=couleur_texte_boutons)

Quitter = Button(Fenetre, text="Quitter", font=("Helvetica", 20), bg=couleur_boutons, fg=couleur_texte_boutons, command=the_end)

entry.pack(pady=(30,10), padx=(90, 90), fill=X, side=TOP)
zone2.pack(fill=X, padx=10,pady=10)
zone3.pack(fill=X, padx=10,pady=10)
EnvoiForward.pack(fill=X, ipadx=55, side=LEFT)
EnvoiBack.pack(fill=X, ipadx=55, side=LEFT)
EnvoiLeft.pack(fill=X, ipadx=25, side=LEFT)
EnvoiRight.pack(fill=X, ipadx=25, side=LEFT)
text.pack(pady=(5,5), padx=(90, 90), fill=X)
liste.pack(fill=X)

EnregistreXML.pack(pady=(1,5), padx=(90, 90), fill=X)
ChargeXML.pack(pady=5, padx=(90, 90), fill=X)
Suppr.pack(pady=5, padx=(90, 90), fill=X)

Quitter.pack(fill=X, side=BOTTOM)

Fenetre.mainloop()