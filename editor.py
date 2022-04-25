from tkinter import *

from ivy.std_api import *

window = Tk()
entry = Entry
text = Label
background_color = '#e09f3e'  # couleur editeur
button_color = '#335c67'
button_text_color = '#fff3b0'
zone2 = Frame()
zone3 = Frame()
send_forward = Button
send_back = Button
send_left = Button
send_right = Button
liste = Listbox
Suppr = Button
saveXML = Button
loadXML = Button
leave = Button


class Editor:
    def __init__(self, master):
        self.master = master
        master.title("editor")
        master.geometry("360x720")
        window.minsize(360, 600)
        window.maxsize(360, 600)
        self.var = StringVar()
        self.liste_actions = []
        self.entry = Entry(window, font=("Helvetica", 12), fg='Black')
        self.text = Label(window, textvariable=self.var, font=("Helvetica", 12))
        self.zone2 = Frame(window, bg='#777777')
        self.zone3 = Frame(window, bg='#777777')
        self.send_forward = Button(zone2, text="avance", font=("Helvetica", 12), bg=button_color,
                                   fg=button_text_color,
                                   command=self.forward)
        self.send_back = Button(zone2, text="recule", font=("Helvetica", 12), bg=button_color,
                                fg=button_text_color,
                                command=self.back)
        self.send_left = Button(zone3, text="tourne a gauche", font=("Helvetica", 12), bg=button_color,
                                fg=button_text_color,
                                command=self.left)
        self.send_right = Button(zone3, text="tourne a droite", font=("Helvetica", 12), bg=button_color,
                                 fg=button_text_color,
                                 command=self.right)
        self.liste = Listbox(window, bg=background_color)
        self.Suppr = Button(window, text="Supprimer ligne", font=("Helvetica", 12), bg=button_color,
                            fg=button_text_color,
                            command=self.suppr_liste)
        self.saveXML = Button(window, text="Enregistre fichier", font=("Helvetica", 12), bg=button_color,
                              fg=button_text_color, command=self.fpos)
        self.loadXML = Button(window, text="Charger fichier", font=("Helvetica", 12), bg=button_color,
                              fg=button_text_color, command=self.fcc)
        self.leave = Button(window, text="Quitter", font=("Helvetica", 20), bg=button_color,
                            fg=button_text_color,
                            command=self.the_end)
        self.entry.pack(pady=(30, 10), padx=(90, 90), fill=X, side=TOP)
        zone2.pack(fill=X, padx=10, pady=10)
        zone3.pack(fill=X, padx=10, pady=10)
        self.send_forward.pack(fill=X, ipadx=55, side=LEFT)
        self.send_back.pack(fill=X, ipadx=55, side=LEFT)
        self.send_left.pack(fill=X, ipadx=25, side=LEFT)
        self.send_right.pack(fill=X, ipadx=25, side=LEFT)
        self.liste.pack(fill=X)
        self.text.pack(pady=(15, 5), padx=(90, 90), fill=X)
        self.saveXML.pack(pady=(1, 5), padx=(90, 90), fill=X)
        self.loadXML.pack(pady=5, padx=(90, 90), fill=X)
        self.Suppr.pack(pady=5, padx=(90, 90), fill=X)
        self.leave.pack(fill=X, side=BOTTOM)
        IvyInit("Editor")
        IvyStart()

    @staticmethod
    def the_end():
        window.destroy()

    def fpos(self):
        if self.check_coordinates():
            self.add_list("fpos", self.entry.get())
            IvySendMsg("Draw:" + "fpos " + self.entry.get())

    def fcap(self):
        if self.check_angle():
            self.add_list("fcap", self.entry.get())
            IvySendMsg("Draw:" + "fcap " + self.entry.get())

    def fcc(self):
        if self.check_color():
            self.add_list("fcc", self.entry.get())
            IvySendMsg("Draw:" + "fcc " + self.entry.get())

    def penup(self):
        self.add_list("penup", "0")
        IvySendMsg("Draw:" + "penup " + "0")

    def pendown(self):
        self.add_list("pendown", "0")
        IvySendMsg("Draw:" + "pendown " + "0")

    def origin(self):
        self.add_list("origin", "0")
        IvySendMsg("Draw:" + "origin " + "0")

    def restore(self):
        IvySendMsg("Draw:" + "restore " + "0")

    def clear(self):
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
            coos = eval(self.entry.get())
            if coos.len != 2:
                return False
            self.var.set("")
            int(coos[0])
            int(coos[1])
            return True
        except:
            self.var.set("veuillez entrer des coordonnées")
            return False

    def check_color(self):
        try:
            coos = eval(self.entry.get())
            if coos.len != 3:
                return False
            self.var.set("")
            0 <= int(coos[0]) <= 255
            0 <= int(coos[1]) <= 255
            0 <= int(coos[2]) <= 255
            return True
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
