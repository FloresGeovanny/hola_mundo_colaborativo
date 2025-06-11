import tkinter as tk

class HolaMundo:
     def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hola mundo!")
        self.label = tk.Label(self.root,text= "Hola Mundo!")
        self. label.pack()
        self.root.mainloop()
HolaMundo()
