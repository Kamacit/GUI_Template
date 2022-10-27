import tkinter as tk 
from tkinter import font as tkfont
from tkinter import filedialog
from Startpage.Page0 import StartPage
from Site1.Page1 import PageOne
from Site2.Page2 import PageTwo
from Site3.Page3 import PageThree

class KamacitApps(tk.Tk):

    def __init__(self, *args, **kwargs):
        pages = [StartPage, PageOne, PageTwo, PageThree]
        tk.Tk.__init__(self, *args, **kwargs)
        self.geometry("300x300")
        self.title_font = tkfont.Font(family='Arial', size=10, weight="bold")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in pages:
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")
        self.menu()
    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()



    def menu(self):
        def NewFile():
            print("New File!")
        def OpenFile():
            name = filedialog.askopenfile()
            print(name)
        def About():
            newWindow = tk.Toplevel(self)
            newWindow.title("About")
            newWindow.geometry("200x200")
            tk.Label(newWindow,text="About").pack()
            
        menu = tk.Menu(self)
        self.config(menu=menu)
        filemenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=filemenu)
        filemenu.add_command(label="New", command=NewFile)
        filemenu.add_command(label="Open...", command=OpenFile)
        helpmenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About...", command=About)
        helpmenu.add_command(label="Exit", command=self.quit)
        


if __name__ == "__main__":
    app = KamacitApps()
    app.mainloop()