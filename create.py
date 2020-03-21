from tkinter import *
from tkinter import messagebox
from db import *

class Create:
    def __init__(self, root, panels):
        self.root = root
        self.panels = panels
        self.setUp()

    def setUp(self):
        nameL = Label(self.root,text="Dish Name : ").grid(row=0,column=0)
        self.nameE = Entry(self.root)
        self.nameE.grid(row=0, column=1)

        priceL = Label(self.root,text="Dish Price : ").grid(row=1,column=0)
        self.priceE = Entry(self.root)
        self.priceE.grid(row=1,column=1)

        button = Button(self.root,text="Create",command=lambda : self.insertNewDish())
        button.grid(row=2,column=1)

    def changeScene(self,scene):
        self.panels[scene].tkraise()

    def insertNewDish(self):
        # createDishTable()
        name = self.nameE.get() 
        price = self.priceE.get()
        insertNewDish(name,price)
        self.changeScene("home")
