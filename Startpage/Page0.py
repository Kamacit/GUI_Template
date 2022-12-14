import tkinter as tk               
from tkinter import font as tkfont  

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="This is the start page", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tk.Button(self, text="Go to Page One",
                            command=lambda: controller.show_frame("PageOne")).pack()
        button2 = tk.Button(self, text="Go to Page Two",
                            command=lambda: controller.show_frame("PageTwo")).pack()
        button3 = tk.Button(self, text="Go to Page Three",
                            command=lambda: controller.show_frame("PageThree")).pack()