from tkinter import *

from ivy.std_api import *

window = Tk()

entry = Entry
text = Label
background_color = '#e09f3e'  # couleur editeur
button_color = '#335c67'
button_text_color = '#fff3b0'

zoneMove = Frame()
zoneTurn = Frame()

send_forward = Button
send_back = Button
send_left = Button
send_right = Button
fcap = Button

liste = Listbox
listeR = Listbox
Suppr = Button

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


repet = Button

saveXML = Button
loadXML = Button
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
        self.entry = Entry(window, font=("Helvetica", 12), fg='Black')
        self.text = Label(window, textvariable=self.var, font=("Helvetica", 12))
        self.zoneMove = Frame(window, bg='#777777')
        self.zoneTurn = Frame(window, bg='#777777')
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
        self.Suppr = Button(window, text="Supprimer ligne", font=("Helvetica", 12), bg=button_color,
                            fg=button_text_color,
                            command=self.suppr_liste)

        self.zonePen = Frame(window, bg='#777777')
        self.penup = Button(zonePen, text="lever la tortue", font=("Helvetica", 12), bg=button_color,
                                   fg=button_text_color,
                                   command=self.penup)
        self.pendown = Button(zonePen, text="poser la tortue", font=("Helvetica", 12), bg=button_color,
                                   fg=button_text_color, state = DISABLED,
                                   command=self.pendown)

        self.zoneCoord = Frame(window, bg=background_color)
        self.CoordX = Entry(zoneCoord, font=("Helvetica", 12), fg='Black', width=5)
        self.CoordY = Entry(zoneCoord, font=("Helvetica", 12), fg='Black', width=5)
        self.Goto = Button(zoneCoord, text="position", font=("Helvetica", 12), bg=button_color,
                                   fg=button_text_color,
                                   command=self.fpos)

        self.repet = Button(window, text="repete", font=("Helvetica", 12), bg=button_color,
                                   fg=button_text_color,
                                   command=self.repet)

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

        self.saveXML = Button(window, text="Enregistre fichier", font=("Helvetica", 12), bg=button_color,
                              fg=button_text_color, command=self.fpos)
        self.loadXML = Button(window, text="Charger fichier", font=("Helvetica", 12), bg=button_color,
                              fg=button_text_color, command=self.fcc)
        self.leave = Button(window, text="Quitter", font=("Helvetica", 20), bg=button_color,
                            fg=button_text_color,
                            command=self.the_end)

        self.entry.pack(pady=(15, 10), padx=(90, 90), fill=X, side=TOP)

        zoneMove.pack(fill=X, padx=10)
        zoneTurn.pack(fill=X, padx=10, pady=3)
        self.fcap.pack(fill=X, padx=10)
        self.liste.pack(fill=X, pady=10)
        zonePen.pack(fill=X, padx=10)
        zoneCoord.pack(fill=X, padx=10, pady=3)
        zoneRGB.pack(fill=X, padx=10, pady=3)
        zoneFunction.pack(fill=X, padx=10, pady=3)

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

        self.repet.pack(fill=X,ipadx=21)

        self.text.pack(pady=(0, 5), padx=(90, 90), fill=X)
        self.saveXML.pack(pady=(1, 5), padx=(90, 90), fill=X)
        self.loadXML.pack(pady=5, padx=(90, 90), fill=X)
        self.Suppr.pack(pady=5, padx=(90, 90), fill=X)
        self.leave.pack(fill=X, side=BOTTOM)
        IvyInit("Editor")
        IvyStart()

    @staticmethod
    def the_end():
        window.destroy()

    def repet(self):
        RepWindows=Toplevel(window)
        RepWindows.title("test")
        RepWindows.geometry("200x200")
        listeR = Listbox(RepWindows, bg=background_color)
        test = Button(RepWindows, text="Supprimer ligne", font=("Helvetica", 12), bg=button_text_color, fg=background_color)
        listeR.pack(fill=X)
        test.pack(fill=X)

    def fpos(self):
        if self.check_coordinates():
            self.add_list("fpos", self.CoordX.get()+" "+self.CoordY.get())
            IvySendMsg("Draw:" + "fpos (" +self.CoordX.get()+","+self.CoordY.get()+")")

    def fcap(self):
        listeR.insert(END, "chibre")
        if self.check_angle():
            self.add_list("fcap", self.entry.get())
            IvySendMsg("Draw:" + "fcap " + self.entry.get())

    def fcc(self):
        if self.check_color():
            self.add_list("fcc", self.colorR.get()+" "+self.colorG.get()+" "+self.colorB.get())
            IvySendMsg("Draw:" + "fcc (" + self.colorR.get()+","+self.colorG.get()+","+self.colorB.get()+")")

    def penup(self):
        self.add_list("penup", "0")
        IvySendMsg("Draw:" + "penup " + "0")
        self.pendown['state'] = NORMAL
        self.penup['state'] = DISABLED

    def pendown(self):
        self.add_list("pendown", "0")
        IvySendMsg("Draw:" + "pendown " + "0")
        self.penup['state'] = NORMAL
        self.pendown['state'] = DISABLED

    def addRep(self):
        self.backNormal['state'] = NORMAL
        self.addRep['state'] = DISABLED

    def backNormal(self):
        self.addRep['state'] = NORMAL
        self.backNormal['state'] = DISABLED

    def origin(self):
        self.add_list("origin", "0")
        IvySendMsg("Draw:" + "origin " + "0")

    def restore(self):
        self.add_list("restore", "0")
        IvySendMsg("Draw:" + "restore " + "0")

    def clear(self):
        self.add_list("clear", "0")
        IvySendMsg("Draw:" + "clear " + "0")

    def check_int(self):
        try:
            val = int(self.entry.get())
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
                return False
        except:
            self.var.set("veuillez entrer un triplet RGB")
            return False

    def suppr_liste(self):
        x = (((str(self.liste.curselection())).replace("(", "")).replace(")", "")).split(",")
        for i in range(len(x) - 1):
            self.liste_actions.pop(int(x[i]))
            self.liste.delete(x[i])
            IvySendMsg("Draw:" + "erase " + x[i])
        IvySendMsg("Draw:" + "redraw " + "0")

    def add_list(self, move, size):
        self.liste_actions.append((move + " " + size))
        self.liste.insert(END, (move, size))

    def forward(self):
        if self.check_int():
            self.add_list("Z", self.entry.get())
            IvySendMsg("Draw:" + "forward " + self.entry.get())

    def back(self):
        if self.check_int():
            self.add_list("S", self.entry.get())
            IvySendMsg("Draw:" + "back " + self.entry.get())

    def left(self):
        if self.check_int():
            self.add_list("Q", self.entry.get())
            IvySendMsg("Draw:" + "left " + self.entry.get())

    def right(self):
        if self.check_int():
            self.add_list("D", self.entry.get())
            IvySendMsg("Draw:" + "right " + self.entry.get())


Editor(window)
window.mainloop()
