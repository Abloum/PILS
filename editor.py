from tkinter import *
from tkinter.filedialog import asksaveasfile
from ivy.std_api import *
from lxml import etree

window = Tk()

entry = Entry
text = Label
background_color = '#e09f3e'  # couleur editeur
button_color = '#335c67'
button_text_color = '#fff3b0'

zoneMode = Frame()
autoOn = Button
autoOff = Button

zoneMove = Frame()
zoneTurn = Frame()

send_forward = Button
send_back = Button
send_left = Button
send_right = Button
fcap = Button

liste = Listbox

zonePen = Frame()
penup = Button
pendown = Button

zoneFunction = Frame()
origin = Button
restore = Button
clear = Button

zoneCoord = Frame()
CoordX = Entry
CoordY = Entry
Goto = Button

zoneRGB = Frame()
colorR = Entry
colorG = Entry
colorB = Entry
fcc = Button

zoneRepBtn = Frame()
RepOn = Button
RepOff = Button

zoneRep = Frame()
NRep = Entry
btn_repet = Button
liste_repet = Listbox

zoneXML = Frame()
saveXML = Button
loadXML = Button
NomFichier = Entry

zoneSuppr = Frame()
Suppr = Button
Vide = Button

saveIMG = Button

leave = Button


class Editor:
    def __init__(self, master):
        self.master = master
        master.title("editor")
        master.geometry("360x720")
        window.minsize(360, 700)
        window.maxsize(360, 700)
        window.config(background=background_color)
        self.var = StringVar()
        self.liste_actions = []
        self.liste_actions_repet = []
        self.start = 0
        self.entry = Entry(window, font=("Helvetica", 12), fg='Black')
        self.text = Label(window, textvariable=self.var, font=("Helvetica", 12))
        self.zoneMove = Frame(window, bg='#777777')
        self.zoneTurn = Frame(window, bg='#777777')

        self.zoneMode = Frame(window, bg=background_color)
        self.autoOff = Button(zoneMode, text="Stop", font=("Helvetica", 12), bg=button_color,
                              fg=button_text_color,
                              command=self.autoOff)
        self.autoOn = Button(zoneMode, text="Reprendre", font=("Helvetica", 12), bg=button_color,
                             fg=button_text_color, state=DISABLED,
                             command=self.autoOn)

        self.send_forward = Button(zoneMove, text="avance", font=("Helvetica", 12), bg=button_color,
                                   fg=button_text_color,
                                   command=self.forward)
        self.send_back = Button(zoneMove, text="recule", font=("Helvetica", 12), bg=button_color,
                                fg=button_text_color,
                                command=self.back)
        self.send_left = Button(zoneTurn, text="tourne a gauche", font=("Helvetica", 12), bg=button_color,
                                fg=button_text_color,
                                command=self.left)
        self.send_right = Button(zoneTurn, text="tourne a droite", font=("Helvetica", 12), bg=button_color,
                                 fg=button_text_color,
                                 command=self.right)
        self.fcap = Button(window, text="fcap", font=("Helvetica", 12), bg=button_color,
                           fg=button_text_color,
                           command=self.fcap)

        self.liste = Listbox(window, bg=background_color, height=5)

        self.zonePen = Frame(window, bg='#777777')
        self.penup = Button(zonePen, text="lever la tortue", font=("Helvetica", 12), bg=button_color,
                            fg=button_text_color,
                            command=self.penup)
        self.pendown = Button(zonePen, text="poser la tortue", font=("Helvetica", 12), bg=button_color,
                              fg=button_text_color,
                              command=self.pendown)

        self.zoneCoord = Frame(window, bg=background_color)
        self.CoordX = Entry(zoneCoord, font=("Helvetica", 12), fg='Black', width=5)
        self.CoordY = Entry(zoneCoord, font=("Helvetica", 12), fg='Black', width=5)
        self.Goto = Button(zoneCoord, text="position", font=("Helvetica", 12), bg=button_color,
                           fg=button_text_color,
                           command=self.fpos)

        self.zoneRGB = Frame(window, bg=background_color)
        self.colorR = Entry(zoneRGB, font=("Helvetica", 12), fg='Black', width=5)
        self.colorG = Entry(zoneRGB, font=("Helvetica", 12), fg='Black', width=5)
        self.colorB = Entry(zoneRGB, font=("Helvetica", 12), fg='Black', width=5)
        self.fcc = Button(zoneRGB, text="Couleur", font=("Helvetica", 12), bg=button_color,
                          fg=button_text_color,
                          command=self.fcc)

        self.zoneFunction = Frame(window, bg='#777777')
        self.origin = Button(zoneFunction, text="origine", font=("Helvetica", 12), bg=button_color,
                             fg=button_text_color,
                             command=self.origin)
        self.restore = Button(zoneFunction, text="restaure", font=("Helvetica", 12), bg=button_color,
                              fg=button_text_color,
                              command=self.restore)
        self.clear = Button(zoneFunction, text="nettoie", font=("Helvetica", 12), bg=button_color,
                            fg=button_text_color,
                            command=self.clear)

        self.zoneRepBtn = Frame(window, bg=background_color)
        self.RepOn = Button(zoneRepBtn, text="on repetition", font=("Helvetica", 12), bg=button_color,
                            fg=button_text_color,
                            command=self.RepTurnOn)
        self.RepOff = Button(zoneRepBtn, text="off repetition", font=("Helvetica", 12), bg=button_color,
                             fg=button_text_color, state=DISABLED,
                             command=self.RepTurnOff)

        self.zoneRep = Frame(window, bg=background_color)
        self.liste_repet = Listbox(zoneRep, bg=background_color, height=5)
        self.NRep = Entry(zoneRep, font=("Helvetica", 12), fg='Black', width=5)
        self.btn_repet = Button(zoneRep, text="Repete ", font=("Helvetica", 12), bg=button_color,
                                fg=button_text_color,
                                command=self.repet)

        self.zoneXML = Frame(window, bg=background_color)
        self.saveXML = Button(zoneXML, text="Enregistre fichier", font=("Helvetica", 12), bg=button_color,
                              fg=button_text_color,
                              command=self.save)
        self.loadXML = Button(zoneXML, text="Charger fichier", font=("Helvetica", 12), bg=button_color,
                              fg=button_text_color,
                              command=self.load)
        self.NomFichier = Entry(window, font=("Helvetica", 12), fg='Black', width=5)

        self.zoneSuppr = Frame(window, bg=background_color)
        self.Suppr = Button(zoneSuppr, text="Supprimer ligne", font=("Helvetica", 12), bg=button_color,
                            fg=button_text_color,
                            command=self.suppr_liste)
        self.Vide = Button(zoneSuppr, text="Vider liste", font=("Helvetica", 12), bg=button_color,
                           fg=button_text_color,
                           command=self.vide)

        self.saveIMG = Button(window, text="Sauvegarder l'image", font=("Helvetica", 20), bg=button_color,
                              fg=button_text_color,
                              command=self.save_img)

        zoneMode.pack(fill=X, padx=10, pady=(10, 0))
        self.entry.pack(pady=(10, 5), padx=(90, 90), fill=X, side=TOP)
        zoneMove.pack(fill=X, padx=10)
        zoneTurn.pack(fill=X, padx=10)
        self.fcap.pack(fill=X, padx=10)
        self.liste.pack(fill=X, pady=3)
        zonePen.pack(fill=X, padx=10)
        zoneCoord.pack(fill=X, padx=10)
        zoneRGB.pack(fill=X, padx=10)
        zoneFunction.pack(fill=X, padx=10)
        zoneRepBtn.pack(fill=X, padx=10, pady=(3, 0))
        zoneRep.pack(fill=X, padx=10, pady=(0, 3))
        self.NomFichier.pack(fill=X, padx=10, pady=(3, 0))
        zoneXML.pack(fill=X, padx=10, pady=(0, 3))
        zoneSuppr.pack(fill=X, padx=10, pady=3)

        self.autoOff.pack(fill=X, ipadx=62, side=LEFT)
        self.autoOn.pack(fill=X, ipadx=50, side=LEFT)

        self.send_forward.pack(fill=X, ipadx=55, side=LEFT)
        self.send_back.pack(fill=X, ipadx=55, side=LEFT)
        self.send_left.pack(fill=X, ipadx=25, side=LEFT)
        self.send_right.pack(fill=X, ipadx=26, side=LEFT)

        self.penup.pack(fill=X, ipadx=34, side=LEFT)
        self.pendown.pack(fill=X, ipadx=30, side=LEFT)

        self.CoordX.pack(fill=X, padx=10, side=LEFT)
        self.CoordY.pack(fill=X, padx=(0, 10), side=LEFT)
        self.Goto.pack(fill=X)

        self.colorR.pack(fill=X, padx=(10, 0), side=LEFT)
        self.colorB.pack(fill=X, padx=10, side=LEFT)
        self.colorG.pack(fill=X, padx=(0, 10), side=LEFT)
        self.fcc.pack(fill=X)

        self.origin.pack(fill=X, ipadx=26, side=LEFT)
        self.restore.pack(fill=X, ipadx=21, side=LEFT)
        self.clear.pack(fill=X, ipadx=26, side=LEFT)

        self.RepOn.pack(fill=X, ipadx=35, side=LEFT)
        self.RepOff.pack(fill=X, ipadx=35, side=LEFT)

        self.NRep.pack(fill=X, pady=10, side=LEFT)
        self.btn_repet.pack(fill=X, pady=10, side=LEFT)
        self.liste_repet.pack(fill=X, side=RIGHT)

        self.text.pack(pady=(0, 5), padx=(90, 90), fill=X)
        self.saveXML.pack(ipadx=20, fill=X, side=LEFT)
        self.loadXML.pack(ipadx=40, fill=X, side=LEFT)

        self.Suppr.pack(ipadx=25, fill=X, side=LEFT)
        self.Vide.pack(ipadx=42, fill=X, side=LEFT)

        self.saveIMG.pack(fill=X, side=BOTTOM)
        IvyInit("Editor")
        IvyStart()

    def forward(self):
        """
        Envoi à la tortue l'ordre d'avancer de la valeur de l'entree principal de la fenetre

        """
        if self.check_int(self.entry.get()):
            self.add_list("forward", self.entry.get())

    def back(self):
        """
        Envoi à la tortue l'ordre de reculer de la valeur de l'entree principal de la fenetre

        """
        if self.check_int(self.entry.get()):
            self.add_list("back", self.entry.get())

    def left(self):
        """
        Envoi à la tortue l'ordre de tourner sur sa gauche de la valeur (en degré) de l'entree principal de la fenetre

        """
        if self.check_int(self.entry.get()):
            self.add_list("left", self.entry.get())

    def right(self):
        """
        Envoi à la tortue l'ordre de tourner sur sa droite de la valeur (en degré) de l'entree principal de la fenetre

        """
        if self.check_int(self.entry.get()):
            self.add_list("right", self.entry.get())

    def fpos(self):
        """
        Envoi à la tortue l'ordre de se deplacer vers la position x y (indiqué par les entry)

        """
        if self.check_coordinates():
            self.add_list("fpos", "(" + self.CoordX.get() + "," + self.CoordY.get() + ")")

    def fcap(self):
        """
        Envoi à la tortue l'ordre de se tourner jusqu'a atteindre l'angle indiqué par la valeure de l'entry principal

        """
        if self.check_int(self.entry.get()):
            self.add_list("fcap", self.entry.get())

    def fcc(self):
        """
        Envoi à la tortue l'ordre de changer de couleur (selon les valeurs rgb des entry)

        """
        if self.check_color():
            self.add_list("fcc", "(" + self.colorR.get() + "," + self.colorG.get() + "," + self.colorB.get() + ")")

    def penup(self):
        """
        Envoi à la tortue l'ordre de se lever

        """
        self.add_list("penup", "0")

    def pendown(self):
        """
        Envoi à la tortue l'ordre de se poser

        """
        self.add_list("pendown", "0")

    def RepTurnOn(self):
        """
        Active le mode repete (à partir d'un click sur ce bouton, les commandes entrés iront dans la liste qui sera répété)

        """
        self.RepOff['state'] = NORMAL
        self.RepOn['state'] = DISABLED

    def RepTurnOff(self):
        """
        Désactive le mode repete (à partir d'un click sur ce bouton, les commandes entrés iront dans la liste de base)

        """
        self.RepOn['state'] = NORMAL
        self.RepOff['state'] = DISABLED

    def autoOn(self):
        """
        Active le mode auto (la tortue bouge si une indication est donnée)

        """
        self.autoOff['state'] = NORMAL
        self.autoOn['state'] = DISABLED
        while (self.start < len(self.liste_actions)):
            move = (str(self.liste_actions[self.start])).split()
            if (move[0] == "repete"):
                nb = int(move[1])
                self.start += 1
                listeTemp = []
                while (move[0] != "fin"):
                    listeTemp.append(str(self.liste_actions[self.start]))
                    self.start += 1
                    move = (str(self.liste_actions[self.start])).split()
                self.lireRep(listeTemp, nb)
            else:
                IvySendMsg("Draw:" + move[0] + " " + move[1])
            self.start += 1

    def autoOff(self):
        """
        Desactive le mode auto (la tortue ne bouge pas même si une indication est donnée)

        """
        self.autoOn['state'] = NORMAL
        self.autoOff['state'] = DISABLED
        self.start = len(self.liste_actions)

    def origin(self):
        """
        Envoi à la tortue l'ordre de retourner au point d'origine

        """
        self.add_list("origin", "0")

    def restore(self):
        """
        Envoi à la tortue l'ordre de restaurer la page

        """
        self.add_list("restore", "0")

    def clear(self):
        """
        Envoi à la tortue l'ordre de nettoyer la page

        """
        self.add_list("clear", "0")

    def save(self):
        """
        Sauvegarde en XML la liste des actions présentes dans l'historique des actions

        """
        if (len(self.NomFichier.get()) > 0):
            self.var.set("")
            i = 0
            ch = "<?xml version='1.0' encoding='UTF-8'?>\n<liste_actions>\n"
            while (i < len(self.liste_actions)):
                move = (str(self.liste_actions[i])).split()
                if move[0] == "repete":
                    ch += "<repeter fois='" + move[1] + "'>\n"
                    while (move[0] != "fin"):
                        ch += self.xmlFileWrite(move)
                        i += 1
                        move = (str(self.liste_actions[i])).split()
                    ch += "</repeter>\n"
                else:
                    ch += self.xmlFileWrite(move)
                i += 1
            ch += "</liste_actions>"
            fichier = open("XML_Save/" + self.NomFichier.get() + ".xml", "w")
            fichier.write(ch)
            fichier.close()
        else:
            self.var.set("veuillez entrer un nom")

    def xmlFileWrite(self, move):
        """
        Passe des données de la liste (en anglais) au format imposé pour la sauvegarde en XML

        """
        if move[0] == "clear":
            return "<nettoyer/>\n"
        elif move[0] == "restore":
            return "<restaurer/>\n"
        elif move[0] == "origin":
            return "<origine/>\n"
        elif move[0] == "pendown":
            return "<lever/>\n"
        elif move[0] == "penup":
            return "<baisser/>\n"
        elif move[0] == "forward":
            return "<avancer dist='" + move[1] + "'/>\n"
        elif move[0] == "back":
            return "<reculer dist='" + move[1] + "'/>\n"
        elif move[0] == "left":
            return "<gauche angle='" + move[1] + "'/>\n"
        elif move[0] == "right":
            return "<droite angle='" + move[1] + "'/>\n"
        elif move[0] == "fcap":
            return "<cap angle='" + move[1] + "'/>\n"
        elif move[0] == "fpos":
            moveTemp = eval(move[1])
            return "<position x='" + str(moveTemp[0]) + "' y='" + str(moveTemp[1]) + "' />\n"
        elif move[0] == "fcc":
            moveTemp = eval(move[1])
            return "<crayon rouge='" + str(moveTemp[0]) + "' vert='" + str(moveTemp[1]) + "' bleu='" + str(
                moveTemp[2]) + "'/>\n"
        else:
            return ""

    def load(self):
        """
        Charge la liste des actions présentes dans le fichier xml recherché dans l'historique des actions

        """
        if (len(self.NomFichier.get()) > 0):
            self.autoOn['state'] = DISABLED
            tree = etree.parse("XML_Save/" + self.NomFichier.get() + ".xml")
            i = 1
            for move in tree.xpath("/liste_actions/*"):
                if str(move).split()[1] == "repeter":
                    self.liste_actions.append("repete " + move.get("fois"))
                    self.liste.insert(END, ("repete", move.get("fois")))
                    for moveRep in tree.xpath("/liste_actions/repeter[position()=" + str(i) + "]/*"):
                        self.FloadXML(moveRep)
                    self.liste_actions.append("fin repete")
                    self.liste.insert(END, ("fin repete"))
                    i += 1
                else:
                    self.FloadXML(move)
            self.autoOn()
        else:
            self.var.set("veuillez entrer un nom")

    def FloadXML(self, move):
        """
        Passe du format imposé pour la sauvegarde en XML aux données de la liste (en anglais)

        """
        if str(move).split()[1] == "avancer":
            self.add_list("forward", move.get("dist"))
        elif str(move).split()[1] == "reculer":
            self.add_list("back", move.get("dist"))
        elif str(move).split()[1] == "droite":
            self.add_list("right", move.get("angle"))
        elif str(move).split()[1] == "gauche":
            self.add_list("left", move.get("angle"))
        elif str(move).split()[1] == "lever":
            self.add_list("penup", "0")
        elif str(move).split()[1] == "baisser":
            self.add_list("pendown", "0")
        elif str(move).split()[1] == "origine":
            self.add_list("origin", "0")
        elif str(move).split()[1] == "restaurer":
            self.add_list("restore", "0")
        elif str(move).split()[1] == "nettoyer":
            self.add_list("clear", "0")
        elif str(move).split()[1] == "crayon":
            self.add_list("fcc", "(" + move.get("rouge") + "," + move.get("vert") + "," + move.get("bleu") + ")")
        elif str(move).split()[1] == "cap":
            self.add_list("fcap", move.get("angle"))
        elif str(move).split()[1] == "position":
            self.add_list("fpos", "(" + move.get("x") + "," + move.get("y") + ")")

    def check_mode_repete(self):
        """
        Vérifie si l'on est en mode repete

        :rtype: Bool
        """
        if (self.RepOff['state'] == NORMAL):
            return True
        return False

    def check_int(self, check):
        """
        Vérifie si l'entrée correspondante est bien un entier

        :param check: entrée à vérifier
        :type check: str
        :rtype: Bool
        """
        try:
            val = int(check)
            self.var.set("")
            return True
        except ValueError:
            self.var.set("veuillez entrer un entier")
            return False

    def check_coordinates(self):
        """
        Vérifie les entrées correspondant aux coordonnées

        :rtype: Bool
        """
        try:
            int(self.CoordX.get())
            int(self.CoordY.get())
            self.var.set("")
            return True
        except ValueError:
            self.var.set("veuillez entrer un entier")
            return False

    def check_color(self):
        """
        Vérifie les entrées correspondant aux couleurs RGB

        :rtype: Bool
        """
        try:
            if (0 <= int(self.colorR.get()) <= 255 and
                    0 <= int(self.colorG.get()) <= 255 and
                    0 <= int(self.colorB.get()) <= 255):
                return True
            else:
                self.var.set("RGB incorrect")
                return False
        except:
            self.var.set("veuillez entrer un triplet RGB")
            return False

    def suppr_liste(self):
        """
        Supprime un élément (de la liste répété et de la liste principale) et redessine

        """
        ListeP = (((str(self.liste.curselection())).replace("(", "")).replace(")", "")).split(",")
        ListeR = (((str(self.liste_repet.curselection())).replace("(", "")).replace(")", "")).split(",")
        for i in range(len(ListeP) - 1):
            testTemp = (str(self.liste_actions[int(ListeP[i])])).split()
            if (testTemp[0] == "repete"):
                self.liste_actions.pop(int(ListeP[i]))
                self.liste.delete(ListeP[i])
                while (testTemp != "fin repete"):
                    self.liste_actions.pop(int(ListeP[i]))
                    self.liste.delete(ListeP[i])
                    testTemp = self.liste_actions[int(ListeP[i])]
                self.liste_actions.pop(int(ListeP[i]))
                self.liste.delete(ListeP[i])
            elif (testTemp[0] == "fin"):
                self.var.set("valeur non supprimable")
            else:
                self.liste_actions.pop(int(ListeP[i]))
                self.liste.delete(ListeP[i])
        for i in range(len(ListeR) - 1):
            self.liste_actions_repet.pop(int(ListeR[i]))
            self.liste_repet.delete(ListeR[i])
        if (len(ListeP) - 1 > 0):
            self.redraw()

    def vide(self):
        """
        Vide la liste que l'on veut vider (en fonction de si le mode repete est activé)

        """
        if self.check_mode_repete():
            while len(self.liste_actions_repet) > 0:
                self.liste_actions_repet.pop(0)
                self.liste_repet.delete(0)
        else:
            while len(self.liste_actions) > 0:
                self.liste_actions.pop(0)
                self.liste.delete(0)

    def add_list(self, move, size):
        """
        Ajoute les ordres qui seront envoyés à la tortue dans la liste correspondante et les envoies si nécéssaire

        """
        if self.check_mode_repete():
            self.liste_actions_repet.append((move + " " + size))
            self.liste_repet.insert(END, (move, size))
        else:
            self.liste_actions.append((move + " " + size))
            self.liste.insert(END, (move, size))
            if (self.autoOn['state'] == DISABLED):
                IvySendMsg("Draw:" + move + " " + size)

    def repet(self):
        """
        Ajoute à la liste principale la commande repete ainsi que ses éléments

        """
        self.RepTurnOff()
        if self.check_int(self.NRep.get()):
            self.liste_actions.append("repete " + self.NRep.get())
            self.liste.insert(END, ("repete", self.NRep.get()))
            listeTemp = []
            for i in range(len(self.liste_actions_repet)):
                listeTemp.append(str(self.liste_actions_repet[i]))
                self.liste_actions.append(str(self.liste_actions_repet[i]))
                self.liste.insert(END, str(self.liste_actions_repet[i]))
            self.liste_actions.append("fin repete")
            self.liste.insert(END, ("fin repete"))
            if (self.autoOn['state'] == DISABLED):
                self.lireRep(listeTemp, int(self.NRep.get()))

    def lireRep(self, liste, nb):
        """
        Lis une liste à répéter et envoi les commandes à la tortue

        """
        for i in range(nb):
            for i in range(len(liste)):
                move = (str(liste[i])).split()
                IvySendMsg("Draw:" + move[0] + " " + move[1])

    def redraw(self):
        """
        Redessine entièrement le dessin (utilisé lors de la suppresion d'un élément de la liste principale)

        """
        IvySendMsg("Draw:" + "restore" + " 0")
        i = 0
        while (i < len(self.liste_actions)):
            move = (str(self.liste_actions[i])).split()
            if (move[0] == "repete"):
                nb = int(move[1])
                i += 1
                listeTemp = []
                while (move[0] != "fin"):
                    listeTemp.append(str(self.liste_actions[i]))
                    i += 1
                    move = (str(self.liste_actions[i])).split()
                self.lireRep(listeTemp, nb)
            else:
                IvySendMsg("Draw:" + move[0] + " " + move[1])
            i += 1

    def save_img(self):
        """
        Envoi une demande de sauvegarde d'image à la tortue

        """
        file_type = [("fichier PNG", "*.png"), ("fichier JPEG", "*.jpg")]
        dialog = asksaveasfile(defaultextension=file_type, filetypes=file_type)
        if dialog is not None:
            IvySendMsg("Draw:" + "save_img " + dialog.name)


Editor(window)
window.mainloop()
