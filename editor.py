from tkinter import *
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
                                   fg=button_text_color, state = DISABLED,
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
                                   fg=button_text_color, state = DISABLED,
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

        self.leave = Button(window, text="Quitter", font=("Helvetica", 20), bg=button_color,
                            fg=button_text_color,
                            command=self.the_end)

        zoneMode.pack(fill=X, padx=10, pady=(10,0))
        self.entry.pack(pady=(10, 5), padx=(90, 90), fill=X, side=TOP)
        zoneMove.pack(fill=X, padx=10)
        zoneTurn.pack(fill=X, padx=10)
        self.fcap.pack(fill=X, padx=10)
        self.liste.pack(fill=X, pady=3)
        zonePen.pack(fill=X, padx=10)
        zoneCoord.pack(fill=X, padx=10)
        zoneRGB.pack(fill=X, padx=10)
        zoneFunction.pack(fill=X, padx=10)
        zoneRepBtn.pack(fill=X, padx=10, pady=(3,0))
        zoneRep.pack(fill=X, padx=10, pady=(0,3))
        self.NomFichier.pack(fill=X,padx=10, pady=(3,0))
        zoneXML.pack(fill=X, padx=10, pady=(0,3))
        zoneSuppr.pack(fill=X, padx=10, pady=3)

        self.autoOff.pack(fill=X,ipadx=62, side=LEFT)
        self.autoOn.pack(fill=X,ipadx=50, side=LEFT)

        self.send_forward.pack(fill=X, ipadx=55, side=LEFT)
        self.send_back.pack(fill=X, ipadx=55, side=LEFT)
        self.send_left.pack(fill=X, ipadx=25, side=LEFT)
        self.send_right.pack(fill=X, ipadx=26, side=LEFT)

        self.penup.pack(fill=X,ipadx=34, side=LEFT)
        self.pendown.pack(fill=X,ipadx=30, side=LEFT)

        self.CoordX.pack(fill=X, padx=10, side=LEFT)
        self.CoordY.pack(fill=X, padx=(0,10), side=LEFT)
        self.Goto.pack(fill=X)

        self.colorR.pack(fill=X, padx=(10,0), side=LEFT)
        self.colorB.pack(fill=X, padx=10, side=LEFT)
        self.colorG.pack(fill=X, padx=(0,10), side=LEFT)
        self.fcc.pack(fill=X)

        self.origin.pack(fill=X,ipadx=26, side=LEFT)
        self.restore.pack(fill=X,ipadx=21, side=LEFT)
        self.clear.pack(fill=X,ipadx=26, side=LEFT)

        self.RepOn.pack(fill=X,ipadx=35, side=LEFT)
        self.RepOff.pack(fill=X,ipadx=35, side=LEFT)

        self.NRep.pack(fill=X, pady=10, side=LEFT)
        self.btn_repet.pack(fill=X, pady=10, side=LEFT)
        self.liste_repet.pack(fill=X, side=RIGHT)

        self.text.pack(pady=(0, 5), padx=(90, 90), fill=X)
        self.saveXML.pack(ipadx=20, fill=X, side=LEFT)
        self.loadXML.pack(ipadx=40, fill=X, side=LEFT)

        self.Suppr.pack(ipadx=25, fill=X, side=LEFT)
        self.Vide.pack(ipadx=42, fill=X, side=LEFT)
        self.leave.pack(fill=X, side=BOTTOM)
        IvyInit("Editor")
        IvyStart()

    @staticmethod
    def the_end():
        window.destroy()

    def forward(self):
        if self.check_int(self.entry.get()):
            self.add_list("forward", self.entry.get())

    def back(self):
        if self.check_int(self.entry.get()):
            self.add_list("back", self.entry.get())

    def left(self):
        if self.check_int(self.entry.get()):
            self.add_list("left", self.entry.get())

    def right(self):
        if self.check_int(self.entry.get()):
            self.add_list("right", self.entry.get())

    def fpos(self):
        if self.check_coordinates():
            self.add_list("fpos", "("+self.CoordX.get()+","+self.CoordY.get()+")")

    def fcap(self):
        if self.check_int(self.entry.get()):
            self.add_list("fcap", self.entry.get())

    def fcc(self):
        if self.check_color():
            self.add_list("fcc", "("+self.colorR.get()+","+self.colorG.get()+","+self.colorB.get()+")")

    def penup(self):
        self.add_list("penup", "0")

    def pendown(self):
        self.add_list("pendown", "0")

    def RepTurnOn(self):
        self.RepOff['state'] = NORMAL
        self.RepOn['state'] = DISABLED

    def RepTurnOff(self):
        self.RepOn['state'] = NORMAL
        self.RepOff['state'] = DISABLED

    def autoOn(self):
        self.autoOff['state'] = NORMAL
        self.autoOn['state'] = DISABLED
        for i in range(self.start, len(self.liste_actions)):
            move = (str(self.liste_actions[i])).split()
            if move[0] == "clear" or move[0] == "restore" or move[0] == "origin" or move[0] == "pendown" or move[0] == "penup":
                IvySendMsg("Draw:" + move[0] +" 0")
            elif move[0] == "fpos":
                IvySendMsg("Draw:fpos" + "(" + move[1] + "," + move[2])
            elif move[0] == "fcc":
                IvySendMsg("Draw:fcc" + "(" + move[1] + "," + move[2] + "," + move[3] + ")")
            else:
                IvySendMsg("Draw:" + move[0] +" "+move[1])

    def autoOff(self):
        self.autoOn['state'] = NORMAL
        self.autoOff['state'] = DISABLED
        self.start = len(self.liste_actions)

    def origin(self):
        self.add_list("origin", "0")

    def restore(self):
        self.add_list("restore", "0")

    def clear(self):
        self.add_list("clear", "0")

    def save(self):
        if (len(self.NomFichier.get())>0):
            ch = "<?xml version='1.0' encoding='UTF-8'?>\n<liste_actions>\n"
            if(self.check_mode_repete()):
                for i in range(len(self.liste_actions_repet)):
                    move = (str(self.liste_actions_repet[i])).split()
                    if move[0] == "clear" or move[0] == "restore" or move[0] == "origin" or move[0] == "pendown" or move[0] == "penup":
                        ch += "<action move='"+move[0]+"'/>\n"
                    elif move[0] == "fpos":
                        ch += "<action move='fpos' value1='"+move[1]+"' value2='"+move[2]+"' />\n"
                    elif move[0] == "fcc":
                        ch += "<action move='fpos' value1='"+move[1]+"' value2='"+move[2]+"' value3='"+move[3]+"'/>\n"
                    else:
                        ch += "<action move='"+move[0]+"' value='"+move[1]+"' />\n"
            else:
                for i in range(len(self.liste_actions)):
                    move = (str(self.liste_actions[i])).split()
                    if move[0] == "clear" or move[0] == "restore" or move[0] == "origin" or move[0] == "pendown" or move[0] == "penup":
                        ch += "<action move='"+move[0]+"'/>\n"
                    elif move[0] == "fpos":
                        moveTemp = move[1].replace("(","").replace(")","").split(",")
                        ch += "<action move='fpos' value1='"+moveTemp[0]+"' value2='"+moveTemp[1]+"' />\n"
                    elif move[0] == "fcc":
                        moveTemp = move[1].replace("(","").replace(")","").split(",")
                        ch += "<action move='fcc' value1='"+moveTemp[0]+"' value2='"+moveTemp[1]+"' value3='"+moveTemp[2]+"'/>\n"
                    else:
                        ch += "<action move='"+move[0]+"' value='"+move[1]+"' />\n"
            ch += "</liste_actions>"
            fichier = open("XML_Save/"+self.NomFichier.get()+".xml", "w")
            fichier.write(ch)
            fichier.close()
        else :
            self.var.set("veuillez entrer un nom")

    def load(self):
        if (len(self.NomFichier.get())>0):
            tree = etree.parse("XML_Save/"+self.NomFichier.get()+".xml")
            for move in tree.xpath("/liste_actions/action"):
                if str(move.get("move")) == "clear" or str(move.get("move")) == "restore" or str(move.get("move")) == "origin" or str(move.get("move")) == "pendown" or str(move.get("move")) == "penup":
                    self.add_list(str(move.get("move")), "0")
                elif move.get("move") == "fpos":
                    self.add_list("fpos", "(" + str(move.get("value1")) + "," + str(move.get("value2"))+")")
                elif move.get("move") == "fcc":
                    self.add_list("fcc", "(" + str(move.get("value1")) + "," + str(move.get("value2")) + "," + str(move.get("value3")) + ")")
                else:
                    self.add_list(str(move.get("move")), str(move.get("value")))
        else :
            self.var.set("veuillez entrer un nom")

    def check_mode_repete(self):
        if (self.RepOff['state'] == NORMAL ) :
            return True
        return False

    def check_int(self, check):
        try:
            val = int(check)
            self.var.set("")
            return True
        except ValueError:
            self.var.set("veuillez entrer un entier")
            return False

    def check_angle(self):
        try:
            val = float(self.entry.get())
            self.var.set("")
            return True
        except:
            self.var.set("veuillez entrer un angle")
            return False

    def check_coordinates(self):
        try:
            int(self.CoordX.get())
            int(self.CoordY.get())
            self.var.set("")
            return True
        except ValueError:
            self.var.set("veuillez entrer un entier")
            return False

    def check_color(self):
        try:
            if (0 <= int(self.colorR.get()) <= 255 and
                0 <= int(self.colorG.get()) <= 255 and
                0 <= int(self.colorB.get()) <= 255) :
                return True
            else :
                self.var.set("RGB incorrect")
                return False
        except:
            self.var.set("veuillez entrer un triplet RGB")
            return False

    def suppr_liste(self):
        ListeP = (((str(self.liste.curselection())).replace("(", "")).replace(")", "")).split(",")
        ListeR = (((str(self.liste_repet.curselection())).replace("(", "")).replace(")", "")).split(",")
        for i in range(len(ListeP) - 1):
            self.liste_actions.pop(int(ListeP[i]))
            self.liste.delete(ListeP[i])
            IvySendMsg("Draw:" + "erase " + ListeP[i])
        for i in range(len(ListeR) - 1):
            self.liste_actions_repet.pop(int(ListeR[i]))
            self.liste_repet.delete(ListeR[i])
        if (len(ListeP)-1>0):
            IvySendMsg("Draw:" + "redraw " + "0")

    def vide(self):
        if self.check_mode_repete():
            while len(self.liste_actions_repet)>0:
                self.liste_actions_repet.pop(0)
                self.liste_repet.delete(0)
        else:
            while len(self.liste_actions)>0:
                self.liste_actions.pop(0)
                self.liste.delete(0)

    def add_list(self, move, size):
        if self.check_mode_repete():
            self.liste_actions_repet.append((move + " " + size))
            self.liste_repet.insert(END, (move, size))
        else :
            self.liste_actions.append((move + " " + size))
            self.liste.insert(END, (move, size))
            if (self.autoOn['state'] == DISABLED) :
                IvySendMsg("Draw:" + move +" "+ size)

    def repet(self):
        self.RepTurnOff()
        if self.check_int(self.NRep.get()):
            for i in range(int(self.NRep.get())):
                for i in range(len(self.liste_actions_repet)):
                    move = (str(self.liste_actions_repet[i])).split()
                    if move[0] == "clear" or move[0] == "restore" or move[0] == "origin" or move[0] == "pendown" or move[0] == "penup":
                        self.add_list(move[0], "0")
                    elif move[0] == "fpos":
                        moveTemp = move[1].replace("(","").replace(")","").split(",")
                        self.add_list("fpos", "("+moveTemp[0]+","+moveTemp[1]+")")
                    elif move[0] == "fcc":
                        moveTemp = move[1].replace("(","").replace(")","").split(",")
                        self.add_list("fcc", "(" + moveTemp[0] + "," + moveTemp[1] + "," + moveTemp[2] + ")")
                    else:
                        self.add_list(move[0], move[1])

Editor(window)
window.mainloop()
