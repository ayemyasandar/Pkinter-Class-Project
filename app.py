from tkinter import *
from tkinter import messagebox
from home import Home
from create import Create


class Main:
    def __init__(self, root):
        self.root = root
        self.setUpMenu()
        self.setUp()

    def setUp(self):
        self.sideFrame = Frame(self.root, width=200, height=500, bg="pink")
        self.topFrame = Frame(self.root, width=600, height=25, bg="blue")
        self.bottomFrame = Frame(self.root, width=600, height=25, bg="brown")
        self.homeFrame = Frame(self.root, width=600, height=450)
        self.createFrame = Frame(self.root, width=600, height=450)

        self.sideFrame.grid(row=0, column=0, sticky="w")
        self.topFrame.grid(row=0, column=1, sticky="n")
        self.bottomFrame.grid(row=0, column=1, sticky="s")
        self.homeFrame.grid(row=0, column=1)
        self.createFrame.grid(row=0, column=1)
        self.panels = {"home": self.homeFrame, "create": self.createFrame}
        home = Home(self.homeFrame, self.panels)
        create = Create(self.createFrame, self.panels)

        self.panels["home"].tkraise()

    def setUpMenu(self):
        menu = Menu(self.root)
        self.root.config(menu=menu)

        fileMenu = Menu(menu)
        menu.add_cascade(label="File",menu=fileMenu)

        fileMenu.add_command(label="Home",command=lambda : self.changeScene("home"))
        fileMenu.add_command(label="Create", command=lambda: self.changeScene("create"))

        editMenu = Menu(menu)
        menu.add_cascade(label="Edit", menu=editMenu)


    def changeScene(self, scene):
            self.panels[scene].tkraise()

root = Tk()
root.title("My Restaurant")
Main(root)
root.mainloop()

