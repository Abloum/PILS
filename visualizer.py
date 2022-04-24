import queue
import turtle
from tkinter import Tk, Canvas

from ivy.std_api import *

window = Tk()


class Visualizer:

    def read_msg(self, *arg):
        print(str(arg[0]) + " a envoyé : " + arg[1])
        self.queue.put(arg[1])

    def __init__(self, master):
        self.master = master
        master.title("Visualizer")
        master.geometry("600x600")
        master.configure(bg="#FFFFFF")
        self.list_actions = []
        self.screenTurtle = Canvas(
            master,
            bg="#FFFFFF",
            height=600,
            width=600,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )
        self.screenTurtle.place(x=0, y=0)
        self.screen = turtle.TurtleScreen(self.screenTurtle)
        self.turtle = turtle.RawTurtle(self.screen, shape="turtle")

        IvyInit("Visualizer")
        IvyStart()
        IvyBindMsg(self.read_msg, "Draw:(.*)")
        self.queue = queue.Queue()
        self.running = 1
        self.periodicCall()

    def periodicCall(self):
        """
        Check every 100 ms if there is something new in the queue.
        """
        while not self.queue.empty():
            current = self.queue.get()
            tab = current.split()
            print(tab)

            func = getattr(Visualizer, tab[0])
            func(self, int(tab[1]))
            if (tab[0] != "redraw") & (tab[0] != "erase"):
                self.list_actions.append(tab)

        if not self.running:
            # This is the brutal stop of the system. You may want to do
            # some cleanup before actually shutting it down.
            import sys
            sys.exit(1)
        self.master.after(100, self.periodicCall)

    def redraw(self, any):
        self.turtle.reset()
        tmp = self.list_actions
        self.list_actions = []
        for i in range(len(tmp)):
            self.queue.put(str(tmp[i][0]) + " " + str(tmp[i][1]))

    def erase(self, index):
        self.list_actions.pop(index)

    def forward(self, amount):
        self.turtle.forward(amount)

    def back(self, amount):
        self.turtle.back(amount)

    def left(self, amount):
        self.turtle.left(amount)

    def right(self, amount):
        self.turtle.right(amount)

    def endApplication(self):
        self.running = 0


Visualizer(window)
window.mainloop()
