from tkinter import * 

class Home:
    def __init__(self,root,panels):
        self.root = root 
        self.panels = panels
        self.setUp() 

    def setUp(self):
        button = Button(self.root,text="To About Page",command=lambda : self.changeScene("about")).pack()

    def changeScene(self,scene):
        self.panels[scene].tkraise()