import queue
import turtle
from tkinter import Tk, Canvas
from PIL import Image

from ivy.std_api import *

window = Tk()


class Visualizer:

    def read_msg(self, *arg):
        """
        Lis le message recu
        """
        print(str(arg[0]) + " a envoyé : " + arg[1])
        self.queue.put(arg[1])

    def __init__(self, master):
        self.master = master
        master.title("Visualizer")
        master.geometry("600x600")
        master.configure(bg="#FFFFFF")
        self.list_actions = []
        self.canvas = Canvas(
            master,
            bg="#FFFFFF",
            height=600,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.canvas.place(x=0, y=0)
        self.screen = turtle.TurtleScreen(self.canvas)
        self.turtle = turtle.RawTurtle(self.screen, shape="turtle")
        self.turtle.screen.colormode(255)

        IvyInit("Visualizer")
        IvyStart()
        IvyBindMsg(self.read_msg, "Draw:(.*)")
        self.queue = queue.Queue()
        self.running = 1
        self.loop()

    def loop(self):
        """
        Vérifie s'il y a de nouvelle indication toutes les 100ms
        """
        while not self.queue.empty():
            current = self.queue.get()
            tab = current.split()
            print(tab)

            func = getattr(Visualizer, tab[0])
            func(self, tab[1])
            if (tab[0] != "redraw") & (tab[0] != "erase"):
                self.list_actions.append(tab)

        if not self.running:
            import sys
            sys.exit(1)
        self.master.after(100, self.loop)

    def save_img(self, filename):
        """
        Tourne la tortue sur sa gauche.

        :param filename: nom du fichier
        :type filename: str
        """
        self.canvas.postscript(file='tmp_img' + '.eps')
        img = Image.open('tmp_img' + '.eps')
        img.save(filename, 'png')

    def redraw(self, any):
        """
        Redessine selon la liste active
        """
        self.turtle.reset()
        tmp = self.list_actions
        self.list_actions = []
        for i in range(len(tmp)):
            self.queue.put(str(tmp[i][0]) + " " + str(tmp[i][1]))

    def fcc(self, rgb):
        """
        Change la couleur du trait tracé par la tortue.

        :param rgb: couleur rgb
        :type rgb: str
        """
        print(eval(rgb))
        self.turtle.pencolor(eval(rgb))

    def erase(self, index):
        """
        Efface le parcours de la tortue.
        """
        self.list_actions.pop(int(index))

    def penup(self, any):
        """
        Lève la tortue.
        """
        self.turtle.penup()

    def pendown(self, any):
        """
        Pose la tortue
        """
        self.turtle.pendown()

    def origin(self, any):
        """
        Déplace la tortue à l'origine (0;0) sans tracer de trait.
        """
        self.penup(any)
        self.turtle.goto(0, 0)
        self.pendown(any)

    def restore(self, any):
        """
        Remet le dessin à zéro.
        """
        self.turtle.reset()

    def clear(self, any):
        """
        Nettoie le parcours de la tortue.
        """
        self.turtle.clear()

    def fpos(self, coordinates):
        """
        Deplace la tortue aux coordonnées indiqué.

        :param coord: couple de coordonné
        :type coord: str
        """
        self.turtle.goto(eval(coordinates))

    def fcap(self, cap):
        """
        Tourne la tortue à l'angle indiqué (selon cercle trigonometrique).

        :param cap: angle
        :type cap: str
        """
        self.turtle.setheading(int(cap))

    def forward(self, amount):
        """
        Avance la tortue.

        :param amount: distance de deplacement
        :type amount: str
        """
        self.turtle.forward(int(amount))

    def back(self, amount):
        """
        Recule la tortue.

        :param amount: distance de deplacement
        :type amount: str
        """
        self.turtle.back(int(amount))

    def left(self, amount):
        """
        Tourne la tortue sur sa gauche.

        :param amount: angle de rotation
        :type amount: str
        """
        self.turtle.left(int(amount))

    def right(self, amount):
        """
        Tourne la tortue sur sa droite.

        :param amount: angle de rotation
        :type amount: str
        """
        self.turtle.right(int(amount))

    def end_application(self):
        self.running = 0


Visualizer(window)
window.mainloop()
