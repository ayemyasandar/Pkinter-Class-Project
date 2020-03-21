from tkinter import *
from db import *
from tkinter import messagebox


class Home:
    def __init__(self, root, panels):
        self.root = root
        self.panels = panels
        self.setUp()

    def setUp(self):
        results = getAllDishes()
        t = 0
        for result in results:
            self.entry = Entry(self.root)
            self.entry.insert(1, result[0])
            self.entry.bind("",self.editDish(result[0]))
            self.entry.grid(row=t, column=0)

            self.entry = Entry(self.root)
            self.entry.insert(1, result[1])
            self.entry.grid(row=t, column=1)

            self.entry = Entry(self.root)
            self.entry.insert(1, result[2])
            self.entry.grid(row=t, column=2)
            t += 1

    def editDish(self, id):
        messagebox.showinfo("Edit", f"Current Edit Dish id is {id}")
