from tkinter import *
from tkinter import messagebox
from home import Home
from about import About


class Main:
    def __init__(self, root):
        self.root = root
        self.setUp()

    def setUp(self):
        self.sideFrame = Frame(self.root, width=200, height=500, bg="pink")
        self.topFrame = Frame(self.root, width=600, height=25, bg="blue")
        self.bottomFrame = Frame(self.root, width=600, height=25, bg="brown")
        self.homeFrame = Frame(self.root, width=600, height=450, bg="#ff8800")
        self.aboutFrame = Frame(self.root, width=600, height=450, bg="red")

        self.sideFrame.grid(row=0, column=0, sticky="w")
        self.topFrame.grid(row=0, column=1, sticky="n")
        self.bottomFrame.grid(row=0, column=1, sticky="s")
        self.homeFrame.grid(row=0, column=1)
        self.aboutFrame.grid(row=0, column=1)
        self.panels = {"home": self.homeFrame, "about": self.aboutFrame}
        home = Home(self.homeFrame, self.panels)
        about = About(self.aboutFrame, self.panels)

        self.panels["home"].tkraise()


root = Tk()
root.title("My Restaurant")
Main(root)
root.mainloop()

