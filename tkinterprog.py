from tkinter import *

class window(Frame):
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()
    def init_window(self):
        self.master.title("GUI")
        self.pack(fill=BOTH, expand=1)
        #quitButton = Button(self, text="Quit", command=self.client_exit)
        #quitButton.place(x=10,y=10)
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(lable='Exit', command=self.client_exit)
        menu.add_cascade(lable='File', menu=file)

        edit = Menu(menu)
        edit.add_command(label='Undo')
        menu.add_cascade(label='Edit', menu=edit)
        
    def client_exit(self):
        exit()
    
root = Tk()
root.geometry('420x400')
app = window(root)
root.mainloop()