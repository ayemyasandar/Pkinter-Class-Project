from tkinter import *

class About:
    def __init__(self, root, panels):
        self.root = root
        self.panels = panels
        self.setUp()

    def setUp(self):
        button = Button(self.root, text="To Home Page",command=lambda : self.changeScene("home")).pack()

    def changeScene(self,scene):
        self.panels[scene].tkraise()
